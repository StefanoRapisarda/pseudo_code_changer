#!/usr/bin/env python

"""Tests for `pseudo_code_changer` package."""

import pytest

from click.testing import CliRunner

from pseudo_code_changer import change_pseudo_code
from pseudo_code_changer import cli

CONTENT = "content"

def test_change_names(tmp_path):
    bad_dir = tmp_path / "2023127_bad_pcode_src"
    bad_dir.mkdir()

    bad_files = ['bad_pcode_test.txt','123bad_pcode.rsx','ertgbad_pcodeert.pdf']
    for f in bad_files:
        p = bad_dir / f
        p.write_text(CONTENT)        
    bad_dirs = ['bad_pcode_test','123bad_pcode','ertgbad_pcodeert']
    for d in bad_dirs:
        p = bad_dir / d
        p.mkdir()
    
    good_pcode = 'A23456'
    good_dir = tmp_path / f"2023127_{good_pcode}_src"
    good_files = [f.replace('bad_pcode',good_pcode) for f in bad_files]
    good_dirs = [d.replace('bad_pcode',good_pcode) for d in bad_dirs]

    change_pseudo_code('bad_pcode',good_pcode,path=tmp_path,confirm=False)

    assert good_dir.exists()
    for f in good_files:
        assert (good_dir/f).exists()
    for d in good_dirs:
        assert (good_dir/d).exists()


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'pseudo_code_changer.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output

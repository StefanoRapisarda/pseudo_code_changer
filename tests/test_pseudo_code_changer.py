#!/usr/bin/env python

"""Tests for `pseudo_code_changer` package."""

import pytest
from pathlib import Path

from click.testing import CliRunner

from ..pseudo_code_changer import change_pseudo_code
from ..functions import pcode_generator
# from pseudo_code_changer import cli

CONTENT = "content"

class TestChangePseudoCode:
    def preliminaries(self,tmp_path):
        self.names = ['bad_pcode_test','123bad_pcode','ertgbad_pcodeert']
        self.container = tmp_path / 'container_bad_pcode_dir'
        self.container.mkdir()

    def test_change_file_names(self,tmp_path):

        self.preliminaries(tmp_path)

        bad_files = []
        for name in self.names:
            bad_file = name + '.txt'
            bad_file_fullp = self.container / bad_file
            bad_file_fullp.write_text(CONTENT)
            bad_files += [bad_file]     
    
        good_pcode = pcode_generator()
        good_files = [f.replace('bad_pcode',good_pcode) for f in bad_files]

        change_pseudo_code('bad_pcode',good_pcode,path=self.container,
                            change_parent_dir=False,change_dirs=False,confirm=False)

        for f in good_files:
            assert (self.container/f).exists()
            assert (self.container/f).is_file()

    def test_change_dir_names(self,tmp_path):

        self.preliminaries(tmp_path)

        bad_dirs = []
        for name in self.names:
            bad_dir_fullp = self.container / name
            bad_dir_fullp.mkdir()
            bad_dirs += [name] 
        
        good_pcode = pcode_generator()
        good_dirs = [d.replace('bad_pcode',good_pcode) for d in bad_dirs]

        change_pseudo_code('bad_pcode',good_pcode,path=self.container,
                            change_parent_dir=False,change_files=False,confirm=False)

        for d in good_dirs:
            assert (self.container/d).exists()
            assert (self.container/d).is_dir()

    def test_change_parent_dir(self,tmp_path):

        self.preliminaries(tmp_path)

        good_pcode = pcode_generator()
        good_dir = Path(str(self.container).replace('bad_pcode',good_pcode))
 
        change_pseudo_code('bad_pcode',good_pcode,path=self.container,
                            change_dirs=False,change_files=False,confirm=False)
        
        assert good_dir.exists()
        assert good_dir.is_dir()

    def test_change_all(self,tmp_path):

        self.preliminaries(tmp_path)

        good_pcode = pcode_generator()
        good_dir = Path(str(self.container).replace('bad_pcode',good_pcode))

        bad_files = []
        bad_dirs = []
        for name in self.names:
            bad_file = name + '.txt'
            bad_file_fullp = self.container/bad_file
            bad_file_fullp.write_text(CONTENT)
            bad_files += [bad_file]   

            bad_dir_fullp = self.container / name
            bad_dir_fullp.mkdir()

        good_files = [f.replace('bad_pcode',good_pcode) for f in bad_files]   
        good_dirs = [d.replace('bad_pcode',good_pcode) for d in self.names]

        change_pseudo_code('bad_pcode',good_pcode,path=self.container,
                            confirm=False)
        
        assert good_dir.exists()
        assert good_dir.is_dir()
        for good_file,good_local_dir in zip(good_files,good_dirs):
            assert (good_dir/good_file).exists()
            assert (good_dir/good_file).is_file()
            assert (good_dir/good_local_dir).exists()
            assert (good_dir/good_local_dir).is_dir()

    def test_content_sub_dir_preserved(self,tmp_path):

        self.preliminaries(tmp_path)

        good_pcode = pcode_generator()   

        sub_dir = self.container/'sub_dir_bad_pcode'
        sub_dir.mkdir()
        good_sub_dir = Path(str(sub_dir).replace('bad_pcode',good_pcode))

        good_files = []
        for name in self.names:
            file_fullp = sub_dir/(name+'.txt') 
            file_fullp.write_text(CONTENT)
            good_files += [good_sub_dir/(name+'.txt')] 

        for item in self.container.iterdir(): print(item)
        print('='*72)
        for item in sub_dir.iterdir(): print(item) 

        change_pseudo_code('bad_pcode',good_pcode,path=self.container,confirm=False)

        for f in good_files:
            assert f.exists()
            assert f.is_file()

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

@pytest.mark.skip(reason="to be implemented yet")
def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'pseudo_code_changer.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output

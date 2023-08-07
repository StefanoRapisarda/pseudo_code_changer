import os
import pytest
from pseudo_code_changer.functions import make_dummy_dir_tree



class TestMakeDummyDirTree:

    def preliminaries(self,text='',make_parent=True,
                      text_in_parent=False,text_in_files=False, text_in_dirs=False):
        self.parent =make_dummy_dir_tree(text=text,make_parent=make_parent,
                                        text_in_parent=text_in_parent,
                                        text_in_files=text_in_files,
                                        text_in_dirs=text_in_dirs)

    def test_tree(self):
        self.preliminaries()
        assert self.parent.exists()
        assert self.parent.is_dir()

        files = [f for f in self.parent.iterdir() if f.is_file()]
        dirs  = [d for d in self.parent.iterdir() if d.is_dir()]

        assert len(files) == 3
        assert len(dirs) == 3
        
        self.clean_up()

    def test_text_in_parent(self):
        text = 'doppio_formaggio'
        self.preliminaries(text=text,text_in_parent=True)

        assert self.parent.exists()
        assert self.parent.is_dir()    
        assert text in str(self.parent)

        self.clean_up()

    def test_text_in_files(self):
        text = 'salsa_tonnata'
        self.preliminaries(text=text,text_in_files=True)

        files = [f for f in self.parent.iterdir() if f.is_file()]
        assert len(files) == 3

        for f in files: assert text in str(f)

        self.clean_up()

    def test_text_in_dirs(self):
        text = 'funghi'
        self.preliminaries(text=text,text_in_dirs=True)

        dirs = [d for d in self.parent.iterdir() if d.is_dir()]
        assert len(dirs) == 3

        for d in dirs: assert text in str(d)

        self.clean_up()

    def clean_up(self):
        os.system(f'rm -rf {self.parent}')

    
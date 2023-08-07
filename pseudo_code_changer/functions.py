import os
from pathlib import Path
import random
import uuid

from pseudo_code_changer.my_logging import LoggingWrapper

CONTENT = "content"

def make_fake_name(text=''):
    '''
    Generate a fake name containing the specified text
    '''
    random_name = str(uuid.uuid4())
    if text:
        n = len(random_name)
        i = random.randint(0,n-1)
        name = random_name[:i] + text + random_name[i:]
    else:
        name = random_name
    return name

def make_dummy_dir_tree(text='',path = Path.cwd(), make_parent=True,
                        text_in_parent=False,text_in_files=False, text_in_dirs=False):
    '''
    It creates a directory containing other directories and text files
    containing (if specified) a certain string. This is to be used 
    when testing pseudo_code_changer
    '''

    if make_parent:
        if text_in_parent: 
            parent_name = make_fake_name(text)
        else:
            parent_name = make_fake_name()
        parent = path/parent_name
        parent.mkdir()
    else:
        parent = path

    for d in range(3):
        if text_in_dirs and text:
            dir_name = make_fake_name(text)
        else:
            dir_name = make_fake_name()
        dir_full_path = parent/dir_name
        dir_full_path.mkdir()

    file_exts = ['.pdf','.txt','.qmd','.doc','.jpeg','.py','.R','.md']
    for f in range(3):
        if text_in_files and text:
            file_name = make_fake_name(text) + random.choice(file_exts)
        else:
            file_name = make_fake_name() + random.choice(file_exts)
        file_full_path = parent/file_name
        file_full_path.write_text(CONTENT)

    return parent

def pcode_generator():
    letter = random.choice(['A', 'B'])
    digits = random.randint(10000, 99999)
    return f'{letter}{digits}'

def change_names(old_string,new_string,path=Path.cwd(),
                 opt='f',confirm=True):
    '''
    Substitutes old string into new string in either files or directories
    contained in a specific directory (including the parent directory) 
    '''

    mylogging = LoggingWrapper()

    if opt == 'f': 
        items = [f'{item.name}' for item in path.iterdir() if not item.is_dir()]
        opt_descr = 'Files'
    elif opt == 'd':
        items = [f'{item.name}' for item in path.iterdir() if item.is_dir()]
        opt_descr = 'Directories'
    else:
        raise ValueError("opts['sel'] must be either f (files) or d (directory)")

    if not isinstance(path,Path): path = Path(path)

    old_names = []
    new_names = []

    for item in items:
        if old_string in item: 
            old_names += [item]
            new_names += [item.replace(old_string,new_string)]

    if old_names:

        proceed = True
        
        mylogging.info('\nReplacing summary')
        mylogging.info('-'*72)
        mylogging.info(f'Replacing {opt_descr}')
        mylogging.info(f'Directory: {path}')
        for i,(old,new) in enumerate(zip(old_names,new_names)):
            mylogging.info(f'{i+1}) {old} ---> {new}')
        mylogging.info('-'*72)

        if confirm:
            ans = input('Do you want to proceed?').strip().lower()
            if not ans in ['y','yes','ye']: proceed = False

        if proceed:
            for i,(old,new) in enumerate(zip(old_names,new_names)):
                os.rename(path/old,path/new)
            mylogging.info('Done!\n')

        return 1
    else:
        mylogging.info(f'No {opt_descr} matching your bad pcode has been found')

        return 0

def change_parent_dir_name(old_string,new_string,path=Path.cwd(),
                           confirm=True):
    '''
    Change the name of the specified directory substituing old_string
    with new_string
    '''
    
    mylogging = LoggingWrapper()

    # Changing name of current dir
    if old_string in path.name:
        proceed = True

        mylogging.info('\nReplacing summary')
        mylogging.info('-'*72)
        new_parent_dir = path.parent / path.name.replace(old_string,new_string)
        
        mylogging.info('Replacing parent directory')
        mylogging.info(f'{path} --> {new_parent_dir}')
        mylogging.info('-'*72)
    
        if confirm:
            ans = input('Do you want to proceed?').strip().lower()
            if not ans in ['y','yes','ye']: proceed = False

        if proceed:
            os.rename(path,new_parent_dir)
            mylogging.info('Done!'+'\n')

        return new_parent_dir
    else:
        mylogging.info('Your old string is not contained in the parent directory')
        return path
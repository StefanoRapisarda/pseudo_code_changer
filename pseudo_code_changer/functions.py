import os
from pathlib import Path
import random

from my_logging import LoggingWrapper

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

        return 1
    else:
        mylogging.info('Your old string is not contained in the parent directory')
        return 0
"""Main module."""

# INPUTS:
# - Directory
# - (List of) bad pseudo codes 
# - List of good pseudo codes or single pseudo code
# - User options
#   - Substitute folder names
#   - Substitute file names
#   - Both
# OUTPUTS:
# - Log file

# Tasks
# - Initialize log file;
# - Ask directory if not specified;
# - Locate all target directories (if option is specified);
# - Locate all target files (if option is specified);
# - Display changes;
# - Ask confirmation;
# - Apply changes;
# - Write changes in log file; 
# - Close log file and move it in the working directory;

import os
from pathlib import Path

from classes import PseudoCode
from my_logging import LoggingWrapper

def change_pseudo_code(bad_pcode,good_pcode,path=Path.cwd(),
    opts={'files':True,'dirs':True,'confirm':True}):
    
    if not isinstance(path,Path):
        path = Path(path)
    assert path.is_dir(), 'Directory does not exists'
    bad_pcode = str(bad_pcode)
    good_pcode = PseudoCode(good_pcode)

    mylogging = LoggingWrapper()

    files = [f'{item.name}' for item in path.iterdir() if not item.is_dir()]
    dirs = [f'{item.name}' for item in path.iterdir() if item.is_dir()]

    if opts['files']:
        files_flag = True
        old_files = []
        new_files = []

        for item in files:
            if bad_pcode in item: 
                old_files += [item]
                new_files += [item.replace(bad_pcode,good_pcode)]

        if old_files:
            mylogging.info('File replacing summary')
            mylogging.info('-'*72)
            mylogging.info(f'Directory: {path}')
            for i,(old,new) in enumerate(zip(old_files,new_files)):
                mylogging.info(f'{i+1}) {old} ---> {new}')
            mylogging.info('-'*72+'\n')

            if opts['confirm']:
                ans = input('Do you want to proceed?').strip().lower()
                if not ans in ['y','yes','ye']: files_flag = False

            if files_flag:
                for i,(old,new) in enumerate(zip(old_files,new_files)):
                    cmd = f'mv {old} {new}'
                    os.system(cmd)
                mylogging.info('Done!\n')
        else:
            mylogging.info('No file matching your bad pcode has been found')

    if opts['dirs']:
        dirs_flag = True
        old_dirs = []
        new_dirs = []

        for item in dirs:
            if bad_pcode in item: 
                old_dirs += [item]
                new_dirs += [item.replace(bad_pcode,good_pcode)]

        if old_dirs:
            mylogging.info('Directory replacing summary')
            mylogging.info('-'*72)
            mylogging.info(f'Directory: {path}')
            for i,(old,new) in enumerate(zip(old_dirs,new_dirs)):
                mylogging.info(f'{i+1}) {old} ---> {new}')
            mylogging.info('-'*72+'\n')

            if opts['confirm']:
                ans = input('Do you want to proceed?').strip().lower()
                if not ans in ['y','yes','ye']: dirs_flag = False

            if dirs_flag:
                for i,(old,new) in enumerate(zip(old_dirs,new_dirs)):
                    cmd = f'mv {old} {new}'
                    os.system(cmd)
                mylogging.info('Done!\n')
        else:
            mylogging.info('No directory matching your band pcode has been found')

        # Changing name of current dir
        if bad_pcode in path.name:
            parent_dir_flag = True 
            new_parent_dir = path.parent / path.name.replace(bad_pcode,good_pcode)
            
            mylogging.info('Replacing parent directory')
            mylogging.info(f'{path} --> {new_parent_dir}')
        
            if opts['confirm']:
                ans = input('Do you want to proceed?').strip().lower()
                if not ans in ['y','yes','ye']: parent_dir_flag = False

            if parent_dir_flag:
                Path.mkdir(new_parent_dir)
                os.system(f'mv -r {path}/* {new_parent_dir}/')
                mylogging.info('Done!'+'\n')
        else:
            mylogging.info('Your bad pcode is not contained in the parent directory')




if __name__ == '__main__':
    change_pseudo_code('code','B12345')
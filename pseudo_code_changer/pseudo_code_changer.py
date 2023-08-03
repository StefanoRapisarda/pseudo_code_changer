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

def change_pseudo_code(bad_pcode,good_pcode,path=Path.cwd(),
    opts={'files':True,'dirs':True,'confirm':True}):
    
    if not isinstance(path,Path):
        path = Path(path)
    assert path.is_dir(), 'Directory does not exists'
    bad_pcode = str(bad_pcode)
    good_pcode = PseudoCode(good_pcode)

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

        print('File replacing summary')
        print('-'*72)
        print(f'Directory: {path}')
        for i,(old,new) in enumerate(zip(old_files,new_files)):
            print(f'{i+1}) {old} ---> {new}')
        print('-'*72+'\n')

        if opts['confirm']:
            ans = input('Do you want to proceed?').strip().lower()
            if not ans in ['y','yes','ye']: files_flag = False

        if files_flag:
            for i,(old,new) in enumerate(zip(old_files,new_files)):
                cmd = f'mv {old} {new}'
                os.system(cmd)
            print('Done!\n')



if __name__ == '__main__':
    change_pseudo_code('re','')
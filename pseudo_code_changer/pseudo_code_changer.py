import os
import sys
from pathlib import Path

from classes import PseudoCode
from functions import change_names,change_parent_dir_name, make_dummy_dir_tree
from my_logging import LoggingWrapper, get_logger_name, initialize_logger, loggers

def change_pseudo_code(bad_pcode,good_pcode,path=Path.cwd(),
    change_files=True,change_dirs=True,change_parent_dir=True,confirm=True,log=True):

    if not isinstance(path,Path):
        path = Path(path)
    assert path.is_dir(), 'Directory does not exists'
    bad_pcode = str(bad_pcode)
    good_pcode = PseudoCode(good_pcode)

    if log:
        log_name = get_logger_name('change_pseudo_code')
        full_log_name = Path.cwd()/log_name
        logger = initialize_logger(full_log_name)
        loggers[log_name] = logger

    mylogging = LoggingWrapper()

    mylogging.info('User specified options:')
    mylogging.info(f'String to substitute: {bad_pcode}')
    mylogging.info(f'Specified pseudo code: {good_pcode}')
    mylogging.info(f'Target directory: {path}')
    mylogging.info(f'Change parent directory: {change_parent_dir}')
    mylogging.info(f'Change dirs: {change_dirs}')
    mylogging.info(f'Change files: {change_files}')
    mylogging.info(f'Log file name: {log_name}')
    mylogging.info('-'*72+'\n')

    if change_files:
        change_names(bad_pcode,good_pcode,path=path,opt='f',
                     confirm=confirm)
    if change_dirs:
        change_names(bad_pcode,good_pcode,path=path,opt='d',
                     confirm=confirm)        
    if change_parent_dir:
        parent_dir = change_parent_dir_name(bad_pcode,good_pcode,path=path,
                               confirm=confirm)
    else:
        parent_dir = path
        
    if log:
        os.system(f'mv {full_log_name}.log {parent_dir}')


if __name__ == '__main__':
    sys.path.append('/Users/xizg0003/Documents/programming_playground')
    test_dir = '/Users/xizg0003/Documents/programming_playground/test_pcode'
    parent = make_dummy_dir_tree('provola',make_parent=True,text_in_parent=True,
                        text_in_files=True,text_in_dirs=True)
    change_pseudo_code('provola','B12345',path=parent,confirm=False,change_parent_dir=True)
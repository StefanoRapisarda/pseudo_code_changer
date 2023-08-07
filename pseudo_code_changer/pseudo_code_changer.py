import os
from pathlib import Path

from pseudo_code_changer.classes import PseudoCode
from pseudo_code_changer.functions import change_names,change_parent_dir_name
from pseudo_code_changer.my_logging import LoggingWrapper, get_logger_name, initialize_logger, loggers

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
        os.system(f'mv {full_log_name} {parent_dir}')


if __name__ == '__main__':
    change_pseudo_code('code','B12345')
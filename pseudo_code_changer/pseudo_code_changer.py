from pathlib import Path

from pseudo_code_changer.classes import PseudoCode
from pseudo_code_changer.functions import change_names,change_parent_dir_name
from pseudo_code_changer.my_logging import LoggingWrapper

def change_pseudo_code(bad_pcode,good_pcode,path=Path.cwd(),
    change_files=True,change_dirs=True,change_parent_dir=True,confirm=True):

    if not isinstance(path,Path):
        path = Path(path)
    assert path.is_dir(), 'Directory does not exists'
    bad_pcode = str(bad_pcode)
    good_pcode = PseudoCode(good_pcode)

    mylogging = LoggingWrapper()

    if change_files:
        change_names(bad_pcode,good_pcode,path=path,opt='f',
                     confirm=confirm)
    if change_dirs:
        change_names(bad_pcode,good_pcode,path=path,opt='d',
                     confirm=confirm)        
    if change_parent_dir:
        change_parent_dir_name(bad_pcode,good_pcode,path=path,
                               confirm=confirm)


if __name__ == '__main__':
    change_pseudo_code('code','B12345')
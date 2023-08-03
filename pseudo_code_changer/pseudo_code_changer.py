from pathlib import Path

from classes import PseudoCode
from functions import change_names,change_parent_dir_name
from my_logging import LoggingWrapper

def change_pseudo_code(bad_pcode,good_pcode,path=Path.cwd(),
    opts={'files':True,'dirs':True,'parent_dir':True,'confirm':True}):
    
    if not isinstance(path,Path):
        path = Path(path)
    assert path.is_dir(), 'Directory does not exists'
    bad_pcode = str(bad_pcode)
    good_pcode = PseudoCode(good_pcode)

    mylogging = LoggingWrapper()

    if opts['files']:
        change_names(bad_pcode,good_pcode,path=path,opt='f',
                     confirm=opts['confirm'])
    if opts['dirs']:
        change_names(bad_pcode,good_pcode,path=path,opt='d',
                     confirm=opts['confirm'])        
    if opts['parent_dir']:
        change_parent_dir_name(bad_pcode,good_pcode,path=path,
                               confirm=opts['confirm'])


if __name__ == '__main__':
    change_pseudo_code('code','B12345')
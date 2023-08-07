"""Console script for pseudo_code_changer."""
import sys
import click
from pathlib import Path

from pseudo_code_changer.pseudo_code_changer import change_pseudo_code


@click.command()
@click.option('-f', '--files', 'file_flag', 
              is_flag=True, show_default=True, default=False, 
              help='Change file names inside specified directory')
@click.option('-r', '--dirs', 'dir_flag', 
              is_flag=True, show_default=True, default=False, 
              help='Change directory names inside specified directory')
@click.option('-p', '--parent', 'parent_flag', 
              is_flag=True, show_default=True, default=False, 
              help='Change name of the specified input directory')
@click.option('-c', '--confirm', 'confirm_flag', 
              is_flag=True, show_default=True, default=False, 
              help='Ask for confirmation before changing names')  
@click.argument('bad_pcode', nargs=1, metavar='<bad_pseudo_code>')
@click.argument('good_pcode',nargs=1, metavar='<good_pseudo_code>')
@click.argument('path', nargs=-1, metavar='<directory>') 
def main(bad_pcode,good_pcode,path,file_flag,dir_flag,parent_flag,confirm_flag):
    """
    The script changes names of files and directory substituting bad
    pseudo codes (or generic string) with good (user specified) pseudo code.

    If <directory> is not specified, it will be assumed as the current directory.
    If it is a file, the script will read lines inside it assuming they are path
    and it will run in every specified directory.
    If it is a squence of paths, it will run over them.
    """

    if not (file_flag and dir_flag and parent_flag):
        print('No options has been specified')
        print('Check --help and choose -r, -f, -p or a combination of these')
        return 0
    
    if not path: 
        change_pseudo_code(bad_pcode,good_pcode,
                           change_files=file_flag,
                           change_dirs=dir_flag,
                           change_parent_dir=parent_flag,
                           confirm=confirm_flag)
    else:
        for item in path:
            if 'txt' in item:
                if not Path(item).is_file(): 
                    print(f'File {item} does not exist. Skipping')
                    continue
                with open(item,'rb') as infile:
                    paths = infile.readlines()
                for local_path in paths:
                    local_path = local_path.strip()
                    if not Path(local_path).is_dir():
                        print(f'Directory {local_path} does not exist. Skipping')
                        continue
                    change_pseudo_code(bad_pcode,good_pcode,path=local_path,
                        change_files=file_flag,
                        change_dirs=dir_flag,
                        change_parent_dir=parent_flag,
                        confirm=confirm_flag)
            else:
                change_pseudo_code(bad_pcode,good_pcode,path=item,
                    change_files=file_flag,
                    change_dirs=dir_flag,
                    change_parent_dir=parent_flag,
                    confirm=confirm_flag)                

    return 0


if __name__ == "__main__":
    main()  # pragma: no cover

"""Console script for pseudo_code_changer."""
import sys
import click


@click.command()
@click.option('-f', '--files', 'file_flag', 
              is_flag=True, show_default=True, default=True, 
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
@click.argument('path',nargs=1, metavar='<directory>') 
def main(file_flag,dir_flag,confirm_flag,bad_pcode,good_pcode,path):
    """
    The script changes names of files and directory substituting bad
    pseudo codes (or generic string) with good (user specified) pseudo code.
    If <directory> is not specified, it will be assumed as the current directory.
    """
    click.echo("Replace this message by putting your code into "
               "pseudo_code_changer.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    main()  # pragma: no cover

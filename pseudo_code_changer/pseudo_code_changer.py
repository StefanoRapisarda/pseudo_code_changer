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

import pathlib

def change_pseudo_code(path,bad_pseudo,good_pseudo):
    pass
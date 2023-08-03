# NOTE: 
# 2023 08 03, Stefano Rapisarda:
# Defining a class for a pseudo code seems a but an overshooting, but
# there may be some extra functionality to be added in the future
# related to that, so... that's it

import re 

class PseudoCode(str):
    def __new__(cls,code=''):
        instance = super().__new__(cls, code)
        if instance:
            assert len(instance) == 6, 'Pseudo code must contain exactly 6 characters'
            assert instance[0] in ['A','B'], 'First character must be either A or B'
            assert instance[1:].isnumeric(), 'All but first character must be numbers'
        return instance

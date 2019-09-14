import os
import sys
from .helper import prnt_iteratable

def prnt(*obj, enable=True, both=False, truncate=False,
        sep='', end='\n', file=sys.stdout, flush=False,
        width=os.get_terminal_size().columns or 50):
    # Separator in action
    if len(obj) > 1 and sep != '':
        print(*obj, sep=sep, end=end, file=file, flush=flush)
        return

    for i, o in enumerate(obj):
        if enable and (type(o) == list or type(o) == dict):
            if both: print(o, sep=sep, end='\n', file=file, flush=flush)
            prnt_iteratable(o, end=end, truncate=truncate, width=width)
        else:
            trailing = end if (len(obj) >= 1) and (i == len(obj) - 1) else " "
            print(o, sep=sep, end=trailing, file=file, flush=flush)

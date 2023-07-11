#!/usr/bin/python3

import json


import pydoc

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter


def colored_help(obj):
    pydoc.pipepager(highlight(pydoc.render_doc(
        obj), PythonLexer(), TerminalFormatter()))


data = {'name': 'John', 'age': 30, 'city': 'New York'}

print(type(data))
json_string = json.dumps(data)
print(type(json_string))


help(open)

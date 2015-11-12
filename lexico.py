import collections
import re

Token = collections.namedtuple('Token', ['typ', 'value', 'line', 'column'])

def tokenize(code):
    keywords = {'ALT', 'ELSE', 'END', 'LEFT', 'LOOP', 'NOTE', 'OF', 'TITLE', 'NEWLINE'}
    token_specification = [
        ('MENSAJE',     r'->'), # NEW MESSAGE A -> B
        ('CONTENT',     r':'),          # A -> B: CONTENT
        ('LEFT',        r'LEFT|OVER|RIGHT|left|over|right'),           # Any other character
        ('TEXT',        r'[A-Za-z|(|)|0-9|,|*|$|%|@|&|-|_]+'),   # Identifiers
        ('NEWLINE',     r'\n'),          # Line endings
        ('SKIP',        r'[ \t]+'),      # Skip over spaces and tabs
        ('MISMATCH',    r'.'),           # Any other character
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    line_num = 1
    line_start = 0
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group(kind)
        if kind == 'NEWLINE':
            column = mo.start() - line_start
            yield Token(kind, value, line_num, column)
            line_start = mo.end()
            line_num += 1
        elif kind == 'SKIP':
            pass
        elif kind == 'MISMATCH':
            raise RuntimeError('%r unexpected on line %d' % (value, line_num))
        else:
            if kind == 'TEXT' and value.upper() in keywords:
                kind = value.upper()
            column = mo.start() - line_start
            yield Token(kind, value, line_num, column)

# Ref Bibliografica: https://docs.python.org/3/library/re.html
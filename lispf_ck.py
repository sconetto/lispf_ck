import ox

lexer = ox.make_lexer([
    ('NUMBER', r'\d+(\.\d*)?'),
    ('LPAR', r'\('),
    ('RPAR', r'\)'),
    ('DEF_FUNC', r'def'),
    ('EXEC_BLOCK', r'do'),
    ('LOOP', r'loop'),
    ('PRINT', r'print'),
    ('READ', r'read'),
    ('DEC', r'dec'),
    ('INC', r'inc'),
    ('LEFT', r'left'),
    ('RIGHT', r'right'),
    ('DO_BEFORE', r'do\-before'),
    ('DO_AFTER', r'do\-after'),
    ('ADD', r'add'),
    ('SUB', r'sub'),
    ('COMMENT', r'\;([^\n\r]+)'),
    ('NAME', r'[a-zA-z]+\d*'),
])

token_list = ['NUMBER', 'LPAR', 'RPAR', 'DEF_FUNC', 'EXEC_BLOCK', 'LOOP',
              'PRINT', 'READ', 'DEC', 'INC', 'LEFT', 'RIGHT', 'DO_BEFORE',
              'DO_AFTER', 'ADD', 'SUB', 'COMMENT', 'NAME']

parser = ox.make_parser ([

], token_list)

lisp_entry = input('Enter the lisp code: ')

tokens = lexer(lisp_entry)
print('Tokens:\n', tokens)

ast = parser(tokens)
print('AST:\n', ast)

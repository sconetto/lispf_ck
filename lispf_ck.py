import ox
import click

@click.command()
@click.argument('lispf_ck',type=click.File('r'))

def ast_lispf_fc(lispf_ck):
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

    source = lispf_ck.read()

    lisp_entry = []
    for data in source:
        lisp_entry.append(data)


    tokens = lexer(lisp_entry)
    print('Tokens:\n', tokens)

    ast = parser(tokens)
    print('AST:\n', ast)


if __name__ == "__main__":
    run = ast_lispf_fc()

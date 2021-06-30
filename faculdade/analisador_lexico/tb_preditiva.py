import enum
from tag import Tag
from enum import Enum

class Tb_rule(Enum):
    prog =          [[Tag.KW_PROGRAM, Tag.ID, 'body' ]]
    body =          [['decl-list', Tag.SMB_OBC, 'stmt-list', Tag.SMB_CBC]]
    decl_list =     [['decl', Tag.SMB_SEM, 'decl-list'], []]
    decl =          [['type', Tag.SMB_SEM, 'decl-list'], []]
    type =          [[Tag.KW_NUM], [Tag.KW_CHAR]]
    id_list =       [[Tag.ID, 'id_list_']]
    id_list_ =      [[Tag.SMB_COM, 'id_list'], []]

    stmt_list =     [['stmt', Tag.SMB_SEM], []]
    stmt =          [['assign_stmt', Tag.SMB_SEM], ['if_stmt'], ['read_stmt'], ['write_stmt']]
    assign_smt =    [[Tag.ID, Tag.OP_EQ, 'simple_expr']]
    if_smt =        [[Tag.KW_IF, Tag.SMB_OPA, 'expression', Tag.SMB_CPA, Tag.SMB_OBC, 'stmt_list', Tag.SMB_CBC, 'if_stmt_' ]]
    if_smt_ =       [[Tag.KW_ELSE, Tag.SMB_OBC, 'stmt_list', Tag.SMB_CBC ], []]
    while_stmt =    [['stmt_prefix', Tag.SMB_OBC, 'stmt_list', Tag.SMB_CBC]]
    stmt_prefix =   [[Tag.KW_WHILE, Tag.SMB_OPA, 'expression', Tag.SMB_CPA]]
    read_stmt =     [[Tag.KW_READ, Tag.ID]]
    write_stmt =    [[Tag.KW_WRITE, 'simple_expr']]

    expression =    [['simple_expr', 'expression_']]
    expression_ =   [['logop', 'simple_expr', 'expression_'], []]
    simple_expr =   [['term', 'simple_expr_']]
    simple_expr_ =  [['relop', 'term', 'simple_expr_'], []]
    term =          [['factor_b', 'term_']]
    term_ =         [['addop', 'factor_b', 'term_'], []]
    factor_b =      [['factor_a', 'factor_b_']]
    factor_b_ =     [['addop', 'factor_a', 'factor_b_'], []]
    factor_a =      [['factor'], [Tag.KW_NOT, 'factor']]
    factor =        [[Tag.ID], ['constant'], [Tag.SMB_OPA, 'expression', Tag.SMB_CPA]]

    logop =         [[Tag.KW_OR], [Tag.KW_AND]]
    relop =         [[Tag.OP_LE], [Tag.OP_GE], [Tag.OP_LT], [Tag.OP_GT], [Tag.OP_EQ], [Tag.OP_NE]]
    addop =         [[Tag.OP_AD], [Tag.OP_MIN]]
    mulop =         [[Tag.OP_MUL], [Tag.OP_DIV]]
    constant =      [[Tag.KW_NUM], [Tag.KW_CHAR]]

_TB={
    ('prog', 'program'):    Tb_rule.prog.value[0],
    ('body', '{'):          Tb_rule.body.value[0],          
    ('body', 'num'):        Tb_rule.body.value[0],
    ('body', 'char'):       Tb_rule.body.value[0],
    ('decl-list', '{'):     Tb_rule.decl_list.value[0],
    ('decl-list', 'num'):   Tb_rule.decl_list.value[1],
    ('decl-list', 'char'):  Tb_rule.decl_list.value[1],
}


print(_TB['prog','program' ])
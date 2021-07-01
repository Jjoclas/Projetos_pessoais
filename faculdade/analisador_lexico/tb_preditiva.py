import enum
from tag import Tag
from enum import Enum

class Tb_rule(Enum):
    prog =          [[Tag.KW_PROGRAM, Tag.ID, 'body' ]] # 1
    body =          [['decl_list', Tag.SMB_OBC, 'stmt_list', Tag.SMB_CBC]] # 2
    decl_list =     [['decl', Tag.SMB_SEM, 'decl_list'], []] # 3, 4
    decl =          [['_type', Tag.SMB_SEM, 'decl_list'], []] # 5
    _type =         [[Tag.KW_NUM], [Tag.KW_CHAR]] # 6, 7
    id_list =       [[Tag.ID, 'id_list_']] # 8
    id_list_ =      [[Tag.SMB_COM, 'id_list'], []] # 9, 10

    stmt_list =     [['stmt', Tag.SMB_SEM, 'stmt_list'], []] # 11, 12
    stmt =          [['assign_stmt'], ['if_stmt'], ['while_stmt'], ['read_stmt'], ['write_stmt']] # 13, 14, 15, 16, 17
    assign_stmt =   [[Tag.ID, Tag.OP_ATRIB, 'simple_expr']] # 18
    if_stmt =       [[Tag.KW_IF, Tag.SMB_OPA, 'expression', Tag.SMB_CPA, Tag.SMB_OBC, 'stmt_list', Tag.SMB_CBC, 'if_stmt_' ]] # 19
    if_stmt_ =      [[Tag.KW_ELSE, Tag.SMB_OBC, 'stmt_list', Tag.SMB_CBC ], []] # 20, 21
    while_stmt =    [['stmt_prefix', Tag.SMB_OBC, 'stmt_list', Tag.SMB_CBC]] # 22
    stmt_prefix =   [[Tag.KW_WHILE, Tag.SMB_OPA, 'expression', Tag.SMB_CPA]] # 23
    read_stmt =     [[Tag.KW_READ, Tag.ID]] # 24
    write_stmt =    [[Tag.KW_WRITE, 'simple_expr']] # 25

    expression =    [['simple_expr', 'expression_']] # 26
    expression_ =   [['logop', 'simple_expr', 'expression_'], []] # 27, 28
    simple_expr =   [('term', 'simple_expr_')] # 29
    simple_expr_ =  [['relop', 'term', 'simple_expr_'], []] # 30, 31
    term =          [['factor_b', 'term_']] # 32
    term_ =         [['addop', 'factor_b', 'term_'], []] # 33, 34
    factor_b =      [['factor_a', 'factor_b_']] # 35
    factor_b_ =     [['mulop', 'factor_a', 'factor_b_'], []] # 36, 37
    factor_a =      [['factor'], [Tag.KW_NOT, 'factor']] # 38, 39
    factor =        [[Tag.ID], ['constant'], [Tag.SMB_OPA, 'expression', Tag.SMB_CPA]] # 40, 41, 42

    logop =         [[Tag.KW_OR], [Tag.KW_AND]] # 43, 44
    relop =         [[Tag.OP_EQ], [Tag.OP_GT], [Tag.OP_GE], [Tag.OP_LT], [Tag.OP_LE], [Tag.OP_NE]] # 45, 46, 47, 48, 49, 50
    addop =         [[Tag.OP_AD], [Tag.OP_MIN]] # 51, 52
    mulop =         [[Tag.OP_MUL], [Tag.OP_DIV]] # 53, 54
    constant =      [[Tag.NUM], [Tag.CHAR]] # 55, 56

TB={
    ('prog', Tag.KW_PROGRAM):       Tb_rule.prog.value[0], # 1
    
    ('body', Tag.SMB_OBC):          Tb_rule.body.value[0],  # 2        
    ('body', Tag.KW_NUM):           Tb_rule.body.value[0],  # 2
    ('body', Tag.KW_CHAR):          Tb_rule.body.value[0],  # 2
    
    ('decl_list', Tag.KW_NUM):      Tb_rule.decl_list.value[0], # 3
    ('decl_list', Tag.KW_CHAR):     Tb_rule.decl_list.value[0], # 3
    ('decl_list', Tag.SMB_OBC):     Tb_rule.decl_list.value[1], # 4
    
    ('decl', Tag.KW_NUM):           Tb_rule.decl.value[0],
    ('decl', Tag.KW_CHAR):          Tb_rule.decl.value[0],
    
    ('_type', Tag.KW_NUM):          Tb_rule._type.value[0],
    ('_type', Tag.KW_CHAR):         Tb_rule._type.value[1],
    
    ('id_list', Tag.ID):            Tb_rule.id_list.value[0],
    ('id_list_', Tag.SMB_COM):      Tb_rule.id_list_.value[0],
    ('id_list_', Tag.SMB_SEM):      Tb_rule.id_list_.value[1],
    
    ('stmt_list', Tag.ID):          Tb_rule.stmt_list.value[0],
    ('stmt_list', Tag.KW_IF):       Tb_rule.stmt_list.value[0],
    ('stmt_list', Tag.KW_WRITE):    Tb_rule.stmt_list.value[0],
    ('stmt_list', Tag.KW_READ):     Tb_rule.stmt_list.value[0],
    ('stmt_list', Tag.KW_WHILE):    Tb_rule.stmt_list.value[0],
    ('stmt_list', Tag.SMB_CBC):     Tb_rule.stmt_list.value[1],
    
    ('stmt', Tag.ID):               Tb_rule.stmt.value[0],
    ('stmt', Tag.KW_IF):            Tb_rule.stmt.value[1],
    ('stmt', Tag.KW_WHILE):         Tb_rule.stmt.value[2],
    ('stmt', Tag.KW_READ):          Tb_rule.stmt.value[3],
    ('stmt', Tag.KW_WRITE):         Tb_rule.stmt.value[4],
    
    ('assign_stmt', Tag.ID):        Tb_rule.assign_stmt.value[0],
    ('if_stmt', Tag.KW_IF):         Tb_rule.if_stmt.value[0],
    ('if_stmt_', Tag.KW_ELSE):      Tb_rule.if_stmt_.value[0],
    ('if_stmt_', Tag.SMB_SEM):      Tb_rule.if_stmt_.value[1],
    ('while_stmt', Tag.KW_WHILE):   Tb_rule.while_stmt.value[0],
    ('stmt_prefix', Tag.KW_WHILE):  Tb_rule.stmt_prefix.value[0],
    ('read_stmt', Tag.KW_READ):     Tb_rule.read_stmt.value[0],
    ('write_stmt', Tag.KW_WRITE):   Tb_rule.write_stmt.value[0],

    ('expression', Tag.ID):         Tb_rule.expression.value[0],
    ('expression', Tag.SMB_OPA):    Tb_rule.expression.value[0],
    ('expression', Tag.KW_NOT):     Tb_rule.expression.value[0],
    ('expression', Tag.NUM):        Tb_rule.expression.value[0],
    ('expression', Tag.CHAR):       Tb_rule.expression.value[0],
    ('expression_', Tag.KW_AND):    Tb_rule.expression_.value[0],
    ('expression_', Tag.KW_OR):     Tb_rule.expression_.value[0],
    ('expression_', Tag.SMB_CPA):   Tb_rule.expression_.value[1],

    ('simple_expr', Tag.ID):        Tb_rule.simple_expr.value[0],
    ('simple_expr', Tag.SMB_OPA):   Tb_rule.simple_expr.value[0],
    ('simple_expr', Tag.KW_NOT):    Tb_rule.simple_expr.value[0],
    ('simple_expr', Tag.NUM):       Tb_rule.simple_expr.value[0],
    ('simple_expr', Tag.CHAR):      Tb_rule.simple_expr.value[0],
    
    ('simple_expr_', Tag.OP_LE):    Tb_rule.simple_expr_.value[0],
    ('simple_expr_', Tag.OP_GE):    Tb_rule.simple_expr_.value[0],
    ('simple_expr_', Tag.OP_LT):    Tb_rule.simple_expr_.value[0],
    ('simple_expr_', Tag.OP_GT):    Tb_rule.simple_expr_.value[0],
    ('simple_expr_', Tag.OP_EQ):    Tb_rule.simple_expr_.value[0],
    ('simple_expr_', Tag.OP_NE):    Tb_rule.simple_expr_.value[0],
    ('simple_expr_', Tag.SMB_SEM):  Tb_rule.simple_expr_.value[1],
    ('simple_expr_', Tag.SMB_CPA):  Tb_rule.simple_expr_.value[1],
    ('simple_expr_', Tag.KW_AND):   Tb_rule.simple_expr_.value[1],
    ('simple_expr_', Tag.KW_OR):    Tb_rule.simple_expr_.value[1],

    ('term', Tag.ID):               Tb_rule.term.value[0],
    ('term', Tag.SMB_OPA):          Tb_rule.term.value[0],
    ('term', Tag.KW_NOT):           Tb_rule.term.value[0],
    ('term', Tag.NUM):              Tb_rule.term.value[0],
    ('term', Tag.CHAR):             Tb_rule.term.value[0],

    ('term_', Tag.OP_AD):           Tb_rule.term_.value[0],
    ('term_', Tag.OP_MIN):          Tb_rule.term_.value[0],
    ('term_', Tag.SMB_SEM):         Tb_rule.term_.value[1],
    ('term_', Tag.SMB_CPA):         Tb_rule.term_.value[1],
    ('term_', Tag.KW_AND):          Tb_rule.term_.value[1],
    ('term_', Tag.KW_OR):           Tb_rule.term_.value[1],
    ('term_', Tag.OP_LE):           Tb_rule.term_.value[1],
    ('term_', Tag.OP_GE):           Tb_rule.term_.value[1],
    ('term_', Tag.OP_LT):           Tb_rule.term_.value[1],
    ('term_', Tag.OP_GT):           Tb_rule.term_.value[1],
    ('term_', Tag.OP_EQ):           Tb_rule.term_.value[1],
    ('term_', Tag.OP_NE):           Tb_rule.term_.value[1],

    ('factor_b', Tag.ID):           Tb_rule.factor_b.value[0],
    ('factor_b', Tag.SMB_OPA):      Tb_rule.factor_b.value[0],
    ('factor_b', Tag.KW_NOT):       Tb_rule.factor_b.value[0],
    ('factor_b', Tag.NUM):          Tb_rule.factor_b.value[0],
    ('factor_b', Tag.CHAR):         Tb_rule.factor_b.value[0],

    ('factor_b_', Tag.OP_MUL):      Tb_rule.factor_b_.value[0],
    ('factor_b_', Tag.OP_DIV):      Tb_rule.factor_b_.value[0],
    ('factor_b_', Tag.OP_AD):       Tb_rule.factor_b_.value[1],
    ('factor_b_', Tag.OP_MIN):      Tb_rule.factor_b_.value[1],
    ('factor_b_', Tag.SMB_SEM):     Tb_rule.factor_b_.value[1],
    ('factor_b_', Tag.SMB_CPA):     Tb_rule.factor_b_.value[1],
    ('factor_b_', Tag.KW_AND):      Tb_rule.factor_b_.value[1],
    ('factor_b_', Tag.KW_OR):       Tb_rule.factor_b_.value[1],
    ('factor_b_', Tag.OP_LE):       Tb_rule.factor_b_.value[1],
    ('factor_b_', Tag.OP_GE):       Tb_rule.factor_b_.value[1],
    ('factor_b_', Tag.OP_LT):       Tb_rule.factor_b_.value[1],
    ('factor_b_', Tag.OP_GT):       Tb_rule.factor_b_.value[1],
    ('factor_b_', Tag.OP_EQ):       Tb_rule.factor_b_.value[1],
    ('factor_b_', Tag.OP_NE):       Tb_rule.factor_b_.value[1],

    ('factor_a', Tag.ID):           Tb_rule.factor_a.value[0],
    ('factor_a', Tag.SMB_OPA):      Tb_rule.factor_a.value[0],
    ('factor_a', Tag.NUM):          Tb_rule.factor_a.value[0],
    ('factor_a', Tag.CHAR):         Tb_rule.factor_a.value[0],
    ('factor_a', Tag.KW_NOT):       Tb_rule.factor_a.value[1],

    ('factor', Tag.ID):             Tb_rule.factor.value[0],
    ('factor', Tag.NUM):            Tb_rule.factor.value[1],
    ('factor', Tag.CHAR):           Tb_rule.factor.value[1],
    ('factor', Tag.SMB_OPA):        Tb_rule.factor.value[2],

    ('logop', Tag.KW_OR):           Tb_rule.logop.value[0],
    ('logop', Tag.KW_AND):          Tb_rule.logop.value[1],

    ('relop', Tag.OP_EQ):           Tb_rule.relop.value[0],
    ('relop', Tag.OP_GT):           Tb_rule.relop.value[1],
    ('relop', Tag.OP_GE):           Tb_rule.relop.value[2],
    ('relop', Tag.OP_LT):           Tb_rule.relop.value[3],
    ('relop', Tag.OP_LE):           Tb_rule.relop.value[4],
    ('relop', Tag.OP_NE):           Tb_rule.relop.value[5],

    ('addop', Tag.OP_MIN):          Tb_rule.addop.value[0],
    ('addop', Tag.OP_AD):           Tb_rule.addop.value[1],

    ('mulop', Tag.OP_MUL):          Tb_rule.mulop.value[0],
    ('mulop', Tag.OP_DIV):          Tb_rule.mulop.value[1],

    ('constant', Tag.NUM):          Tb_rule.constant.value[0],
    ('constant', Tag.CHAR):         Tb_rule.constant.value[0]
}

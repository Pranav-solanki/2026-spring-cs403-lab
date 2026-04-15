from dataclasses import dataclass
from typing import List, Optional

class ASTNode:
    pass

@dataclass
class Program(ASTNode):
    declarations: List[ASTNode]

@dataclass
class VarDecl(ASTNode):
    var_type: str
    var_name: str

@dataclass
class ArrayDecl(ASTNode):
    var_type: str
    var_name: str
    size: int

@dataclass
class ArrayAccess(ASTNode):
    var_name: str
    index: ASTNode

@dataclass
class FuncDecl(ASTNode):
    return_type: str
    func_name: str
    params: List[VarDecl]
    body: 'Block'

@dataclass
class ReadStmt(ASTNode):
    var_name: str

@dataclass
class WriteStmt(ASTNode):
    expr: ASTNode

@dataclass
class GotoStmt(ASTNode):
    label: int

@dataclass
class LabelStmt(ASTNode):
    label: int

@dataclass
class Block(ASTNode):
    statements: List[ASTNode]

@dataclass
class IfStmt(ASTNode):
    condition: ASTNode
    then_branch: Block
    else_branch: Optional[Block]

@dataclass
class WhileStmt(ASTNode):
    condition: ASTNode
    body: Block

@dataclass
class ReturnStmt(ASTNode):
    value: Optional[ASTNode]

@dataclass
class ExprStmt(ASTNode):
    expr: ASTNode

@dataclass
class Assign(ASTNode):
    target: str
    value: ASTNode

@dataclass
class UnaryOp(ASTNode):
    op: str
    operand: ASTNode

@dataclass
class BinOp(ASTNode):
    op: str
    left: ASTNode
    right: ASTNode

@dataclass
class FuncCall(ASTNode):
    func_name: str
    args: List[ASTNode]

@dataclass
class Id(ASTNode):
    name: str

@dataclass
class Number(ASTNode):
    value: int

@dataclass
class Char_Literal(ASTNode):
    value: str

@dataclass
class String_Literal(ASTNode):
    value: str
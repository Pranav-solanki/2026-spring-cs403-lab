from sly import Lexer

# noqa: F821
class MiniCLexer(Lexer):
    # Set of token names
    tokens = {
        # Keywords
        IF, ELSE, WHILE, RETURN, GOTO, INT, CHAR, VOID, READ, WRITE, INCLUDE,
        
        # Identifiers & Literals
        ID, NUMBER, CHAR_LITERAL, STRING_LITERAL,
        
        # Operators
        PLUS, MINUS, TIMES, DIVIDE, MOD,
        ASSIGN, EQ, NE, LT, GT, LE, GE,
        AND, OR, NOT,
        
        # Delimiters
        LPAREN, RPAREN, LBRACE, RBRACE, 
        LBRACKET, RBRACKET, SEMI, COMMA, COLON,

        # Decorators
        AT, HASH
    }

    # --- Special Handling ---

    @_(r'\#\s*include\s*[<][^>\n]+[>]')
    def INCLUDE(self, t):
        start = t.value.find('<') + 1
        end = t.value.find('>')
        t.value = t.value[start:end].strip()
        return t

    # Ignored characters (whitespace)
    ignore = ' \t'

    # Line number tracking
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)

    # Comments (C-style /* ... */)
    @_(r'/\*[\s\S]*?\*/')
    def ignore_multiline_comment(self, t):
        self.lineno += t.value.count('\n')

    # Comments (C++ style //)
    @_(r'//.*')
    def ignore_single_line_comment(self, t):
        pass

    # --- Regular Expressions for Tokens ---

    # Delimiters
    LPAREN    = r'\('
    RPAREN    = r'\)'
    LBRACE    = r'\{'
    RBRACE    = r'\}'
    LBRACKET  = r'\['
    RBRACKET  = r'\]'
    SEMI      = r';'
    COMMA     = r','
    COLON     = r':'

    # Decorators
    AT        = r'@'
    HASH      = r'\#'

    # Operators
    PLUS      = r'\+'
    MINUS     = r'-'
    TIMES     = r'\*'
    DIVIDE    = r'/'
    MOD       = r'%'
    EQ        = r'=='
    ASSIGN    = r'='
    NE        = r'!='
    LE        = r'<='
    LT        = r'<'
    GE        = r'>='
    GT        = r'>'
    AND       = r'&&'
    OR        = r'\|\|'
    NOT       = r'!'

    # Identifiers and Keywords
    # (Regex matches identifiers, then checks if they are special keywords)
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ID['if']     = IF
    ID['else']   = ELSE
    ID['while']  = WHILE
    ID['return'] = RETURN
    ID['goto']   = GOTO
    ID['int']    = INT
    ID['char']   = CHAR
    ID['void']   = VOID
    ID['read']   = READ
    ID['write']  = WRITE

    # Literals
    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value) # Convert string digits to python integer
        return t

    # Character literal (e.g. 'c')
    @_(r"'([^'\\\n]|(\\ .))'")
    def CHAR_LITERAL(self, t):
        return t

    # String literal (e.g. "Hello")
    @_(r'\"([^\\\n]|(\\.))*?\"')
    def STRING_LITERAL(self, t):
        return t

    # Error handling
    def error(self, t):
        print(f"Line {self.lineno}: Illegal character '{t.value[0]}'")
        self.index += 1
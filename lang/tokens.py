# keyword constants
# keywords
KW_PRINT = "print"
KW_VARIABLE = "="
KW_COMMENT = "#"
KEYWORDS = [KW_PRINT, KW_VARIABLE, KW_COMMENT]

# characters (mainly for identifying different pieces of data as seperate from others)
CH_LPAREN = "("
CH_RPAREN = ")"
CH_STRING = "'"
CHARACTERS = [CH_LPAREN, CH_RPAREN, CH_STRING]

# mathematical operations (for math I think)
MO_PLUS = "+"
MO_MINUS = "-"
MO_DIVISION = "/"
MO_MULTIPLICATION = "*"
MATH_OPS = "+-/*"

DIGITS = "1234567890"

# returns data in token form
class Token:
    def token(pretoken):
        return pretoken
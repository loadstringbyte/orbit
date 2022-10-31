from err import HandleException
from tokens import Token
import re

# CONSTANTS
KW_LPAREN = "LPAREN"
KW_RPAREN = "RPAREN"
KW_SEMICOLON = 'SCOL'
KW_DOUBLEQUOTE = "DBQUOTE"
KW_PRINT = "PRINT"
KW_EXPRESSION = "EXPRESSION"
NUMBERS = "1234567890"

# LEXER LOGIC
class Lexer:
	def __init__(self, line):
		self.line = line
	def generateToken(self):
		tokens = []
		for i in range(len(self.line)):
			character = self.line[i]
			if character == ";":
                		tokens.append(Token(KW_SEMICOLON))
			elif character in NUMBERS:
				tokens.append(Token(KW_INT, int(character)))
				tokens.append(Token(KW_MULTIPLICATION))
			elif character == "(":
				tokens.append(Token(KW_LPAREN))
			elif character == ")":
				tokens.append(Token(KW_RPAREN))
			elif self.line[i] == '"' and self.line[i-1] == '(':
				ret = []
				j = i+1
				ret.append(self.line[i])
				ret.append(self.line[j])
				while self.line[j] != '"' and self.line[i] == '"':
					j += 1
					ret.append(self.line[j])
				ret.pop(0)
				ret.pop(-1)
				tokens.append(Token("".join(ret)))
				ret.clear()
			elif self.line[i] == 'p':
				if self.line[i + 1] == 'r':
					if self.line[i + 2] == "i":
						if self.line[i + 3] == "n":
							if self.line[i + 4] == "t":
								tokens.append(Token(KW_PRINT))
		return tokens, None

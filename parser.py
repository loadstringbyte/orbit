from lexer import Lexer
import tokens
from err import HandleException

class Parser:
	def __init__(self, tokens_output):
		self.token_output = tokens_output

		# statements
		
	def parse(self):
		i = 1
		garbage = []
		while i < len(self.token_output):
			if self.token_output[i-1] != tokens.Token("PRINT"):
				garbage.append(self.token_output[i])
				i += 1
		garbage.pop(0)
		garbage.pop(-1)
		res = str(garbage)[1:-1]
		print(res)

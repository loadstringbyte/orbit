from lexer import Token, Lexer
from parser import Parser

while True:
	userInput = input("orbit > ")

	l = Lexer(userInput)
	tokens, err = l.generateToken()

	if err != None:
		print("Syntax Error")

	p = Parser(tokens)
	p.parse()

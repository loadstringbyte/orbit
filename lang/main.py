from parse import *
from lexer import *

while True:
    inp = input("language >> ")
    if inp == "q": break;
    print(Parser(Lexer(inp).lex()).parsify())
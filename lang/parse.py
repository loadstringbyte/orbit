# importing * doesn't is okay in this situation because local libraries only have required funcs/vars declared
# that are distinct from eachother - does not pollute namespace
from lexer import *
from tokens import *
from data.store import *
from logging import log

# parser code
class Parser:
    def __init__(self, lexed):
        self.lexed = lexed
    
    # parses everything and runs everything basically
    def parsify(self):
        for idx, data in enumerate(self.lexed):
            
            # parsing mathematical operations
            if data in MATH_OPS:
                if data == '+': 
                    return int(self.lexed[idx-1])+int(self.lexed[idx+1])
                
                if data == '-' : 
                    return int(self.lexed[idx-1])-int(self.lexed[idx+1])
                
                if data == '*': 
                    return int(self.lexed[idx-1])*int(self.lexed[idx+1])
                
                if data == '/': 
                    return int(self.lexed[idx-1])/int(self.lexed[idx+1])
                
            # parsing print statement
            if data == KW_PRINT and self.lexed[idx+1] == '(' and self.lexed[idx+3] == ')':
                if self.lexed[2][0] == '"' and self.lexed[2][-1] == '"':
                    return self.lexed[2]
                
                return variables[str(self.lexed[2]).strip()]
            
            # parsing variable declaration
            if self.lexed[1] == KW_VARIABLE:
                DeclareVariable(self.lexed[0].strip(), self.lexed[2].strip())
                
        # print(variables)
                
        # print(self.lexed) # -> debugging purposes
    
# print(Parser(Lexer("hello_var = hello world").lex()).parsify())
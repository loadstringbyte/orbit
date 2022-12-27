from tokens import *

# tokenize the entire string
class Lexer:
    def __init__(self, plaintext: str):
        self.plaintext = plaintext
        
    def lex(self):
        tokenized = []
        for idx, data in enumerate(self.plaintext):
            
            # mathematical operations
            if data == MO_PLUS:
                self.plaintext += " "
                tokenized.append(Token.token(self.plaintext[0:idx-1]))
                tokenized.append(Token.token(MO_PLUS))
                tokenized.append(Token.token(self.plaintext[idx+1:-1]))
                
            if data == MO_DIVISION:
                self.plaintext += " "
                tokenized.append(Token.token(self.plaintext[0:idx-1]))
                tokenized.append(Token.token(MO_DIVISION))
                tokenized.append(Token.token(self.plaintext[idx+1:-1]))
                
            if data == MO_MULTIPLICATION:
                self.plaintext += " "
                tokenized.append(Token.token(self.plaintext[0:idx-1]))
                tokenized.append(Token.token(MO_MULTIPLICATION))
                tokenized.append(Token.token(self.plaintext[idx+1:-1]))
                
            if data == MO_MINUS:
                self.plaintext += " "
                tokenized.append(Token.token(self.plaintext[0:idx-1]))
                tokenized.append(Token.token(MO_MINUS))
                tokenized.append(Token.token(self.plaintext[idx+1:-1]))
            
            
            # lexing variable declairation
            if data == KW_VARIABLE:
                self.plaintext += " "
                tokenized.append(Token.token(self.plaintext[0:idx-1]))
                tokenized.append(Token.token(KW_VARIABLE))
                tokenized.append(Token.token(self.plaintext[idx+1:-1]))
            
            
            # printing and reading characters
            if self.plaintext[idx:idx+5] == KW_PRINT:
                tokenized.append(Token.token(KW_PRINT))
                
            if data == CH_LPAREN:
                tokenized.append(Token.token(CH_LPAREN))
                tokenized.append(self.plaintext.split("print(").pop(-1).replace(")", ''))
                
                tokenized.append(Token.token(CH_RPAREN))
            
            
        return tokenized
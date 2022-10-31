class HandleException:
    def __init__(self, error_name):
        self.error_name = error_name
    def generateError(self):
        if self.error_name == "ParsingError":
            return "Parsing Error"

        elif self.error_name == "LexicalAnalysisError":
            return "Lexical Analysis Error"

        elif self.error_name == "SyntaxError":
            return "Syntax Error"
        else:
            return "Error which has an unknown problem"
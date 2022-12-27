# stores data in memory

variables = {}

def DeclareVariable(var_kw, var_data):
    variables[var_kw] = var_data

def DestroyVariable(var_kw):
    del variables[var_kw]
    
from LinkStack import *

Bracket:dict = {")":"(","]":"[","}":"{"}
def Match_Bracket(data:str):
    global Bracket
    Stack:LinKStack = LinKStack()
    for i in data:
        if not Stack and i in list(Bracket.keys()):
            return False
        if i in list(Bracket.values()):
            Stack.L_push(i)
        elif Bracket[i] == Stack.return_top():
            Stack.L_pop()
        elif Bracket[i] != Stack.return_top():
            return False
    return True

print(Match_Bracket('({}{}{}[{}])'))
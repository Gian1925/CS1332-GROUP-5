from lexer import tokenize
from parser import Parser
from evaluator import Evaluator

code = """
HAI
I HAS A x ITZ 5
VISIBLE x
VISIBLE "HELLO"
VISIBLE SUM OF 3 AN 4
KTHXBYE
"""

# Tokenize the LOLCODE
tokens = tokenize(code)

# Parse the tokens into an AST
parser = Parser(tokens)
ast = parser.parse_program()

# Evaluate the AST
evaluator = Evaluator()
output = evaluator.eval(ast)

print("\nOutput:")
for result in output:
    print(result)

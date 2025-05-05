import re
import sys

# List of (pattern,                        token_type)
TOKEN_SPEC = [
    # Comments (ignored)
    (r'\s*BTW.*',                          None),
    (r'\s*OBTW.*',                         None),  # Optional: add multiline support later

    # **Program start/end:** `HAI`, `KTHXBYE`
    (r'\s*HAI\s+',                         'Code Delimiter'),
    (r'\s*KTHXBYE\s+',                     'Code Delimiter'),

    # **Variable declaration:** `I HAS A var`, optionally with `ITZ <value>`
    # **Assignment:** `var R <value or expression>`
    (r'\s*I HAS A\s+',                     'Variable Declaration'),
    (r'\s*ITZ\s+',                         'Variable Assignment'),
    (r'\s*R\s+',                           'Variable Assignment'),

    # **Input/Output:** `VISIBLE`, `GIMMEH`
    (r'\s*VISIBLE\s+',                     'Output Keyword'),
    (r'\s*GIMMEH\s+',                      'Input Keyword'),

    # **Arithmetic operations:** `SUM OF`, `DIFF OF`, `PRODUKT OF`, `QUOSHUNT OF`, `MOD OF`, `BIGGR OF`, `SMALLR OF`
    (r'\s*SUM OF\s+',                      'Arithmetic Operation'),
    (r'\s*DIFF OF\s+',                     'Arithmetic Operation'),
    (r'\s*PRODUKT OF\s+',                  'Arithmetic Operation'),
    (r'\s*QUOSHUNT OF\s+',                 'Arithmetic Operation'),
    (r'\s*MOD OF\s+',                      'Arithmetic Operation'),
    (r'\s*BIGGR OF\s+',                    'Arithmetic Operation'),
    (r'\s*SMALLR OF\s+',                   'Arithmetic Operation'),

    # **Logical operations:** `BOTH SAEM`, `DIFFRINT`, `NOT`, `BOTH OF`, `EITHER OF`
    (r'\s*BOTH SAEM\s+',                   'Logical Operation'),
    (r'\s*DIFFRINT\s+',                    'Logical Operation'),
    (r'\s*NOT\s+',                         'Logical Operation'),
    (r'\s*BOTH OF\s+',                     'Logical Operation'),
    (r'\s*EITHER OF\s+',                   'Logical Operation'),

    # AN separator
    (r'\s*AN\s+',                          'Operand Separator'),

    # **Conditional execution:** `O RLY?`, `YA RLY`, `NO WAI`, `OIC`
    (r'\s*O RLY\?\s*',                     'Conditional execution'),
    (r'\s*YA RLY\s*',                      'Conditional execution'),
    (r'\s*NO WAI\s*',                      'Conditional execution'),
    (r'\s*OIC\s*',                         'Conditional execution'),

    # **Data types:** NUMBR (integer), NUMBAR (float), YARN (string), TROOF (boolean)
    (r'\s*(NUMBR|NUMBAR|YARN|TROOF)\s*',   'Type Literal'),
    (r'\s*(WIN|FAIL)\s*',                  'TROOF Literal'), #Boolean 
    (r'\s*-?(0|[1-9][0-9]*)\.[0-9]+\s*',   'NUMBAR Literal'),
    (r'\s*-?(0|[1-9][0-9]*)\s*',           'NUMBR Literal'),
    (r'\s*\"[^\"]*\"\s*',                  'YARN Literal'),

    # Identifiers
    (r'\s*[a-zA-Z][a-zA-Z0-9_]*\s*',       'Identifier'),

    # Catch any remaining non-whitespace
    (r'\s*\S+',                            'Special Characters')
]

# Compile patterns into one regex
token_re = re.compile("|".join(f"(?P<TOK{i}>{pattern})" for i, (pattern, _) in enumerate(TOKEN_SPEC)))

def tokenize(code):
    tokens = []
    for match in token_re.finditer(code):
        for i, (_, tag) in enumerate(TOKEN_SPEC):
            if match.lastgroup == f"TOK{i}":
                if tag:  # ignore None (e.g., comments/whitespace)
                    value = match.group().strip()
                    tokens.append((tag, value))
                break
    return tokens

with open('lexer_test.lol', 'r') as f:
    code = f.read()
print(tokenize(code))

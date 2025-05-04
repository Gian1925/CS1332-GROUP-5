class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return (None, None)

    def consume(self, expected_type=None):
        if self.pos >= len(self.tokens):
            raise SyntaxError("Unexpected end of input")

        token = self.tokens[self.pos]

        if expected_type and token[0] != expected_type:
            raise SyntaxError(f"Expected {expected_type}, got {token[0]}")

        self.pos += 1
        return token

    def parse_program(self):
        program = []
        while self.pos < len(self.tokens):
            tok_type, tok_val = self.peek()
            if tok_type == 'Code Delimiter':
                self.consume()
            else:
                stmt = self.parse_statement()
                program.append(stmt)
        return program

    def parse_statement(self):
        tok_type, tok_val = self.peek()

        if tok_type == 'Variable Declaration':
            return self.parse_var_declaration()
        elif tok_type == 'Output Keyword':
            return self.parse_output()
        elif tok_type == 'Arithmetic Operation':
            return self.parse_arithmetic()
        else:
            raise SyntaxError(f"Unknown statement: {tok_val}")

    def parse_var_declaration(self):
        self.consume('Variable Declaration')  # I HAS A
        var_name = self.consume('Identifier')[1]

        next_type, _ = self.peek()
        if next_type == 'Variable Assignment':  # ITZ
            self.consume('Variable Assignment')
            value_token = self.consume()
            return {'type': 'var_decl', 'name': var_name, 'value': value_token[1]}
        else:
            return {'type': 'var_decl', 'name': var_name, 'value': None}

    def parse_output(self):
        self.consume('Output Keyword')  # VISIBLE
        next_type, _ = self.peek()

        if next_type == 'Arithmetic Operation':
            expr = self.parse_arithmetic()
            return {'type': 'output', 'value': expr}
        else:
            value = self.consume()
            return {'type': 'output', 'value': value[1]}

    def parse_arithmetic(self):
        op_token = self.consume('Arithmetic Operation')  # e.g., SUM OF
        left = self.consume()  # NUMBR or Identifier
        self.consume('Operand Separator')  # AN
        right = self.consume()  # NUMBR or Identifier

        return {
            'type': 'arithmetic',
            'op': op_token[1],
            'left': left[1],
            'right': right[1]
        }

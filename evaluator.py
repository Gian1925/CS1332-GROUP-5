class Evaluator:
    def __init__(self):
        self.variables = {}  # Dictionary to store variables

    def eval(self, ast):
        results = []
        for node in ast:
            if node['type'] == 'var_decl':
                results.append(self.eval_var_decl(node))
            elif node['type'] == 'output':
                results.append(self.eval_output(node))
            elif node['type'] == 'arithmetic':
                results.append(self.eval_arithmetic(node))
        return results

    def eval_var_decl(self, node):
        var_name = node['name']
        value = node['value']
        if value is None:
            self.variables[var_name] = None
        else:
            self.variables[var_name] = value
        return f"Variable {var_name} declared with value {value}"

    def eval_output(self, node):
        value = node['value']
        if isinstance(value, dict) and value['type'] == 'arithmetic':
            return self.eval_arithmetic(value)
        elif value.startswith('"') and value.endswith('"'):  # String literal
            return value.strip('"')
        else:  # Variable or literal
            return self.variables.get(value, value)

    def eval_arithmetic(self, node):
        op = node['op']
        left = self.get_value(node['left'])
        right = self.get_value(node['right'])

        if op == 'SUM OF':
            return left + right
        elif op == 'DIFF OF':
            return left - right
        elif op == 'PRODUKT OF':
            return left * right
        elif op == 'QUOSHUNT OF':
            return left / right
        elif op == 'MOD OF':
            return left % right
        elif op == 'BIGGR OF':
            return max(left, right)
        elif op == 'SMALLR OF':
            return min(left, right)

    def get_value(self, value):
        if value.isdigit():  # Numeric literal
            return int(value)
        elif value.replace('.', '', 1).isdigit():  # Floating-point number
            return float(value)
        elif value in self.variables:  # Variable
            return self.variables.get(value)
        else:
            return value  # For now, if it's not a number or variable, just return it

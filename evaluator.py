class Evaluator:
    def __init__(self):
        self.variables = {}
        self.input_buffer = []
#Dictionary to store variables
    def eval(self, ast):
        results = []
        skip_block = False
        inside_conditional = False
        
        for node in ast:
            if skip_block:
                if node['type'] == 'conditional_end':
                    skip_block = False
                continue
            
            if node['type'] == 'var_decl':
                results.append(self.eval_var_decl(node))
                
            elif node['type'] == 'output':
                results.append(self.eval_output(node))
                
            elif node['type'] == 'input':
                results.append(self.eval_input(node))
                
            elif node['type'] == 'arithmetic':
                results.append(self.eval_arithmetic(node))
                
            elif node['type'] == 'conditional_start':
                inside_conditional = True
                condition = self.get_value(node['condition'])
                skip_block = not (condition == "WIN" or condition is True)

            elif node['type'] == 'else':
                skip_block = not skip_block  # Switch execution block

            elif node['type'] == 'conditional_end':
                inside_conditional = False
                skip_block = False  
                
        return results
    
    def eval_var_decl(self, node):
        var_name = node ['name']
        value = node ['value']
        if value is None:
            self.variables[var_name] = None
        else:
            self.variables[var_name] = self.get_value(value)
        return f"Variable {var_name} declared with value {self.variables[var_name]}"
    
    def eval_output(self,node):
        value = node['value']
        if isinstance(value, dict) and value['type'] == 'arithmetic':
            return self.eval_arithmetic(value)
        elif value.startswith('"') and value.endswith('"'): #String literal
            return value.strip('"')
        else: #Variable or literal
            return self.variables.get(value, value)
        
    def eval_input(self, node):
        var_name = node['var']
        user_input = input(f"GIMMEH {var_name}: ")
        self.variables[var_name] = user_input
        return f"Input received for {var_name}: {user_input}"
    
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
        elif op == 'BIGGR OF':
            return max(left, right)
        elif op == 'SMALLR OF':
            return min(left, right)
    
    def get_value(self, value):
        if isinstance(value, (int, float)):
            return value
        if isinstance(value, str):
            if value.isdigit(): #Numeric literal
                return int(value)
            elif value.replace('.', '', 1).isdigit(): #Floating point number
                return float(value)
            elif value in self.variables: #Variables
                return self.variables.get(value)
            elif value in ["WIN", "FAIL"]:
                return value == "WIN"
        else:
            return value

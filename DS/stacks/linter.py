import stack

class Linter:
    def __init__(self):
        # I imported and used the already build Stack as a module
        self.stack = stack.Stack()
    
    def lint(self, text):
        for char in text:
            if self.is_opening_brace(char):
                self.stack.push(char)
                
            elif self.is_closing_brace(char):
                popped_opening_brace = self.stack.pop()
                
                if not popped_opening_brace:
                    return f"#{char} doesn't have an opening brace "
                
                if self.is_not_a_match(popped_opening_brace, char):
                    return f"#{char} has mismatched opening brace "
            
        if self.stack.last():
            return f"#{self.stack.last()} does not have closing braces" 
        return True       
    
    def is_opening_brace(self, char):
        return (char in ["(", "[", "{"])
    
    def is_closing_brace(self, char):
        return (char in [")", "]", "}"])
    
    def is_not_a_match(self, opening_brace, closing_brace):
        tags = {'(': ')', '[': ']', '{':'}'}
        return tags[opening_brace] != closing_brace
        
                
linter = Linter()
x = "{(['hello'])}"

print(linter.lint(x))

import stack

class Linter:
    def __init__(self):
        # I imported and used the already build Stack as a module
        self.stack = stack.Stack()
    
    def lint(self, text):
        for char in text:
            if self.is_opening_brace(char):
                self.stack.push(char)
                self.count += 1
            elif self.is_closing_brace(char):
                if not self.stack:
                    return f"#{char} doesn't have an opening brace "
                popped_opening_brace = self.stack.pop()
            
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
x = "()([]({}[]){}){}{()}[]{}[]()(()([[]]()))()()()[]()(){{}}()({[{}][]}[[{{}({({({})})})}]]]"

print(linter.lint(x))

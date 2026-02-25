from task1 import Stack

def check_balance(string: str) -> str:
    string_stack = Stack()
    for s in string:
        if s in (")", "]", "}") and string_stack.is_empty():
            return "Несбалансированно" 

        if s in ("(", "[", "{"):
            string_stack.push(s)
            continue
        
        last_element = string_stack.pop()

        round_check  = True if s==")" and last_element == "(" else False
        figure_check = True if s=="}" and last_element == "{" else False
        rect_check   = True if s=="]" and last_element == "[" else False

        is_balanced = round_check or figure_check or rect_check

        if not is_balanced:
            return "Несбалансированно" 
        
    if string_stack.is_empty():
        return "Сбалансированно"
    else:
        return "Несбалансированно" 
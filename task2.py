from task1 import Stack

def check_balance(string: str) -> str:
    stack = Stack()
    pairs = {")": "(", "]":'[', "}":"{"}

    for ch in string:
        if ch in "([{":
            stack.push(ch)
        elif ch in ")]}":
            if stack.is_empty():
                return "Несбалансированно"
            if stack.pop() != pairs[ch]:
                return "Несбалансированно"
        else:
            continue
    return "Сбалансированно" if stack.is_empty else "Несбалансированно"
from stack.array_stack import ArrayStack

def main():
    int_stack = ArrayStack()
    int_stack.push(10)
    int_stack.push(20)
    print("Вершина (int):", int_stack.top())

    str_stack = ArrayStack()
    str_stack.push("Python")
    str_stack.push("Stack")
    print("Вершина (str):", str_stack.top())

    print("Разворот строки через стек:")
    word = "hello"
    stack = ArrayStack()
    for char in word:
        stack.push(char)
    reversed_word = ""
    while not stack.empty():
        reversed_word += stack.top()
        stack.pop()
    print(f"'{word}' → '{reversed_word}'")

if __name__ == "__main__":
    main()
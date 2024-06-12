'''
tried code

def camelCase():
    if camel.isupper()
    else camel

def main():
    camel = str(input("camelcase: "))
    print("snake_case: ",snake_case)

main()

def camelCase(camel):
    snake = ''.join([char.lower() if char.isupper() else char for char in camel])
    return snake

def main():
    camel = input("camelCase: ")
    snake_case = camelCase(camel)
    print("snake_case:", snake_case)

if __name__ == '__main__':
    main()

def camelCase(camel):
    snake = ''.join(char[0].lower() if char[1:].isupper() else char for char in camel)
    return snake[0].lower() + snake[1].lower()

def main():
    camel = input("camelCase: ")
    snake_case = camelCase(camel)
    print("snake_case:", snake_case)

if __name__ == '__main__':
    main()

'''
def camelCase(camel):
    snake = ""
    for i, char in enumerate(camel):
        if char.isupper():
            snake += "_" + char.lower()
        else:
            snake += char
    return snake

def main():
    camel = input("camelCase: ")
    snake_case = camelCase(camel)
    print("snake_case:", snake_case)

if __name__ == '__main__':
    main()
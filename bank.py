'''
Prompt the user for a greeting
if greeting == "hello":
    print out $0
elife greeting = "h":
    out put $20
else:
    output $100

    ignore any whitespaces in the user`s greeting
    case-insensitive

'''
#========================={ FIRST ASGNT }=========================
'''
greet = str(input("Greeting: ")).lower()

if "hello" in greet:
    print("$0")
elif "h" in greet[0]:
    print("$20")
else:
    print('$100')

'''

def value(greeting):
    if "hello" in greeting.lower():
        return 0
    elif greeting.lower().startswith("h"):
        return 20
    else:
        return 100

def main():
    greeting = input("Enter a greeting: ")
    result = value(greeting)
    print("Result:", result)

if __name__ == "__main__":
    main()
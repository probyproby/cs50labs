"""
The system should keep asking until the user enter a wrong answer
while True:
    print the question
    if ans == 42 | forty-two | forty two (case insensitive):
        print yes to approve the answer
    else:
        print wrong to disprove the answer
"""
### if the code is left in the manner below it will take any
### any int or str and read it as true so we have to reverse the condition
### and compare each value or str to make it work
'''
while True:
   ans = input("What is the answer to the Great question of life, the Universe, and Everything? ")

    if ans == "42" or Forty-two.lower() or forty two.lower():
        print("Yes")
    else:
        break
'''
### if condition reversed it ends programs on the first line
'''
while True:
    ans = input("What is the answer to the Great question of life, the Universe, and Everything? ")

    if ans != "42" and ans != "Forty-two".lower() and ans != "forty two".lower():
        break
    else:
        print("Yes")
'''
'''
### individually comparing the answers
while True:
    ans = str(input("What is the answer to the Great question of life, the Universe, and Everything? ")).lower()

    if ans == "42":
        print("Yes")
    elif ans == "Forty-two":
        print("Yes")
    elif ans == "forty two":
        print("Yes")
    else:
        print("No")
'''
while True:
    ans = input("What is the answer to the Great question of life, the Universe, and Everything? ").lower()
    if ans == "Forty-two" or ans == "42" or ans == "forty two":
        print("Yes")
    else:
        print("No")
    break
'''
import sys
def adieu(n):
    len(name)
    for _ in range(name):
        farewell_names = names[:_]
        if _ == 1:
            farewell = farewell_name[0]
        elif _ == 2:
            farewell = ''.join(farewell_name[:-1]) + and f'{farewell_name[1]}'
            print(f'Adieu, adieu, to {farewell}')

def mai():
    if len(sys.argv) >= 1:
        n = sys.arg[1:]
    else:
        print("Enter names:")
        names = [name.strip() for name in sys.stdin.readlines()]
main()
'''
import sys

def bid_adieu(names):
    num_names = len(names)
    for i in range(1, num_names + 1):
        farewell_names = names[:i]
        if i == 1:
            farewell_text = farewell_names[0]
        elif i == 2:
            farewell_text = " and ".join(farewell_names)
        else:
            farewell_text = ", ".join(farewell_names[:-1]) + f", and {farewell_names[-1]}"
        print(f"Adieu, adieu, to {farewell_text}")

def main():
    if len(sys.argv) > 1:
        names = sys.argv[1:]
    else:
        print("Enter names:")
        names = [name.strip() for name in sys.stdin.readlines()]

    bid_adieu(names)

if __name__ == "__main__":
    main()
"""
define our main function:
    input(mass)
    call for engergy

define energy(mass):
    e = (m*(300million**2))
    return e

    print(M: = and E: =)

close the main func
"""

def main():
    mass = int(input("M: "))
    E = energy(mass)
    print("E: ",E)

def energy(mass):
    c = 300000000**2
    E = mass * c
    return E

main()
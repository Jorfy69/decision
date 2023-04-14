import random

def main():
    a = input('What is choice 1?')
    b = input('What is choice 2?')
    c = input('What is choice 3?')
    RAND = random.randint(1, 3)
    if RAND == 1:
        print(f'Choice {a} wins!')
    elif RAND == 2:
        print(f'Choice {b} wins!')
    else:
        print(f'Choice {c} wins!')   

if __name__ == '__main__':
    main()

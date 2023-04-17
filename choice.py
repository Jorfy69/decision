import random
def options(rand_highest_value):
    RAND = random.randint(1,int(rand_highest_value))
    a = input('What choices would you like?(Max 5)\n[Please list them all out with one space pls]\nAwnser(s) = ')
    choices = [a]
    if RAND == 1:
        print(f'This choice wins: {choices[0]}')
    elif RAND ==2:
        print(f'This choice wins: {choices[1]}')
    elif RAND == 3:
        print(f'This choice wins: {choices[2]}')
    elif RAND ==4:
        print(f'This choice wins: {choices[3]}')
    elif RAND == 5:
        print(f'This choice wins: {choices[4]}') 
    else:
        print('To many or not enough chocies') 
    

def main():
   choice_selector = input("What number of options would you like? :: ")
   options(choice_selector)
        

if __name__ == '__main__':
    main()

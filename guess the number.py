from random import randint
y=randint(1,100)
x=input("""You have 5 attempts. 
            Guess a number between 1 and 100: """)
count=1
while x!=y:
    print("Wrong guess, try again")
    x=input(f"""You have {5-count} attempts left. 
            Guess a number between 1 and 100: """)
    if count>=4:
        print("You have exceeded the maximum number of attempts. The correct number was", y)
        break
    count+=1
    
if x==y:    
    print("Congratulations! You guessed it right.")
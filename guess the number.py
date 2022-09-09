import random

def guess(guess_limit):
  
    random_number=random.randint(0,guess_limit)
    guess = None
   
    while guess !=random_number:
        # make sure that the entrance is an integer
        try:
            guess = input(f"guess a number between 0 and {guess_limit}:")
            guess = int(guess)
        except:
            print(f"{guess} is not an integer")
            exit()

      
        if guess<random_number:
           print("guess again...too low")
        elif guess>random_number:
           print("guess again...too high")
        else:
            print(f"Yeah,that is right , the random number is :{random_number}  hats off to you")
            break

guess(5)

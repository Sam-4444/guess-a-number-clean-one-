import random
# define a method
def guess(z):
    # assign a random number between 0 and z to random_number
    random_number=random.randint(0,z)
    guess = None
    # make a loop
    while guess !=random_number:
        # make sure that the entrance is an integer
        try:
            guess = input(f"guess a number between 0 and {z}:")
            guess = int(guess)
        except:
            print(f"{guess} is not an integer")
            exit()

        # conditions
        if guess<random_number:
           print("guess again...too low")
        elif guess>random_number:
           print("guess again...too high")
        else:
            print(f"Yeah,that is right , the random number is :{random_number}  hats off to you")
            break

# recall the method
guess(5)
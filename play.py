import random

def play():

    """
    Program to Play Games in different Difficulty Modes. Using Function Difficulty
    """
    print("######### SELECT DIFFICULTY: Use Numbers 1, 2, 3 to choose game Level #######")
    game_level = int(input("Easy: Enter 1, Medium: Enter 2, Hard: Enter 3 "))
    if game_level == 1:
        difficulty(user_guess_trail = 6, max_rand_number = 10)
    elif game_level == 2:
        difficulty(user_guess_trail = 4, max_rand_number = 20)
    else:
        difficulty(user_guess_trail = 3, max_rand_number = 50)



  
def difficulty(user_guess_trail, max_rand_number):
    """
    Sub Routine for Play
    Inputs:
        user_guess_trail ----> Number of time a user can guess
        max_rand_number ------> Maximum random number in the range 1 to Max_rand
    Outputs:
        Prints End Messages
    """
    
    random_num = random.randint(1, max_rand_number)
    print("Hint for Developer: The Correct Number = " + str(random_num)) ##Delete this line
    
    
    
    print("Start You have "+ str(user_guess_trail)+ " guesses total")
    trail_state = 0   # Number of guess remaining

    for i in range(1, (user_guess_trail+1)):

        if trail_state < user_guess_trail:
    
            user_guess = int(input("Enter a random guess!! "))
        
            if user_guess ==  random_num:
                print("Correct Guess You Win!!")
                break;
            else:
                trail_state += 1
                if trail_state < user_guess_trail:
                    print("Wrong Guess!!! please try again, You have " + str(user_guess_trail - trail_state) + " guesses remaining" + "\n")
                else:
                    print("Sorry!! Number of trails exceeded")
                    break;
                
    

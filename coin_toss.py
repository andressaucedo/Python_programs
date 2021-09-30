# coin_toss.py - an introduction into the random module 
def heads_or_tails():
    import random
    heads = 1
    tails = 2
    
    while(1):
        toss = random.randint(heads, tails)
 
        try:
            choice = int(input("Let's do a coin toss, you choose (1 for heads, 2 for tails or 3 to quit): "))
        except ValueError:
            print("That's not a valid choice, try again.\n")
            continue
        except:
            print("Undefined error.\n")

        if choice == 3:
            print("Goodbye.\n")
            break
        elif choice > 3 or choice < 1:
            print("Just choose 1 or 2 please or 3 to quit\n")
            continue 
        elif choice == heads and toss == heads:
            print(f"You guessed heads and the outcome is heads, congratulations!\n")
        elif choice == tails and toss == tails:
            print(f"You guessed tails and the outcome is tails, congratulations!\n")
        else:
            if toss == 1:
                toss_str = "heads"
            elif toss == 2:
                toss_str = "tails"
            print(f"The outcome is {toss_str}, better luck next time.\n")

    pass

if __name__ == "__main__":
    heads_or_tails()
# tryme.py - sample program to illustrate try, except keywords used in a loop

def try_me():

    while(1):
        try:
            temperature = float(input("What do you think the temperature is today?  "))
            break
        except ValueError:
            print("That doesn't quite make sense, try again please.")
        except:
            print("Undefined error.")


    if temperature > 80:
        print("Jeez, that's pretty hot!")
    elif temperature < 50:
        print("Brrrr! That's freezing, can I borrow a jacket?")
    else:
        print("That doesn't sound too bad. Enjoy your day!")

    pass

if __name__ == "__main__":
    try_me()
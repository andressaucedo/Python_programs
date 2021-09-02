# loops.py - This program is a simple illustration of the syntax used in python
# for if-else statements, for loops and lists.
def loopy(friend):
  list = {
  "John","Jane","Diane","Bobby","Lottie","Jimmy"
  }

  print("I'm looking for my friend, what's your name?")
  for name in list:
    print(name)
    if name == friend:
      print(f"Hey, {name}! Good to see ya!" + "\n")
      break
    else:
      print("Nope. Nice to meet you though." + "\n")

if __name__ == "__main__":
  loopy("Diane")
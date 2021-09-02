# loops.py - This program is a simple illustration of the syntax used in python
# for if-else statements, for loops and sets.
def loopy(friend):
  set_folks = {
  "John","Jane","Diane","Bobby","Lottie","Jimmy"
  } 
# Curly brackets make this a set. Unlike lists or tuples, sets are 
# unordered. This means the set output order will vary.

  print("I'm looking for my friend, what's your name?")
  for name in set_folks:
    print(name)
    if name == friend:
      print(f"Hey, {name}! Good to see ya!" + "\n")
      break
    else:
      print("Nope. Nice to meet you though." + "\n")

if __name__ == "__main__":
  loopy("Diane")
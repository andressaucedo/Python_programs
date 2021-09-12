def slicer():
  print("Enter a few words, please: ",end=None)
  a_few_words = input()

  print("Enter a start value: ",end=None)
  start = int(input())
  
  print("Enter an end value: ",end=None)
  end = int(input())

  print("\nThis is your string: " + a_few_words)
  print("This is your sliced string: " + a_few_words[start:end])

if __name__ == "__main__":
  slicer()
def string_finder(): 
  x = 0
  user_string = input("Enter the text you want to search: \n")
  search_phrase = input("Enter your search phrase/word: ")
  nums = [None] * len(user_string)
  print()
  
  print(f"\t{user_string}")
  
  talk_location = user_string.find(search_phrase)
  string_position = 0
  print("\t", end = '')
  while talk_location != -1:
    for i in range(string_position,talk_location):
      print(" ", end = '')
    print("^", end = '')
    nums[x] = talk_location
    x += 1
    string_position = talk_location + 1
    talk_location = user_string.find(search_phrase, string_position)
  print()
  
  print("Locations of occurences: ", end = '')
  for i in range (0, len(nums)):
    if nums[i] != None: 
      print(nums[i], end = '')
      print(" ", end = '')
  print()

if __name__ == "__main__":
  string_finder()
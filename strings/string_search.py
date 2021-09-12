def searcher():

  song_list = ["hurt", "head like a hole","march of the pigs", "the becoming", "we're in this together", "dead souls"]
  flag = False

  while flag == False:  
    song_name = input("Enter the name of a NIN song to see if it's in this list: ")
  
    if song_name.lower() in song_list:
      print(f"\nYou got it! {song_name} is in the list.\n")
      flag = True  
    else: 
      print("\nSorry, that's a good one but it's not on the list. Try again\n")

if __name__ == "__main__":
  searcher()
# import.py- This is a Python program to illustrate how to read JSON files.
#            There should be a file named "import.json" in the same directory.

def json_importer(filename):
    import json # Load the JSON import module

    data_file = open(filename,)  # Opens the filename file

    converted_data = json.load(data_file)  # Returns the JSON data as a dict

    for i in converted_data:
        print(i)
        for j in converted_data[i]:  # Iterating through our dict
            print(j)

    print(f"\nThe data type of 'converted_data' is :{type(converted_data)}")

    data_file.close()  # Close the data file to prevent memory errors.

if __name__ == "__main__":
    json_importer('import.json')
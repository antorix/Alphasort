# This script sorts all strings in the file input.txt alphabetically
# and puts them in the file output.txt.
try:
    with open("input.txt", "r") as file: # open file
        list_new = sorted([line.rstrip() for line in file]) # sort
except:
    input("No file found. Create file \"input.txt\" with strings to sort.")
else:    
    with open("output.txt", "w") as file_new:
        for i in list_new:
            print(i, end='\n', file=file_new) # print sorted strings one by one

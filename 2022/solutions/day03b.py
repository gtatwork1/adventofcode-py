# define a function to find the common alphabet
def find_common_alphabet(row1, row2, row3):
    # create a set with all the letters from row1
    s = set(row1)
    # use the intersection method to find the common letters in row2 and row3
    s = s.intersection(set(row2)).intersection(set(row3))
    # return the first (and only) letter from the set
    return list(s)[0]

# open the input file for reading
with open('in03.txt', 'r') as input_file:

    # Initialize the sum of the values
    sum = 0

    # read the file line by line
    for row1, row2, row3 in zip(input_file, input_file, input_file):
        # find the common alphabet
        common = find_common_alphabet(row1, row2, row3)
        # print the result
        print(f'The common alphabet is: {common}')
        
        # Calculate the value of the common letter
        if "a" <= common <= "z":
            value = ord(common) - ord("a") + 1
        elif "A" <= common <= "Z":
            value = ord(common) - ord("A") + 27
        else:
            value = 0
            
        print("Value for group:", value)
            
        # Add the value to the sum
        sum += value
    
# Output the sum
print("Sum of values:", sum)

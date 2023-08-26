# Given two strings ransomNote and magazine,
# return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.


from collections import Counter
ransomNote, magazine = "aab",  "baa"

rNote = Counter(ransomNote)

mag = Counter(magazine)
if rNote & mag == rNote:
    print(True)

# Create a dictionary to store character counts
dictionary = {}

# Iterate through the magazine and count characters
for char in magazine:
    if char not in dictionary:
        dictionary[char] = 1
    else:
        dictionary[char] += 1

# Iterate through the ransom note and check character counts
for char in ransomNote:
    if char in dictionary and dictionary[char] > 0:
        dictionary[char] -= 1
    else:
        print(False)

print(True)

# Approach
# Create a HashMap called dictionary to store the character counts in the magazine.
# Iterate through each character in the magazine string.
# If the character is not present in the dictionary, add it with a count of 1.
# If the character is already present, increment its count by 1.
# Iterate through each character in the ransom note string.
# Check if the character is present in the dictionary and its count is greater than 0.
# If both conditions are satisfied, decrement the count of the character in the dictionary.
# If a character is not present in the dictionary or its count is 0, return false.
# If all characters in the ransom note have been checked successfully, return true.

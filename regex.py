import re

text = "Testing regex with Kigula by Kigula"
pattern = r"Kigula"


## Find one occurence
match = re.search(pattern, text)
if match:
    print("Match Found: ", match.group())
else:
    print("No match found")

## Find all occurences
matches = re.findall(pattern, text)
print("")
print("All matches: ",matches)

## Substitution
replacement = "Jesse"
new_string = re.sub(pattern,replacement,text)
print("")
print("New String: ",new_string)

#Splitting Strings
split = r"[with]"
new_split = re.split(split, text)
print("")
print("Splitting Strings")
print(new_split)


#Matching Strings
text = "Testing regex with Kigula by Kigula"
pattern = r"Kigula"
match = re.match(pattern, text)
if match:
    print("")
    print("Match Strings")
    print(match.group())

text = "Hello World"
pattern = r"Hello"
match = re.match(pattern, text)
if match:
    print("Match found:", match.group())  # Output: Hello









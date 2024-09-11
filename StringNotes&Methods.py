# Python string methods

# Sample string to demonstrate methods
sample_string = "Hello, World!"

# capitalize() - Converts the first character to upper case
capitalized_string = sample_string.capitalize()
# "Hello, world!"
print("capitalize():", capitalized_string)

# lower() - Converts all characters to lower case
lowercase_string = sample_string.lower()
# "hello, world!"
print("lower():", lowercase_string)

# upper() - Converts all characters to upper case
uppercase_string = sample_string.upper()
# "HELLO, WORLD!"
print("upper():", uppercase_string)

# title() - Converts the first character of each word to upper case
title_string = sample_string.title()
# "Hello, World!"
print("title():", title_string)

# swapcase() - Swaps the case of each character
swapcase_string = sample_string.swapcase()
# "hELLO, wORLD!"
print("swapcase():", swapcase_string)

# isupper() - Returns True if all characters are upper case
print("isupper():", sample_string.isupper())  # False

# islower() - Returns True if all characters are lower case
print("islower():", sample_string.islower())  # False

# istitle() - Returns True if the string is in title case
print("istitle():", sample_string.istitle())  # True

# isalpha() - Returns True if all characters in the string are alphabetic
print("isalpha():", sample_string.isalpha())  # False (due to the comma and space)

# isdigit() - Returns True if all characters are digits
print("isdigit():", "12345".isdigit())  # True

# isalnum() - Returns True if all characters are alphanumeric (no spaces or symbols)
print("isalnum():", "Hello123".isalnum())  # True

# startswith() - Returns True if the string starts with the specified prefix
print("startswith():", sample_string.startswith("Hello"))  # True

# endswith() - Returns True if the string ends with the specified suffix
print("endswith():", sample_string.endswith("World!"))  # True

# find() - Returns the lowest index of the substring if found, otherwise -1
print("find():", sample_string.find("World"))  # 7

# rfind() - Returns the highest index of the substring if found, otherwise -1
print("rfind():", sample_string.rfind("o"))  # 8

# index() - Similar to find(), but raises a ValueError if the substring is not found
try:
    print("index():", sample_string.index("World"))  # 7
except ValueError:
    print("index(): Substring not found")

# count() - Returns the number of occurrences of a substring
print("count():", sample_string.count("l"))  # 3

# replace() - Replaces all occurrences of a substring with another substring
replaced_string = sample_string.replace("World", "Python")
# "Hello, Python!"
print("replace():", replaced_string)

# strip() - Removes leading and trailing whitespace
print("strip():", "   Hello, World!   ".strip())  # "Hello, World!"

# lstrip() - Removes leading (left) whitespace
print("lstrip():", "   Hello, World!   ".lstrip())  # "Hello, World!   "

# rstrip() - Removes trailing (right) whitespace
print("rstrip():", "   Hello, World!   ".rstrip())  # "   Hello, World!"

# split() - Splits the string into a list at each space (default) or specified delimiter
print("split():", sample_string.split())  # ['Hello,', 'World!']

# rsplit() - Splits the string into a list from the right
print("rsplit():", sample_string.rsplit(",", 1))  # ['Hello', ' World!']

# partition() - Splits the string into a tuple with three elements: 
# the part before the separator, the separator itself, and the part after the separator
print("partition():", sample_string.partition(", "))  # ('Hello', ', ', 'World!')

# join() - Joins elements of an iterable with the string as separator
print("join():", "-".join(["2024", "09", "11"]))  # "2024-09-11"

# zfill() - Pads the string on the left with zeros to fill the specified width
print("zfill():", "42".zfill(5))  # "00042"

# encode() - Encodes the string to a bytes object
print("encode():", sample_string.encode())  # b'Hello, World!'

# decode() - Decodes bytes back into a string
print("decode():", b'Hello, World!'.decode())  # "Hello, World!"

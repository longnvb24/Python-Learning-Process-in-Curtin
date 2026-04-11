#
# strings1.py: Read in a string and print it in reverse
#              using a loop and a method call

instring = input("Enter a string... ")

# *** add (2) upper and (3) duplicating code here
instring = instring.upper()
print("Your upper string is: ", instring)
print("Your duplicate string is: ", instring+instring)
instring = instring+instring
# print string with a while loop
print("Every second character in your string is: ", end='')
index = 0
while index < len(instring):
    print(instring[index], end='')
    index += 2
print()

# reversing with a for loop
print("Every second character in your string is: ", end='')
for i in range(0,len(instring),2):
    print(instring[i], end='')
print()

# reversing with slicing
print("Every second character in your string is:", instring[::2])


# print string with a while loop
print("Every second character excluding the first and last is: ", end='')
index = 1
while index < len(instring)-1:
    print(instring[index], end='')
    index += 2
print()

# print string with a for loop
print("Every second character excluding the first and last is: ", end='')
for i in range(1,len(instring)-1,2):
    print(instring[i], end='')
print()

# print with slicing
print("Every second character excluding the first and last is:", instring[1:len(instring)-1:2])


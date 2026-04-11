#
# bucket2.py - bucket list builder
#
print('\nBUCKET LIST BUILDER\n')
bucket = []
choice = input('Enter selection: e(X)it, (A)dd, (L)ist...')
while choice.upper() != "X":
    if choice == "A":
        print("Enter list item... ")
        newitem = input()
        bucket.append(newitem)
    elif choice == "L":
        for item in bucket:
            print(item)
    else:
        print("Invalid selection!")
    choice = input("Enter selection: e(X)it, (A)dd, (L)ist...")
print('\nGOODBYE!\n')

#
# vending.py - vending machine simulation
#
print("\nWelcome to the snack vending machine!\n")
print("The slots are loaded with delicious treats!")
response = input("\nWould you like a treat? (Y/N)...")
treats = [[1, "Choco Pie", 1.00, 5],
          [2, "Hello Panda", 0.50, 10],
          [3, "Fortune Cookie", 0.30, 10],
          [4, "Fig Roll", 0.30, 10],
          [5, "Maliban Orange Cream", 0.30, 10],
          [6, "Maliban Custard Cream", 0.30, 10],
          [7, "Maliban Chocolate Cream", 0.30, 10],
          [8, "Eccles Cake", 0.80, 5],
          [9, "Wagon Wheel", 1.50, 1]]
while response.upper() != "N":
    print("Which treat would you like!\n")
	print("+" + "-"*47 + "+")
	print("|  # | Name"+ " "*21 + "| Price | Count |")
	print("+" + "-"*47 + "+")
	for i in range(len(treats)):
		print(f"|  {treats[i][0]} | {treats[i][1]}{(25-len(treats[i][1]))*' '}| ${treats[i][2]:.2f} |{(6-len(str(treats[i][3])))*' '}{treats[i][3]} |")  
	print("+" + "-"*47 + "+")
    selection = int(input("\nEnter your selection:"))
    if treats[selection-1][3] <= 0:
		print("Oh dear! We are all out of treats[selection][1]")
	else:
		print(f"That will be: ${treats[selection-1][2]:.2f}")
		print("\nEnjoy your treat!\n")
		treats[selection-1][3] -= 1
	response = input("Would you like a treat (Y/N)...")
print("Glad to be of service!")

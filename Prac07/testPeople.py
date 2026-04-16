from people import Address, Person, Staff

print('#### People Test Program ###')
testAdd = Address('10', 'Downing St', 'Carlisle', '6101') 
testPerson = Person('Winston Churchill', '30/11/1874', testAdd) 
testPerson.displayPerson()
print()
testAdd2 = Address('1', 'Infinite Loop', 'Hillarys', '6025')
testPerson2 = Staff('Professor Awesome', '1/6/61', testAdd2, '12345J') 
testPerson2.displayPerson()
print()
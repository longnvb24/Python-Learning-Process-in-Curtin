from people import *

print('#### People Test Program ###')
testAdd = Address('10', 'Downing St', 'Carlisle', '6101') 
testPerson = Person('Winston Churchill', '30/11/1874', testAdd) 
testPerson.displayPerson()
print()

testAdd2 = Address('1', 'Infinite Loop', 'Hillarys', '6025')
testPerson2 = Staff('Professor Awesome', '1/6/61', testAdd2, '12345J') 
testPerson2.displayPerson()
print()

testAdd3 = Address('1', 'Canning', 'Hill', '6000')
testPerson3 = Student('Mi Ha Chan', '1/6/03', testAdd3, 'S12345') 
testPerson3.displayStudent()
print()

testAdd4 = Address('11', 'Avenger', 'War', '6525')
testPerson4 = Postgrad('Long Bao', '1/9/01', testAdd4, 'P12345') 
testPerson4.displayPostgrad()
print()

testAdd5 = Address('7', 'Saringan', 'Chidori', '6035')
testPerson5 = Undergrad('Chicken 1', '1/6/07', testAdd5, 'U12345') 
testPerson5.displayUndergrad()
print()
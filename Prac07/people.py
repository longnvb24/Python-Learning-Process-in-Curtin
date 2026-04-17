class Address():
    def __init__(self, number, street, suburb, postcode): 
        self.number = number
        self.street = street
        self.suburb = suburb
        self.postcode = postcode
        
    def __str__(self):
        return(self.number + ' ' + self.street + ', ' + self.suburb + ', ' + self.postcode)

class Person():
    def __init__(self, name, dob, address): 
        self.name = name
        if self.validDOB(dob):
            self.dob = dob
        else:
            raise ValueError("Invalid date of birth for " + self.name + ": " + dob)
        self.address = address
        
    def displayPerson(self):
        print('Name: ', self.name, '\tDOB: ', self.dob) 
        print(' Address: ', str(self.address))
        
    def validDOB(self, dob):
        try:
            day, month, year = dob.split('/')
            day = int(day)
            month = int(month)
            year = int(year)
            if day < 1 or day > 31:
                return False
            if month < 1 or month > 12:
                return False
            if year < 0 or year > 100:
                return False
            return True
        except ValueError:
            return False
        
class Staff(Person):
    myclass = 'Staff'
    def __init__(self, name, dob, address,id):
        super().__init__(name, dob, address)
        self.id = id
        
    def displayPerson(self):
        super().displayPerson()
        print(' Staff ID: ', self.id)
        
class Student(Person):
    myclass = 'Student'
    def __init__(self, name, dob, address,id):
        super().__init__(name, dob, address)
        self.id = id
    
    def displayStudent(self):
        super().displayPerson()
        print(' Student ID: ', self.id)

class Postgrad(Student, Person):
    def displayPostgrad(self):
        super().displayPerson()
        print(' Postgrad ID: ', self.id)

class Undergrad(Student, Person):
    myclass = 'Undergrad'
    def displayUndergrad(self):
        super().displayPerson()
        print(' Undergrad ID: ', self.id)
        
    
    
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname;
        self.secondname = lname;
    def printname(self):
        print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()




#child class --- 
class Student(Person):
  pass



x = Student("Mike", "Olsen")
x.printname()




class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.



class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)



#super --- 
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)



    
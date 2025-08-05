class cpscTA:
    Species = "Human"
    Class = "CPSC 231"
    Level = 99

    def __init__(self, Name, Status):
        self.Name = Name
        self.Status = Status

    def introduceYourself(self):
        print(f"Hello, My name is {self.Name}! I am a {self.Class} TA! I am {self.Status}! ")


t10TA = cpscTA("Brandon Sieu", "a great TA")
t10TA.introduceYourself()

# Question 1: What are the attributes (or fields) of the class?
# The attributes of the class are Species, Class, Level, Name, and Status.

# Question 2: What is the constructor of the class?
#     def __init__(self, Name, Status):
#         self.Name = Name
#         self.Status = Status
# Lines 6-8 of this code are  the constructor of the class.

# Question 3: What are the methods inside the class?
#     def introduceYourself(self):
#         print(f"Hello, I am a {self.Class} TA! I am {self.Status}! My name is {self.Name}!")
# Lines 10-11 are the methods inside the class.

# Question 4: What is/are the variable that has class level scope?
# Species, Class, and Level have class level scope.

# Question 5: What is/are the variables that have object level scope?
# Name and Status are variables that have object level scope.

# Question 6: What is the name of the object?
# The object is named t10TA

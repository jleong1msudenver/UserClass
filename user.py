
class User:
    def __init__(self, firstName, lastName, email, age, phoneNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.age = age
        self.phoneNumber = phoneNumber
        


    def describe_user(self):
        print(f"Please verify your information below. \n First Name: {self.firstName} Last Name: {self.lastName} \n Email: {self.email} Age: {self.age} \n Phone Number: {self.phoneNumber}")



me = User("Josh", "Leong", "leong.jo@gmail.com", 35, "310-382-6484")
me.describe_user()




    # def setFirstName()
    
    # def setLastName()
    # def getLastName()



# create setter and getter


'''
9-3. Users: Make a class called User. Create two attributes called first_name and last_name, 
and then create several other attributes that are typically stored in a user profile. Make a 
method called describe_user() that prints a summary of the user’s information. Make another method 
called greet_user() that prints a personalized greeting to the user.
Create several instances representing different users, and call both methods for each user.
'''



# The first file we build the class 
# The next file is about my car using the class
# The next file is about making different types of cars
# make a new car 
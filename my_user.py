from user import User

newUser = User("Josh", "Leong", "myemail@gmail.com", 35, "303-333-555")
print(newUser.DescribeUser())

newUser.setFirstName = "Ron"
print(newUser.DescribeUser())
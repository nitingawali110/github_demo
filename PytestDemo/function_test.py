
def sample_function():
    print("inside my sample statment")


sample_function() # function calling statement

# Parameterizing functions
def print_name(name): # name=parameter
    print("Your name is :", name)

print_name("Nitin") # Nitin=Argument

# Default Argument
def print_name1(name="Arun"): # name=parameter
    print("Your name is :", name)

print_name1()
print_name1("Nitin") # Nitin=Argument

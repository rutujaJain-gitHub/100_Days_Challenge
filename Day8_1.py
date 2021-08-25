
def greet():
    print("Hello!!")
    print("How do you do?")
    print("Isn't the weather nice today?")
greet()
name = input("enter your name: ")
location = input("Enter your location: ")

def greet_with_name(name, location):
    print(f"Hello {name}")
    print(f"you are from which location?{location}")

greet_with_name(name, location)



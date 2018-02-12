"""
CS241 Checkpoint B6
Written by Chad Macbeth
"""

### Represents a phone
class Phone:

    ### Initialize a phone object
    def __init__(self):
        self.area_code = 0
        self.prefix = 0
        self.suffix = 0

    ### Get the phone number from the user
    def prompt_number(self):
        self.area_code = int(input("Area Code: "))
        self.prefix = int(input("Prefix: "))
        self.suffix = int(input("Suffix: "))

    ### Display the phone number
    def display(self):
        print("Phone info:")
        print("({}){}-{}" .format(self.area_code, self.prefix, self.suffix))

### Reperesents a smart phone which is derived from a Phone
class SmartPhone(Phone):

    ### Initialize a smart phone object
    def __init__(self):
        super().__init__()
        self.email = ""

    ### Get the smart phone information from the user
    def prompt(self):
        super().prompt_number()
        self.email = input("Email: ")

    ### Display the smart phone information
    def display(self):
        super().display()
        print(self.email)

### Test the classes above
def main():
    phone = Phone()
    print("Phone:") 
    phone.prompt_number()
    print()
    phone.display()
    print()

    print("Smart phone:")
    smart = SmartPhone()
    smart.prompt()
    print()
    smart.display()

if __name__ == "__main__":
    main()

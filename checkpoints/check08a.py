"""
CS241 Checkpoint 8A
Written by Chad Macbeth
"""

### Class represents a GPA and allows conversion
### between letter and grade point average.
class GPA:

    ### Initialize the GPA object
    def __init__(self):
        self.gpa = 0

    ### Accessor for GPA
    def get_gpa(self):
        return self.gpa

    ### Mutator for GPA
    ### GPA must be positive
    def set_gpa(self, gpa):
        if gpa < 0.0:
            self.gpa = 0.0
        else:
            self.gpa = gpa 

    ### Convert the GPA to a letter grade
    def get_letter(self):
        if self.gpa <= 0.99:
            return "F"
        elif self.gpa <= 1.99:
            return "D"
        elif self.gpa <= 2.99:
            return "C"
        elif self.gpa <= 3.99:
            return "B"
        else:
            return "A"

    ### Convert a letter to a GPA
    def set_letter(self, letter):
        if letter == "A":
            self.gpa = 4.0
        elif letter == "B":
            self.gpa = 3.0
        elif letter == "C":
            self.gpa = 2.0
        elif letter == "D":
            self.gpa = 1.0
        else:
            self.gpa = 0.0

### Test the GPA Class
def main():
    student = GPA()

    print("Initial values:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

    value = float(input("Enter a new GPA: "))

    student.set_gpa(value)

    print("After setting value:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

    letter = input("Enter a new letter: ")

    student.set_letter(letter)

    print("After setting letter:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

if __name__ == "__main__":
    main()

 


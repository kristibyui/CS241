"""
CS241 Checkpoint 8B
Written by Chad Macbeth
"""

### Class represents a GPA and allows conversion
### between letter and grade point average.
class GPA:

    ### Initialize the GPA object
    def __init__(self):
        self._gpa = 0.0

    ### Accessor for GPA
    def _get_gpa(self):
        return self._gpa

    ### Mutator for GPA
    ### GPA must be positive
    def _set_gpa(self, gpa):
        if gpa < 0.0:
            self._gpa = 0.0
        else:
            self._gpa = gpa 

    ### Convert the GPA to a letter grade
    def _get_letter(self):
        if self._gpa <= 0.99:
            return "F"
        elif self._gpa <= 1.99:
            return "D"
        elif self._gpa <= 2.99:
            return "C"
        elif self._gpa <= 3.99:
            return "B"
        else:
            return "A"

    ### Convert a letter to a GPA
    def _set_letter(self, letter):
        if letter == "A":
            self._gpa = 4.0
        elif letter == "B":
            self._gpa = 3.0
        elif letter == "C":
            self._gpa = 2.0
        elif letter == "D":
            self._gpa = 1.0
        else:
            self._gpa = 0.0

    ### Allows user to get and set gpa without calling a function 
    gpa = property(_get_gpa, _set_gpa)

    ### Allows user to get the ltter without calling a function
    @property
    def letter(self):
        return self._get_letter()

    ### Allows user to set the gpa based on the letter without calling a function
    @letter.setter
    def letter(self,letter):
        self._set_letter(letter)
        

### Test the GPA Class
def main():
    student = GPA()

    print("Initial values:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

    value = float(input("Enter a new GPA: "))

    student.gpa = value

    print("After setting value:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

    letter = input("Enter a new letter: ")

    student.letter = letter

    print("After setting letter:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

if __name__ == "__main__":
    main()

 


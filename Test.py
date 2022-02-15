def main():
    # Prints the Main Menu. This is where you input your choice for functions.
    choice = ''
    while choice.lower() != 'x':
        Print_MainMenu()
        choice = input("Selection: ")
        if choice.lower() == 'a':
            Add_Student()

# Function to add student.
def Add_Student():
    # Opens the AllStudents text file where all students are located.
    f = open("AllStudents","at")

    while(True):
        student_name_input = input("Enter student name: ")

        # Removes all space to see all characters input are alphanumerical.
        temp_name_copy = student_name_input
        temp_name_copy = temp_name_copy.replace(" ","")

        # if isalpha() == true, break loop and write input on AllStudents text file.
        if temp_name_copy.isalpha():
            print("written")
    
            f.write(student_name_input)
            f.write("\n")
            
            break
    pass

def Add_Course():
    pass

def Add_Section():
    pass

def Add_Grade_Component():
    pass

def Compute_Grades():
    pass

def View_Student_Section():
    pass

def View_All_Students():
    pass

def Print_MainMenu():
    print("(A) Add Student") # Add Student --> Select Section??
    print("(B) Add Course") # Select Section --> Select Course??
    print("(C) Add Section") # Add Section
    print("(D) Add Grade Components") # Grade Components
    print("(E) Grade Computation")
    print("(F) View Student Grade per Section")
    print("(G) View All Student")
    print("(X) Exit")
    

main()

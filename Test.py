import csv
namesect = "name,section"

def main():
    # Prints the Main Menu. This is where you input your choice for functions.
    choice = ''
    while True:
        Print_MainMenu()
        choice = input("Selection: ")
        if choice.lower() == 'a':
            Add_Student()
        if choice.lower() == 'd':
            view_students()
        if choice.lower() == 'x':
            break
        

# Function to add student.
def Print_MainMenu():
    print("MAIN MENU --")
    print("(A) Add Student") # Add Student --> Select Section??
    print("(B) Add Course") # Select Section --> Select Course??
    print("(C) Add Section") # Add Section
    print("(D) View Students per Section")
    print("(X) Exit")

def view_students():
  with open('AllStudents','r') as file:
    reader = csv.DictReader(file)
    for i in reader:
      print(i["name"])

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

def Add_Student():
    # Opens the AllStudents text file where all students are located.
    
    choice = ''
    while True:
        print("ADD STUDENT --")
        print("A.a) Add Students")
        print("B.b) Remove Students")
        print("B.x) Back")
        choice = input("Selection: ")
        if choice.lower() == 'a':
            A_add_student()
        elif choice.lower() == 'b':
            A_remove_student()
        elif choice.lower() == 'x':
            print("go here")
            break

def A_remove_student():
    studentList = []
    name = ""
    with open("AllStudents","r") as f:
      next(f)
      print("Name, Section")
      for i in f:
        print(i.rstrip())
        
      while True:
        with open("AllStudents","r") as f:
          reader = csv.DictReader(f)
          
          choice = input("Student to Remove: ")
          
          for element in reader:
            name = element["name"]
            section = element["section"]
            studentList.append(name)

          for i in studentList:
            if i == choice:
              studentList.remove(choice)
          print(studentList)
          

          with open("AllStudents","w") as f:
            
            writing = csv.writer(f)
            f.write(namesect)
            f.write("\n")
            for i in studentList:
              if i != choice:
                writing.writerow([name,section])
          break
    

def A_add_student():
    while True:
      
      student_name_input = input("Enter student name: ")
      student_section_input = input("Enter section: ")

            # Removes all space to see all characters input are alphanumerical.
      temp_name_copy = student_name_input
      temp_name_copy = temp_name_copy.replace(" ","")

            # if isalpha() == true, break loop and write input on AllStudents text file.
      if temp_name_copy.isalpha():
          print("written")
      with open("AllStudents","at") as f:
          writing = csv.writer(f)
          writing.writerow([student_name_input,student_section_input])
          break

main()

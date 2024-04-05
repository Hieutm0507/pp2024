#   Overview: Student mark management system
#   Requirements: NO object/ class. Use tuples, dicts, lists
#   Author: Hieu Ta Minh


class Student:
    def __init__(self, idStudent, nameStudent, dobStudent):
        self._idStudent = idStudent
        self._nameStudent = nameStudent
        self._dob = dobStudent
        self._courses = []              #empty list for the case we store instance classes

    def get_nameS(self):
        return self._nameStudent
    
    def get_idS (self):
        return self._idStudent

    def get_dob(self):
        return self._dob
    
    def add_course(self, course, mark):                             #Using dict
        self._courses.append({"Course":course, "Mark": mark})

    def showFull(self):
        print("\n{:<16} {:<16} {:<16} {:<16} {:<16} {:<16}".format(
            "Student ID", "Name", "Date of Birth", "Course ID", "Course Name", "Mark"))
        for data in self._courses:
            course = data["Course"]
            mark = data["Mark"]
            print("{:<16} {:<16} {:<16} {:<16} {:<16} {:<16}".format(
                self.get_idS(), self.get_nameS(), self.get_dob(), course.get_idC(), course.get_nameC(), mark))
        print()


class Course:
    def __init__(self, idCourse, nameCourse):
        self._idCourse = idCourse
        self._nameCourse = nameCourse

    def get_idC (self):
        return self._idCourse
        
    def get_nameC (self):
        return self._nameCourse


class Mark:
    def __init__(self):
        self._StudentList = []              #empty list for the case we store instance classes

    def add_student(self, student):
        self._StudentList.append(student)

    def showList(self):
        for student in self._StudentList:
            student.showFull()
    
    def showStudentInfo(self):
        print("{:<15} {:<15} {:<15}".format("Student ID", "Student name", "Date of Birth"))
        for student in self._StudentList:
            print("{:<15} {:<15} {:<15}".format(student.get_idS(), student.get_nameS(), student.get_dob()))

    def showCourseInfo(self):
        print("{:<15} {:<15}".format("Course ID", "Course name"))
        for student in self._StudentList:
            for data in student._courses:
                course = data["Course"]
                print("{:<15} {:<15}".format(course.get_idC(), course.get_nameC()))

    def showFollowChoose(self):
        idStudent = input("Enter Student ID: ")
        found = False
        for student in self._StudentList:
            if student.get_idS()== idStudent:
                idCourse = input("Enter Course ID: ")
                for data in student._courses:
                    course = data["Course"]
                    mark = data["Mark"]
                    if course.get_idC() == idCourse:
                        found = True
                        print("\nMark for {} in {}: {}".format(student.get_nameS(), course.get_nameC(), mark))
        if not found:
            print("Student or Course not found.")


# --------------------------------------

# Take input for Student information
def inputStudentInfo():
    idStudent = input("Enter Student's ID: ")
    nameStudent = input("Enter Student's name: ")
    dobStudent = input("Enter DoB of Student: ")
    return Student(idStudent, nameStudent, dobStudent)


# Take input for Course information
def inputCourseInfo():
    idCourse = input("Enter the Course's ID: ")
    nameCourse = input("Enter the Course's name: ")
    return Course(idCourse, nameCourse)


# Take input for Marks information
def inputMark():
    mark = float(input("Enter the mark for this Course: "))
    return mark


# --------------------------------------

# MAIN FUNCTION
def main():
    Management_System = Mark()

    numOfStudent = int(input("Number of the student: "))

    for _ in range(numOfStudent):
        studentInfo = inputStudentInfo()
        numOfCourse = int(input("Enter number of course for {}: ".format(studentInfo.get_nameS())))

        #Student object is created and add to StudentList list
        student = Student(studentInfo.get_idS(), studentInfo.get_nameS(), studentInfo.get_dob())

        for _ in range(numOfCourse):
            courseInfo = inputCourseInfo()
            mark = inputMark()

            #Course object is created 
            course = Course(courseInfo.get_idC(), courseInfo.get_nameC())
            #adding the course to course list created in Student class
            student.add_course(course, mark)

        #adding the student to the StudentList list 
        Management_System.add_student(student)
    while True:
        print("---------------------------------------------------------")
        print("1. Show the Student List information")
        print("2. Show the Course List")
        print("3. Show Student with mark of choosen Course")
        print("4. Show full")
        print("0. Exit")
        print("---------------------------------------------------------")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            Management_System.showStudentInfo()
        elif choice == 2:
            Management_System.showCourseInfo()
        elif choice == 3:
            Management_System.showFollowChoose()
        elif choice ==4:
            Management_System.showList()
        elif choice == 0:
            break
        else:
            print("Invalid")

if __name__ == "__main__":
    main()
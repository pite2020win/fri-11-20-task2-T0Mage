
class Student:
    def __init__(self,fname="unnknown",lname="unnknown"):
        self.fname,self.lname=fname,lname
        self.grades={}
        self.attendance={}

    def add_subject(self,subjectName):
        self.grades[subjectName]=[]
        self.attendance[subjectName]=[]

    def add_grade(self,subjectName,grade):
        self.grades[subjectName].append(grade)

    def average_grade(self,subjectName):
        return sum(self.grades[subjectName])/len(self.grades[subjectName])


    def add_attendance(self,subjectName,isPresent=False):
        self.attendance[subjectName].append({"isPresent":isPresent})

    def __repr__(self):
        return f"{self.fname},{self.lname},{self.grades},{self.attendance}"
    
if __name__ == "__main__":
    testStudent= Student("john","xyz")
    testStudent.add_subject("math")
    testStudent.add_attendance("math",True)
    testStudent.add_grade("math",3)
    testStudent.add_grade("math",4)
    testStudent.add_attendance("math")
    print("avg grade:",testStudent.average_grade("math"))

    print(testStudent)

class Students:
    def __init__(self, name, reg_no):
        self.name = name
        self.reg_no = reg_no
        
    def display_info(self):
        print(f"Student_name: {self.name}")
        print(f"Registration_number: {self.reg_no}")
        
student1 = Students("Nasuuna Swabulah", "B20276")
student1.display_info()

student2 = Students("Kizito Hampus", "S20273")
student2.display_info()
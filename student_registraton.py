class Student:
    def __init__(self, student_id, name, department):
        self.student_id = student_id
        self.name = name
        self.department = department

    def display_details(self):
        print("\n--- Student Details ---")
        print(f"ID        : {self.student_id}")
        print(f"Name      : {self.name}")
        print(f"Department: {self.department}")

    # Feature 1 (Day 1)
    def update_department(self, new_department):
        self.department = new_department
        print("Department updated successfully!")


def main():
    print("=== Student Registration Module ===")

    # Creating a student object
    student = Student(101, "Arun", "CSE")
    student.display_details()

    # Day-wise change starts here 👇
    student.update_department("AI & DS")
    student.display_details()


if __name__ == "__main__":
    main()

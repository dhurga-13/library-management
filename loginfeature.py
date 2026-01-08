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


class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authenticate(self):
        if self.username == "admin" and self.password == "admin123":
            print("Login successful!")
            return True
        else:
            print("Invalid username or password")
            return False


def main():
    print("=== Student Registration Module ===")

    login = Login("admin", "admin123")
    if not login.authenticate():
        return

    student = Student(101, "Arun", "CSE")
    student.display_details()


if __name__ == "__main__":
    main()

import json
import os
from datetime import date

FILE = "attendance.json"


class AttendanceManager:
    def __init__(self, filename):
        self.filename = filename
        self.attendance = self.load_attendance()

    def load_attendance(self):
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump({}, f, indent=2)

        with open(self.filename, "r") as f:
            return json.load(f)

    def save_attendance(self):
        with open(self.filename, "w") as f:
            json.dump(self.attendance, f, indent=2)

    def mark_attendance(self):
        today = date.today().strftime("%d-%m-%Y")
        name = input("Student name: ").strip().lower()
        status = input("Status (Present/Absent): ").strip().capitalize()

        if status not in ("Present", "Absent"):
            print("Invalid status")
            return

        self.attendance.setdefault(today, {})
        self.attendance[today][name] = status
        self.save_attendance()
        print("Attendance marked")

    def view_by_date(self):
        date_key = input("Enter date (dd-mm-yyyy): ").strip()

        if date_key not in self.attendance:
            print("Date not found")
            return

        print(f"\nAttendance for {date_key}")
        for name, status in self.attendance[date_key].items():
            print(f"{name} => {status}")

    def view_all(self):
        if not self.attendance:
            print("No attendance records")
            return

        for date_key, records in self.attendance.items():
            print(f"\nDate: {date_key}")
            for name, status in records.items():
                print(f"{name} => {status}")

    def delete_student(self):
        date_key = input("Enter date (dd-mm-yyyy): ").strip()
        name = input("Student name to delete: ").strip().lower()

        if date_key not in self.attendance:
            print("Date not found ")
            return

        if name not in self.attendance[date_key]:
            print("Student not found ")
            return

        del self.attendance[date_key][name]

        if not self.attendance[date_key]: 
            del self.attendance[date_key]

        self.save_attendance()
        print("Student deleted ")
    def student_percentage(self):
        totals = {}
        present = {}

        for d, records in self.attendance.items():
            for name, status in records.items():
                totals[name] = totals.get(name, 0) + 1 
                if status == "Present":
                    present[name] = present.get(name, 0) + 1
            print("Attendance Precentage")
            
            for name in totals:
                precent = present.get(name, 0) / totals[name] * 100
                print(f"{name} => {precent: .2f}%")
               

def main():
    manager = AttendanceManager(FILE)

    while True:
        print("\n1. Mark attendance")
        print("2. View by date")
        print("3. View all")
        print("4. Delete student")
        print("5. Attendance percentage.")
        print("6. Exit")

        choice = input("Choose (1-6): ")

        if choice == "1":
            manager.mark_attendance()
        elif choice == "2":
            manager.view_by_date()
        elif choice == "3":
            manager.view_all()
        elif choice == "4":
            manager.delete_student()
        elif choice == "5":
            manager.student_percentage()
        elif choice == "6":
            break
        else:
            print("Invalid choice ")


main()


  
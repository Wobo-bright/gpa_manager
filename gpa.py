import json
from tabulate import tabulate

grades_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
    "E": 1,
    "F": 0
}

class GPA:
    def _init_(self):
        self.courses = []

    def add_course(self, course_name, course_unit, course_grade=None):
        numerical_value = grades_values.get(course_grade)
        course_details = {"name": course_name, "unit": course_unit, "grade": numerical_value}

        if any(c['name'] == course_name for c in self.courses):
            return "Course is already on your course list."
        else:
            self.courses.append(course_details)
            return f"{course_name}: {course_unit} unit(s) uploaded successfully."

    def view_courses(self):
        if not self.courses:
            return "No courses added yet. So your list is empty"

        table = []
        for index, course in enumerate(self.courses, start=1):
            letter = next((grade for grade, score in grades_values.items() if score == course['grade']), "N/A")
            table.append([index, course['name'], course['unit'], letter])

        return tabulate(table, headers=["S/N", "Course", "Unit", "Grade"], tablefmt="fancy_grid")

    def update_details(self, course_name, new_course_name=None, new_course_unit=None, new_course_grade=None):
        if not self.courses:
            return "Course list is empty."
        for course_details in self.courses:
            if course_details['name'] == course_name:
                if new_course_name:
                    course_details['name'] = new_course_name
                if new_course_grade:
                    num_value = grades_values.get(new_course_grade)
                    course_details['grade'] = num_value
                if new_course_unit:
                    course_details['unit'] = new_course_unit
                return f"Course updated successfully: {course_details['name']}. Unit: {course_details['unit']}. Grade: {course_details['grade']}."
        return "Such course has not been saved."

    def delete_course(self, course_name):
        if not self.courses:
            return "No courses to delete."
        for course_details in self.courses:
            if course_name == course_details['name']:
                self.courses.remove(course_details)
                return f"{course_details['name']} has been deleted."
        return "Course not found."

    def gpa_calc(self):
        if not self.courses:
            return "No courses to calculate GPA."

        unit_list = []
        grade_score_list = []

        for course_details in self.courses:
            unit_list.append(course_details['unit'])
            grade_score_list.append(course_details['grade'])

        total_units = sum(int(unit) for unit in unit_list)
        accumulated_gp = sum(int(unit_list[i]) * int(grade_score_list[i]) for i in range(len(unit_list)))

        grade_point_average = "{:.2f}".format(accumulated_gp / total_units)
        return f"Your GPA is {grade_point_average}"

    def save_semester(self, filename="Semester_rec.json"):
        with open(filename, "w") as file:
            json.dump(self.courses, file, default=str)
        return "Courses saved successfully."

    def load_semester(self, filename="Semester_rec.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.courses = [
                    {
                        "name": course_details['name'],
                        "unit": course_details['unit'],
                        "grade": course_details['grade'],
                    }
                    for course_details in data
                ]
            return "Courses loaded successfully."
        except (FileNotFoundError, json.JSONDecodeError):
            self.courses = []
            return "Nothing to load. Add a course."

    def clear_rec(self, filename="Semester_rec.json"):
        self.courses = []
        with open(filename, "w") as file:
            json.dump(self.courses, file, default=str)
        return "All records cleared successfully."


if __name__ == "__main__":
    gpa = GPA()
    print(gpa.load_semester())

    while True:
        option = input('''

Options;
1. Add course details
2. View course(s)
3. Update course details
4. Save semester record
5. Load saved semester record
6. Your GPA
7. Clear records
quit?

> ''').strip()

        if option == "1":
            course_name = input("Enter the name of your course: ").upper()
            course_grade = input("Enter the grade of your course (A-F): ").upper()
            try:
                course_unit = int(input("Enter the unit of your course: "))
                result = gpa.add_course(course_name, course_unit, course_grade)
                print(result)
            except ValueError:
                print("Invalid course unit. Please enter a number.")

        elif option == "2":
            print(gpa.view_courses())

        elif option == "3":
            sub_choice = input("What do you want to update?\n1. Course name \n2. Course unit \n3. Course grade\n\n> ").strip()
            course_name = input("Enter the course name you want to update: ").upper()

            if sub_choice == "1":
                new_course_name = input("Enter the new course name: ").upper()
                print(gpa.update_details(course_name, new_course_name=new_course_name))
            elif sub_choice == "2":
                new_course_unit = input("Enter the new course unit: ")
                print(gpa.update_details(course_name, new_course_unit=new_course_unit))
            elif sub_choice == "3":
                new_course_grade = input("Enter the new course grade: ").upper()
                print(gpa.update_details(course_name, new_course_grade=new_course_grade))
            else:
                print("Enter a correct update option.")

        elif option == "4":
            print(gpa.save_semester())

        elif option == "5":
            print(gpa.load_semester())

        elif option == "6":
            print(gpa.gpa_calc())

        elif option == "7":
            print(gpa.clear_rec())

        elif option.lower() in ["quit", "stop", "end","q", "e"]:
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose from the list.")
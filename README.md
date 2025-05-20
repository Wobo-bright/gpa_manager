# 🎓 GPA Calculator – Python CLI App

This is a **command-line GPA calculator** written in Python that helps students manage their course details and calculate their GPA. The app allows users to add, update, delete, and view courses, as well as save and load semester records using JSON for persistent storage.

---

## ✨ Features

* ✅ **Add Courses** – Save course name, unit, and grade
* 📋 **View Courses** – Display all saved courses with units and letter grades
* 📝 **Update Details** – Change course name, unit, or grade
* 🗑️ **Delete Courses** – Remove courses by name
* 🧮 **Calculate GPA** – GPA is computed using weighted grade points
* 💾 **Save Semester** – Store your current course list to a `.json` file
* 📂 **Load Semester** – Load your saved course list on app startup
* 🚮 **Clear Records** – Reset all saved course data

---

## 🧠 Grading System

| Grade | Value |
| ----- | ----- |
| A     | 5     |
| B     | 4     |
| C     | 3     |
| D     | 2     |
| E     | 1     |
| F     | 0     |

---

## 📦 Requirements

* Python 3.6 or higher
* install and import **tabulate**

All other libraries used are built-in (no external dependencies).

---

## 🚀 Installation

0. **Install the required moudule for tabulation**
      ```bash
      pip install tabulate
   ```
   

2. **Clone this repository**:

   ```bash
   git clone https://github.com/wobo-bright/gpa_manager.git
   cd gpa_manager
   ```

3. **Run the program**:

   ```bash
   python gpa.py
   ```

---

## 🖥️ Usage

After launching the program, you’ll see options to add, view, update, or manage course records. Follow the prompts by entering the corresponding number or command.

Example:

```
Options:
1. Add course details
2. View course(s)
3. Update course details
...
```

---

## 📁 File Storage

The program saves and loads course records from a file named `Semester_rec.json` in the same directory. You can back this file up to save progress or start a new semester by clearing it.

---

## 🛠️ Future Improvements (Ideas)

* Add CGPA tracking across semesters
* Add input validation for edge cases
* Add GUI interface (Tkinter or PyQt)
* Export records to Excel or PDF

---

## 👤 Author

**Bright** – *Python developer & student-focused tool builder*

StudyMaster 📚
An All-in-One Academic Productivity Toolkit for Students

StudyMaster is a Python package designed to help students manage their academic responsibilities from a single, unified interface. Below is a comprehensive guide to every function and class in the package, complete with code examples, descriptions, and their intended purposes.

🛠️ Detailed Functions & Examples
1. GPA Calculator (gpa.py)
Function: calculate_gpa(grades)

What it is for: Helps students quickly calculate their cumulative GPA for a given set of letter grades based on a standard 4.0 scale.

Example:

Python
from studymaster import calculate_gpa

grades_list = ["A", "A-", "B+"]
print(calculate_gpa(grades_list))
# Output: 3.67

2. Exam Countdown (exam.py)
Function: exam_countdown(exam_date)

What it is for: Allows students to track the exact number of days remaining until an upcoming exam so they can plan their study timeline.

Example:

Python
from studymaster import exam_countdown

# Pass date as an ISO string ("YYYY-MM-DD")
print(exam_countdown("2026-12-20"))
# Output: Number of days remaining until December 20, 2026

3. Homework Deadline Manager (deadline.py)
Functions: days_left(deadline) and urgency_level(deadline)

What it is for: Tracks assignment due dates and automatically categorizes tasks into priority tiers (High, Medium, Low) to prevent missed deadlines.

Example:

Python
from studymaster import days_left, urgency_level

deadline_date = "2026-12-01"
print(days_left(deadline_date))       # Output: Remaining days (e.g., 19)
print(urgency_level(deadline_date))   # Output: "High Priority", "Medium Priority", or "Low Priority"

4. Study Timer (timer.py)
Class: StudySession

What it is for: Enables students to incrementally record minutes spent studying across multiple blocks of time and easily view their total study hours.

Example:

Python
from studymaster import StudySession

session = StudySession()
session.add_time(120)  # Add 120 minutes of study time
print(session.total_hours())
# Output: 2.0

5. Quiz Generator (quiz.py)
Function: create_quiz(notes)

What it is for: Automatically transforms raw study notes or vocabulary lists into formatted flashcard-style review questions for exam prep.

Example:

Python
from studymaster import create_quiz

notes = {"Accounts Receivable": "Money owed by customers"}
print(create_quiz(notes))
# Output: ['Q: What is Accounts Receivable?\nA: Money owed by customers']

6. Smart Task Prioritization (planner.py)
Functions: add_task(name, days_left, difficulty) and recommend_tasks()

What it is for: Mathematically weighs assignment difficulty and deadline urgency to recommend the optimal completion order.

Example:

Python
from studymaster import add_task, recommend_tasks

# Add tasks: add_task(name, days_until_deadline, difficulty_score)
add_task("CS Project", 3, 9)
add_task("Accounting Homework", 7, 4)

print(recommend_tasks())
# Output: Ordered list of tasks sorted by highest priority score first
```[cite: 1, 2, 3, 5, 6, 7]

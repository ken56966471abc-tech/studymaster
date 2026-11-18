 StudyMaster
An All-in-One Academic Productivity Toolkit for Students
StudyMaster is a Python package that helps students manage their academic responsibilities more effectively. Instead of using multiple applications, students can use a single package to calculate GPA, track deadlines, monitor study time, prepare for exams, generate quizzes, and prioritize assignments.

📖 Motivation
Students often struggle with:

Tracking assignment deadlines
Managing exam schedules
Monitoring GPA performance
Recording study hours
Creating revision materials
Deciding which assignment to complete first
Many existing tools focus on only one of these tasks. StudyMaster combines multiple academic productivity tools into a single package, making student organization simpler and more efficient.

🚀 Features
StudyMaster includes six major features:

📊 GPA Calculator
Calculate GPA using a list of letter grades.

📅 Exam Countdown
Track the number of days remaining before an exam.

📚 Homework Deadline Manager
Monitor assignment deadlines and urgency levels.

⏱️ Study Timer
Track study sessions and total study hours.

❓ Quiz Generator
Convert notes into quiz-style flashcards.

🎯 Smart Task Prioritization
Automatically recommend which assignment should be completed first based on deadline urgency and difficulty.

💡 Innovation
Unlike traditional student productivity tools that perform only one task, StudyMaster integrates six academic functions into a single package.

The most innovative feature is Smart Task Prioritization, which evaluates:

Assignment difficulty
Deadline urgency
and automatically recommends the best order for completing assignments.

This helps students allocate their time more effectively and improve productivity.

📦 Installation
Install StudyMaster using pip:

pip install studymaster
🖥️ Usage Examples
1. GPA Calculator
Example
from studymaster import calculate_gpa

print(calculate_gpa(["A", "A-", "B+"]))
Output
3.67
Explanation
The function converts letter grades into grade points and calculates the average GPA.

Grade Scale:

Grade	Point
A	4.0
A-	3.7
B+	3.3
B	3.0
B-	2.7
C+	2.3
C	2.0
D	1.0
F	0.0
2. Exam Countdown
Example
from studymaster import exam_countdown

print(exam_countdown("2026-12-20"))
Output
38
Explanation
Returns the number of days before an upcoming exam.

3. Homework Deadline Manager
Calculate Remaining Days
from studymaster import days_left

print(days_left("2026-12-01"))
Output
19
Explanation
Returns the remaining number of days before a deadline.

Check Urgency
from studymaster import urgency_level

print(urgency_level("2026-11-15"))
Output
High Priority
Priority Levels
Days Remaining	Priority
0 – 3	High Priority
4 – 7	Medium Priority
More than 7	Low Priority
4. Study Timer
Example
from studymaster import StudySession

session = StudySession()

session.add_time(120)

print(session.total_hours())
Output
2.0
Explanation
Converts total study minutes into hours.

In this example:

120 minutes = 2 hours
5. Quiz Generator
Example
from studymaster import create_quiz

notes = {
    "Accounts Receivable":
    "Money owed by customers"
}

print(create_quiz(notes))
Output
Q: What is Accounts Receivable?
A: Money owed by customers
Explanation
Converts notes into flashcard-style study questions.

Input Format:

{
    "Topic": "Definition"
}
6. Smart Task Prioritization
Purpose
Helps students determine which assignment should be completed first.

Example
from studymaster import add_task
from studymaster import recommend_tasks

add_task("CS Project", 3, 9)

add_task("Accounting Homework", 7, 4)

print(recommend_tasks())
Input Format
add_task(task_name, days_until_deadline, difficulty)
Input Example 1
add_task("CS Project", 3, 9)
Meaning:

Task Name: CS Project
Days Until Deadline: 3
Difficulty: 9/10
Input Example 2
add_task("Accounting Homework", 7, 4)
Meaning:

Task Name: Accounting Homework
Days Until Deadline: 7
Difficulty: 4/10
Priority Formula
priority_score = difficulty * 10 + (30 - days_left)
A higher score means a higher priority.

Score Calculation
CS Project
Difficulty = 9

9 × 10 = 90

Days Remaining = 3

30 - 3 = 27

Priority Score = 117
Accounting Homework
Difficulty = 4

4 × 10 = 40

Days Remaining = 7

30 - 7 = 23

Priority Score = 63
Output
[
 {'name': 'CS Project', 'score': 117},
 {'name': 'Accounting Homework', 'score': 63}
]
Explanation
Since the CS Project:

Has a closer deadline
Has a higher difficulty level
it receives a higher priority score and should be completed first.

🧪 Running Tests
Run tests using:

pytest
Example test file:

from studymaster import calculate_gpa

def test_gpa():
    assert calculate_gpa(["A", "B"]) == 3.5
👥 Team Contributions
Member	Responsibility
Member 1	GPA Calculator
Member 2	Exam Countdown
Member 3	Homework Deadline Manager
Member 4	Study Timer
Member 5	Quiz Generator
Member 6	Smart Task Prioritization
🔮 Future Improvements
Potential future enhancements:

GUI desktop application
Mobile application
Calendar integration
GPA prediction system
Study analytics dashboard
AI-powered quiz generation
Assignment reminders and notifications
Cloud data storage
🎬 Demo
from studymaster import *

print(calculate_gpa(["A", "A-", "B+"]))

print(days_left("2026-12-01"))

session = StudySession()

session.add_time(120)

print(session.total_hours())

add_task("CS Project", 3, 9)

add_task("Accounting Homework", 7, 4)

print(recommend_tasks())
Expected Output:

3.67

19

2.0

[
 {'name': 'CS Project', 'score': 117},
 {'name': 'Accounting Homework', 'score': 63}
]
✅ Conclusion
StudyMaster is a comprehensive academic productivity package that helps students manage GPA, exams, deadlines, study time, quizzes, and assignment priorities.

By combining multiple tools into one package, StudyMaster provides students with a simple, effective, and organized way to improve academic performance and productivity.

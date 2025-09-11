'''3. Classroom Performance Tracker

Scenario:A teacher wants to track student performance. Write a program to calculate the **average marks** of students and identify the **top performer**.

Requirements:

- Use a function to calculate the average marks.

- Identify the student with the highest average.

- Optional: Implement a `Student` class to handle this logic.

Input Example:

students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}

Expected Output:

Average Marks: {"John": 85, "Alice": 87.33, "Bob": 75}

Top Performer: "Alice"'''

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def average(self):
        return sum(self.marks)/len(self.marks) if self.marks else 0
def calculate_avg(students):
    avgs = {name: Student(name, marks).average() for name, marks in students.items()}
    return avgs
def top_performer(avgs):
    return max(avgs, key=avgs.get)
if __name__ == "__main__":
    students =  {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
    avgs = calculate_avg(students)
    print("Average Marks:", avgs)
    print("Top Performer:", top_performer(avgs))
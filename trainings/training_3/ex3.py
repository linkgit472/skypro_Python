from student import Student
from coursegroup import CourseGroup

student = Student('Михаил', 'Мишин', 21, "Инженер по тестированию")
classmate1 = Student("Иван", "Иванов", 23, "Инженер по тестированию")
classmate2 = Student("Александра", "Смирнова", 34, "Инженер по тестированию")
classmate3 = Student("Екатерина", "Кузнецова", 26, "Инженер по тестированию")
first_group = CourseGroup(student, [classmate1, classmate2, classmate3])

print(first_group)

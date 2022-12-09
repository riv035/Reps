class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average = ()

    def ave_grades(self):
        counter = 0
        for grade in self.grades.values():
            counter += len(self.grades[grade])

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.lec_grades:
                lecturer.lec_grades[course] += [grade]
            else:
                lecturer.lec_grades[course] = [grade]
        else:
            return "Ошибка"

    def ave_rate(self):
        counter = 0
        for grade in self.grades:
            counter += len(self.grades[grade])
        self.average = round(sum(map(sum, self.grades.values())) / counter, 1)
        return self.average

    def __str__(self):
        return f"Имя: {self.name}\n\
Фамилия: {self.surname}\n\
Средняя оценка за домашние задания: {self.average}\n\
Курсы в процессе изучения: {self.courses_in_progress}\n\
Завершенные курсы: {self.finished_courses}"

    def __lt__(self, other: "Student"):
        stud1 = self.average
        stud2 = other.average
        return stud1 < stud2

    def __gt__(self, other: "Student"):
        stud1 = self.average
        stud2 = other.average
        return stud1 > stud2

    def __eq__(self, other: "Student"):
        stud1 = self.average
        stud2 = other.average
        return stud1 == stud2


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lec_grades = {}
        self.lec_average = ()

    def ave_rate_lec(self):
        counter = 0
        for grade in self.lec_grades:
            counter += len(self.lec_grades[grade])
        self.lec_average = round(sum(map(sum, self.lec_grades.values())) / counter, 1)
        return self.lec_average

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.lec_average}"

    def __lt__(self, other: "Lecturer"):
        lec1 = self.lec_average
        lec2 = other.lec_average
        return lec1 < lec2

    def __gt__(self, other: "Lecturer"):
        lec1 = self.lec_average
        lec2 = other.lec_average
        return lec1 > lec2

    def __eq__(self, other: "Lecturer"):
        lec1 = self.lec_average
        lec2 = other.lec_average
        return lec1 == lec2


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


best_student = Student("Peter", "Jackson", "male")
best_student.courses_in_progress += ["Python"]
best_student.courses_in_progress += ["Git"]
best_student.finished_courses += ["Math"]

worst_student = Student("Uwe", "Boll", "male")
worst_student.courses_in_progress += ["Python"]
worst_student.courses_in_progress += ["Git"]
worst_student.finished_courses += ["Math"]

cool_mentor = Reviewer("James", "Gunn")
cool_mentor.courses_attached += ["Python"]
cool_mentor.courses_attached += ["Git"]
cool_mentor.rate_hw(best_student, "Python", 8)
cool_mentor.rate_hw(best_student, "Python", 10)
cool_mentor.rate_hw(best_student, "Git", 10)
cool_mentor.rate_hw(worst_student, "Python", 7)
cool_mentor.rate_hw(worst_student, "Git", 4)
cool_mentor.rate_hw(worst_student, "Git", 7)

good_mentor = Reviewer("Steven", "Spielberg")
good_mentor.courses_attached += ["Python"]
good_mentor.courses_attached += ["Git"]
good_mentor.rate_hw(best_student, "Python", 9)
good_mentor.rate_hw(best_student, "Git", 9)
good_mentor.rate_hw(best_student, "Git", 10)
good_mentor.rate_hw(worst_student, "Python", 5)
good_mentor.rate_hw(worst_student, "Python", 8)
good_mentor.rate_hw(worst_student, "Git", 10)

best_student.ave_rate()
worst_student.ave_rate()

cool_lect = Lecturer("Christopher", "Nolan")
cool_lect.courses_attached += ["Python"]
best_student.rate_lec(cool_lect, "Python", 10)
best_student.rate_lec(cool_lect, "Python", 10)
best_student.rate_lec(cool_lect, "Python", 8)
worst_student.rate_lec(cool_lect, "Python", 7)
worst_student.rate_lec(cool_lect, "Python", 10)
worst_student.rate_lec(cool_lect, "Python", 10)

cool_lect.ave_rate_lec()

good_lect = Lecturer("Stanley", "Kubrick")
good_lect.courses_attached += ["Git"]
best_student.rate_lec(good_lect, "Git", 10)
best_student.rate_lec(good_lect, "Git", 7)
best_student.rate_lec(good_lect, "Git", 8)
worst_student.rate_lec(good_lect, "Git", 9)
worst_student.rate_lec(good_lect, "Git", 9)
worst_student.rate_lec(good_lect, "Git", 10)

good_lect.ave_rate_lec()

stud_list = [best_student, worst_student]
lec_list = [cool_lect, good_lect]


def stud_aver(stud_list, course):
    counter = 0
    total = 0
    for stud in stud_list:
        for marks, val in stud.grades.items():
            if course in marks:
                for k in val:
                    total += k
                    counter += 1
    students_average = round(total / counter, 1)
    return students_average


def lec_aver(lec_list, course):
    counter = 0
    total = 0
    for lec in lec_list:
        for marks, val in lec.lec_grades.items():
            if course in marks:
                for k in val:
                    total += k
                    counter += 1
    lec_average = round(total / counter, 1)
    return lec_average


print(f"Сравнение студентов по среднему баллу:\n\
Средний балл студента {best_student.name} {best_student.surname} ({best_student.average}) \
больше чем у студента {worst_student.name} {worst_student.surname} ({worst_student.average})?\n\
Ответ: {best_student > worst_student}")

print(f"Сравнение лекторов по среднему баллу:\n\
Средний балл лектора {good_lect.name} {good_lect.surname} ({good_lect.lec_average}) \
больше чем у лектора {cool_lect.name} {cool_lect.surname} ({cool_lect.lec_average})?\n\
Ответ: {good_lect > cool_lect}")

print(f"Средняя оценка для всех студентов по курсу Git: {stud_aver(stud_list, 'Git')}")

print(f"Средняя оценка для всех лекторов по курсу Python: {lec_aver(lec_list, 'Python')}")

print(best_student)
print(worst_student)
print(cool_mentor)
print(good_mentor)
print(cool_lect)
print(good_lect)

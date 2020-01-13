physics_students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    physics_students.append([name, score])
physics_students.sort()
N = len(physics_students)
### Removing the lowest grades
grades_list = []
for i in range(N):
    grades_list.append(physics_students[i][1])
grades_list.sort()
min_grade = min(grades_list)
grades_list_temp = grades_list[:]
for i in range(len(grades_list)):
    if grades_list[i] == min_grade:
        grades_list_temp.pop(0)
    else:
        pass
#### Finding out the names of students with second lowest grade
lowest2nd_names_list = []
for i in range(N):
    if physics_students[i][1] == grades_list_temp[0]:
        lowest2nd_names_list.append(physics_students[i][0])

for name in lowest2nd_names_list:
    print(name)



def gradingStudents(grades):
    temp = list()
    for val in grades:
        if val < 38:
            temp.append(val)
        elif val % 5 >= 3:
            temp.append(5 * round(val / 5))
        else:
            temp.append(val)
    return temp


if __name__ == '__main__':
    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)

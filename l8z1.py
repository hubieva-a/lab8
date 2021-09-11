#!/usr/bin/env python3

if __name__ == '__main__':

    students_list = []
    while True:
        command = input("Add, list, exit: ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            last_name = input('Your last name^ ')
            class_name = input('Class ')
            grades = []
            n = 0
            while n < 5:
                grades.append(int(input('Your grades ')))
                n += 1

            student = {
                'Last name': last_name,
                'Class': class_name,
                'Grades': grades,
            }
            students_list.append(student)
            if len(students_list) > 1:
                students_list.sort(key=lambda item: item.get('Last name', ''))

            print(students_list)

        elif command == 'list':
            for index in range(len(students_list)):
                for key in students_list:
                    print(students_list[index][key])





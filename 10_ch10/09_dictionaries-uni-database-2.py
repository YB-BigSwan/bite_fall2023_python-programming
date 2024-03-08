def main():
    db = {}

    insert_degree_program(db, "ITBBA")
    insert_degree_program(db, "EXPER")

    insert_course(db, "ITBBA", ("Python Programming", 5))
    insert_course(db, "ITBBA", ("Time Management", 3))
    insert_course(db, "EXPER", ("Creative Hospitality and Tourism", 5))
    insert_course(db, "EXPER", ("Managing Dynamic Restaurant Business", 10))

    print_degree_program(db, "ITBBA")
    print_degree_program(db, "EXPER")
    print()

    remove_course(db, "ITBBA", "Python Programming")
    print_degree_program(db, "ITBBA")
    print()

    # Testing error handling
    insert_degree_program(db, "ITBBA")
    insert_course(db, "ITBBA", ("Time Management", 3))

    print_degree_program(db, "LOBBY")
    remove_course(db, "COMPU", "Surfing")
    remove_course(db, "ITBBA", "Surfing")

def insert_degree_program(db, degree_program):
    if degree_program in db:
        print(f'{degree_program} is already in the database')

    else:
        db[degree_program] = []

def insert_course(db, degree_program, course):
    course_name, course_credits = course

    for existing_course in db[degree_program]:
        if existing_course[0] == course_name:
            print(f'{course_name} is already in the database')
            return
    
    db[degree_program].append((course))

def print_degree_program(db, degree_program):
    total_credits = 0

    if degree_program in db:
        if len(db[degree_program]) < 2:
            print(f'{degree_program} ({len(db[degree_program])} course)')
        else:
            print(f'{degree_program} ({len(db[degree_program])} courses)')

        for course_name, course_credits in db[degree_program]:
            print(f'  {course_name}, {course_credits} credits')
            total_credits += course_credits
            
        print(f'  Total credits: {total_credits}')

    else:
        print(f'Unknown degree program: {degree_program}')

def remove_course(db, degree_program, course_name):
    if degree_program in db:
        for course in db[degree_program]:

            if course[0] == course_name:
                db[degree_program].remove(course)
                return
            
        print(f'Unknown course: {course_name}')

    else:
        print(f'Unknown degree program: {degree_program}')


if __name__ == '__main__':
    main()

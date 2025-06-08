import sys
from collections import defaultdict

# Task 1: Mapper (Course Name, Grade)
def mapper_course():
    for line in sys.stdin:
        parts = line.strip().split(',')
        if len(parts) == 4:
            course_name = parts[1].strip()
            grade = parts[2].strip()
            print(f"{course_name}\t{grade}")

# Task 1: Reducer (Average Grade per Course + Best Course)
def reducer_course():
    course_grades = defaultdict(list)

    for line in sys.stdin:
        course_name, grade = line.strip().split('\t')
        course_grades[course_name].append(int(grade))

    best_course = None
    best_avg = -1

    for course, grades in course_grades.items():
        avg_grade = sum(grades) / len(grades)
        print(f"{course}, {avg_grade:.2f}")

        if avg_grade > best_avg:
            best_avg = avg_grade
            best_course = course

    print(f"Course with highest average: {best_course} with grade {best_avg:.2f}")
    
#to run the mapper type in terminal cat coursegrades.txt | python map_reduce.py mapper_course > mapped_course_output.txt
#to run the reducer type in terminal cat mapped_course_output.txt | python map_reduce.py reducer_course




# Task 2: Mapper (University Name, Grade)
def mapper_university():
    for line in sys.stdin:
        parts = line.strip().split(',')
        if len(parts) == 4:
            university_name = parts[3].strip()
            grade = parts[2].strip()
            print(f"{university_name}\t{grade}")

# Task 2: Reducer (Average Grade per University + Best University)
def reducer_university():
    university_grades = defaultdict(list)

    for line in sys.stdin:
        university_name, grade = line.strip().split('\t')
        university_grades[university_name].append(int(grade))

    best_university = None
    best_avg = -1

    for university, grades in university_grades.items():
        avg_grade = sum(grades) / len(grades)
        print(f"{university}, {avg_grade:.2f}")

        if avg_grade > best_avg:
            best_avg = avg_grade
            best_university = university

    print(f"Best University: {best_university} with {best_avg:.2f} average grade")

# to run the mapper type in terminal cat coursegrades.txt | python map_reduce.py mapper_university > mapped_university_output.txt
# to run the reducer type in terminal cat mapped_university_output.txt | python map_reduce.py reducer_university



# Task 3: Mapper (Year, Grade)
def mapper_top3_grades():
    for line in sys.stdin:
        parts = line.strip().split(',')
        if len(parts) == 4:
            year = parts[0].strip()
            grade = parts[2].strip()
            print(f"{year}\t{grade}")

# Task 3: Reducer (Top 3 Grades per Year)
def reducer_top3_grades():
    year_grades = defaultdict(list)

    for line in sys.stdin:
        year, grade = line.strip().split('\t')
        year_grades[year].append(int(grade))

    for year, grades in year_grades.items():
        top3_grades = sorted(grades, reverse=True)[:3]
        print(f"{year}, {top3_grades}")

#to run the mapper type in terminal cat coursegrades.txt | python map_reduce.py mapper_top3_grades > mapped_top3_output.txt
#to run the reducer type in terminal cat mapped_top3_output.txt | python map_reduce.py reducer_top3_grades



# Main execution logic
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python map_reduce.py <operation>")
        sys.exit(1)

    operation = sys.argv[1]

    if operation == "mapper_course":
        mapper_course()
    elif operation == "reducer_course":
        reducer_course()
    elif operation == "mapper_university":
        mapper_university()
    elif operation == "reducer_university":
        reducer_university()
    elif operation == "mapper_top3_grades":
        mapper_top3_grades()
    elif operation == "reducer_top3_grades":
        reducer_top3_grades()
    else:
        print("Invalid operation. Use mapper_course, reducer_course, mapper_university, reducer_university, mapper_top3_grades, or reducer_top3_grades.")
        sys.exit(1)


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        number_of_students = len(students)
        print(number_of_students)
        
        flag = False
        running_count = 0
        while (number_of_students != 0):
            student_preference = students[0]
            sandwich_at_the_top_of_the_stack = sandwiches[0]
            
            if student_preference == sandwich_at_the_top_of_the_stack:
                students.pop(0)
                sandwiches.pop(0)
                number_of_students = number_of_students - 1
                running_count = 0
            else:
                students.pop(0)
                students.append(student_preference)
                running_count = running_count + 1
                if running_count == number_of_students:
                    flag = True
                    break
            
            print(f"students queue = {students}")
            print(f"sandwiches stack = {sandwiches}")
            print()
        
        print(f"students queue = {students}")
        print(f"sandwiches stack = {sandwiches}")
        print(f"number_of_students = {number_of_students}")
        print()
        return number_of_students
        
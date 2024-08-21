class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        student = collections.deque(students)
        
        for sandwich in sandwiches:
            if sandwich in student:
                while sandwich != student[0]:
                    value = student.popleft()
                    student.append(value)
                student.popleft()
            else:
                return len(student)

        return 0


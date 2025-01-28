class Solution:
    def __init__(self):
        self.course_map = {}
        self.prereqMap = {}

    def dfs(self, course):
        if course not in self.prereqMap:
            self.prereqMap[course] = set()
            for prereqcourse in self.course_map[course]:
                self.prereqMap[course] = self.prereqMap[course] | self.dfs(prereqcourse)
            self.prereqMap[course].add(course)
        return self.prereqMap[course]

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        for course_number in range(numCourses):
            self.course_map[course_number] = set()

        prerequisites_length = 0
        for a , b in prerequisites:
            # courses b is depended on a
            self.course_map[b].add(a)
            prerequisites_length = prerequisites_length + 1

        if prerequisites_length == 0:
            queries_length = len(queries)
            result = [False] * queries_length
            return result
        
        for course_number in range(numCourses):
            self.dfs(course_number)
        
        result = []
        for u , v in queries:
            if u in self.prereqMap[v]:
                result.append(True)
            else:
                result.append(False)
        return result
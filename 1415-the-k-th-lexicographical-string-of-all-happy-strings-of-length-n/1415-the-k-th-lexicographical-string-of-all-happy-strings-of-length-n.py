class Solution:
    def __init__(self):
        self.n = 1
        self.k = 1
        self.solutions = []
        self.solutions_size = 0

    def recursion(self, string, index):
        if index == self.n:
            # have found a happy string
            self.solutions.append(string.copy())
            self.solutions_size = self.solutions_size + 1
            # print("base condition print -- ", string, self.solutions_size)
            if self.solutions_size == self.k:
                return True
            return False # continue further
        
        last_character = string[index - 1]
        happy_characters = ["a", "b", "c"]

        for character in happy_characters:
            if character != last_character:
                string[index] = character
                # print("for loop print -- ", string, index)
                result = self.recursion(string, (index + 1))
                if result:
                    return True
                string[index] = None

        return False
        
    def getHappyString(self, n: int, k: int) -> str:
        max_possible_strings_that_can_be_formed = 3 ** n
        if k > max_possible_strings_that_can_be_formed:
            return ""
        
        self.n = n
        self.k = k
        character_set = set()
        character_set.add("a")
        character_set.add("b")
        character_set.add("c")
        
        string = [None] * n
        happy_characters = ["a", "b", "c"]
        for starting_character in happy_characters:
            string[0] = starting_character
            result = self.recursion(string, 1)
            if result:
                break
            string[0] = None
        
        # print(self.solutions)
        if self.solutions_size >= k:
            return "".join(self.solutions[-1])
        
        return ""
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        
        ransomNoteCharacterMap = {}
        ransomNoteList = list(ransomNote)
        for char in ransomNoteList:
            if char in ransomNoteCharacterMap:
                ransomNoteCharacterMap[char] = ransomNoteCharacterMap[char] + 1
            else:
                ransomNoteCharacterMap[char] = 1
                
        magazineCharacterMap = {}
        magazineList = list(magazine)
        for char in magazineList:
            if char in magazineCharacterMap:
                magazineCharacterMap[char] = magazineCharacterMap[char] + 1
            else:
                magazineCharacterMap[char] = 1
        
        print(ransomNoteCharacterMap)
        print(magazineCharacterMap)
        
        for char in ransomNoteCharacterMap:
            if char not in magazineCharacterMap:
                return False
            elif ransomNoteCharacterMap[char] > magazineCharacterMap[char]:
                return False
        
        return True
                
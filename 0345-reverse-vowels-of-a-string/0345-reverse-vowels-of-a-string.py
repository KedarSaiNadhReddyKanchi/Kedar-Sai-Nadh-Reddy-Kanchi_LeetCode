class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        start = 0
        end = len(s) - 1
        vowels = ['a' , 'e' , 'i' , 'o' , 'u', 'A' , 'E' , 'I' , 'O' , 'U']
        list_str = list(s)
        # print(list_str)
        flag = 0

        while (start != end) and (start < end):
            if (list_str[start] in vowels) and (list_str[end] in vowels):
                # print(" i am here")
                # print("need to swap - " + list_str[start] + " - and - " + list_str[end])
                temp = list_str[start]
                list_str[start] = list_str[end]
                list_str[end] = temp
                flag = 1
            elif (list_str[start] in vowels) and (list_str[end] not in vowels):
                # end = end - 1
                flag = 3
                # print("moved one element from - " + list_str[end + 1])
            elif (list_str[start] not in vowels) and (list_str[end] in vowels):
                # start = start + 1
                flag = 2
                # print("moved one element from - " + list_str[start - 1])
            else:
                # start = start + 1
                # end = end - 1
                flag = 1
            
            if flag == 1:
                start = start + 1
                end = end -1
            elif flag == 2:
                start = start + 1
            elif flag == 3:
                end = end - 1

        # print(s)
        # print(list_str)

        return ''.join(list_str)

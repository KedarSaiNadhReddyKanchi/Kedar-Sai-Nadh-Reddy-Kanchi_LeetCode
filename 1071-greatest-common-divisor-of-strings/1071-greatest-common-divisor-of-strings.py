class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        # take the lengths of both the strings
        # find the Greatest Common Divisor(GCD) of those lengths
        # then the answer would be a substring of length equal to the GCD value

        # but after you find the gcd and retrieve the substring of length equal to the GCD 
        # you need to iterate and form the strings again to check if the substring forms both
        
        # *******************SOLUTION 1********************************
        # gcd = 1

        # if (len(str1) % len(str2)) == 0:
        #     gcd = len(str2)
        # else: 
        #     for num in range(2,len(str2)):
        #         if (len(str1) % num) == 0 and (len(str2) % num) == 0:
        #             gcd = num

        # if (str1[:gcd] == str2[:gcd]):
        #     # return str2[:gcd]
        #     check_str = ""
        #     for itr in range(len(str2) / gcd):
        #         check_str = check_str + str2[:gcd]
        #     if (str2 == check_str):
        #         check_str = ""
        #         for itr in range(len(str1) / gcd):
        #             check_str = check_str + str2[:gcd]
        #         if (str1 == check_str):
        #             return str2[:gcd]
        #         else:
        #             return ""
        #     else:
        #         return ""
        # else:
        #     return ""

        # *******************SOLUTION 2********************************
        # after going through the solutions I understood that we can only find a greatest common divisor for 2 strings if the resulting strings when they are concatenated together with each other alternatively are both same. 

        if (str1 + str2) != (str2 + str1):
            return ""

        gcd = 1
        if (len(str1) % len(str2)) == 0:
            gcd = len(str2)
        else: 
            for num in range(2,len(str2)):
                if (len(str1) % num) == 0 and (len(str2) % num) == 0:
                    gcd = num
        
        if (str1[:gcd] == str2[:gcd]):
            return str2[:gcd]

        
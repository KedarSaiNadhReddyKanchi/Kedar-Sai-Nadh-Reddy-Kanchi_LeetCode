class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        prev_char = chars[0]
        start = 0
        length = 1
        pos = 1
        while pos < len(chars):
            if chars[pos] == prev_char:
                length = length + 1
                pos = pos + 1
            else:
                end = pos
                prev_char = chars[pos]
                if length > 1:
                    chars[(start + 1) : end] = str(length)
                    start = pos - length + (len(str(length)) + 1)
                    pos = start + 1
                else:
                    start = pos
                    pos = start + 1
                length = 1
        end = len(chars)
        if length > 1:
            chars[(start + 1) : end] = str(length)
        return ( len(chars) )

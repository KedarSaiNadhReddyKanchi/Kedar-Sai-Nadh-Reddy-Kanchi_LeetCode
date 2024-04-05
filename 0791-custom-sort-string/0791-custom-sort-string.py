class Solution:
    def customSortString(self, order: str, s: str) -> str:
        smap = {}
        for key in s:
            if key in smap:
                smap[key] = smap[key] + 1
            else:
                smap[key] = 1
        
        result = []
        for key in order:
            if key in smap:
                newlist = [key] * smap[key]
                result = result + newlist
                del smap[key]
        
        for key in smap:
            newlist = [key] * smap[key]
            result = result + newlist
            
        return "".join(result)
        
        
        
import collections

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dic = collections.OrderedDict()
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dic:
            return -1
        
        # In Python 2.7, use `move_to_end` equivalent logic
        value = self.dic[key]
        del self.dic[key]
        self.dic[key] = value
        
        return value
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dic:
            del self.dic[key]
        
        self.dic[key] = value
        if len(self.dic) > self.capacity:
            self.dic.popitem(last=False)

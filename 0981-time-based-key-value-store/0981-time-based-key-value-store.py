class TimeMap:

    def __init__(self):
        self.runningObject = {}
        
#     def bubbleSort(self , key , timestampInQuestion):
#         start = 0
#         end = len(self.runningObject[key]["previous_timestamps"])
#         temp = end
#         nearest_timestamp = None
#         while start <= end:
#             mid = int((start + end) / 2)
#             if mid >= temp:
#                 break
#             recorded_timestamp = self.runningObject[key]["previous_timestamps"][mid]
#             if  recorded_timestamp > timestampInQuestion:
#                 end = mid - 1
#             else:
#                 start = mid + 1
#                 nearest_timestamp = recorded_timestamp
        
#         return nearest_timestamp
    
    def linearSearch(self, key , timestampInQuestion):
        highestpossibleTimeStamp = None
        for timestamp in self.runningObject[key]["previous_timestamps"]:
            if timestamp < timestampInQuestion:
                if highestpossibleTimeStamp == None:
                    highestpossibleTimeStamp = timestamp
                else:
                    if timestamp > highestpossibleTimeStamp:
                        highestpossibleTimeStamp = timestamp
        return highestpossibleTimeStamp

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.runningObject:
            self.runningObject[key] = {
                timestamp : value,
                "timestamp_prev" : timestamp,
                "previous_timestamps": [timestamp]
            }
        else:
            last_largest_time_stamp_prev = self.runningObject[key]["timestamp_prev"]
            if timestamp > last_largest_time_stamp_prev:
                self.runningObject[key]["timestamp_prev"] = timestamp
            self.runningObject[key][timestamp] = value
            self.runningObject[key]["previous_timestamps"].append(timestamp) 
            # self.runningObject[key]["previous_timestamps"] = sorted(self.runningObject[key]["previous_timestamps"])
            

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.runningObject:
            return ""
        else:
            if timestamp not in self.runningObject[key]:
                
                if self.runningObject[key]["timestamp_prev"] <= timestamp:
                    value = self.runningObject[key]["timestamp_prev"] 
                    return self.runningObject[key][value]
                
                # timestampToReturn = self.bubbleSort(key , timestamp)
                timestampToReturn = self.linearSearch(key , timestamp)
                if (timestampToReturn != None) and (timestampToReturn <= timestamp):
                    return self.runningObject[key][timestampToReturn]
                else:
                    return ""
            else:
                return self.runningObject[key][timestamp]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
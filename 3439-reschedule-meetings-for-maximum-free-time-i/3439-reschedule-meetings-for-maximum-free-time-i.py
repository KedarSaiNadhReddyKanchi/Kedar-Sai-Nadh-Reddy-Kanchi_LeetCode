class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        # in order to maximize the gap time, we need to make sure that all the meetings are as close as possible. 
        # therefore, if deciding to reschedule meetings for better gap time then it is better to
            # reschedule (k) consecutive meetings in order to maximize the complete gap time
            # by covering all the intermediary gap times. 

        
        gaps = []
        prev_end_time = 0 # initial event start time
        number_of_gaps = 0
        for start , end in zip(startTime , endTime):
            gap = start - prev_end_time
            gaps.append(gap)
            prev_end_time = end
            number_of_gaps = number_of_gaps + 1
        # adding the gap post the completion of all the meetings
        gap = eventTime - endTime[-1]
        gaps.append(gap)
        number_of_gaps = number_of_gaps + 1

        currentMaxGapTime = 0
        for position in range(k + 1):
            currentMaxGapTime = currentMaxGapTime + gaps[position]
        
        max_gap_time = currentMaxGapTime
        for position in range(k + 1 , number_of_gaps):
            currentMaxGapTime = currentMaxGapTime + gaps[position] - gaps[position - (k + 1)]
            max_gap_time = max(max_gap_time , currentMaxGapTime)
        
        return max_gap_time



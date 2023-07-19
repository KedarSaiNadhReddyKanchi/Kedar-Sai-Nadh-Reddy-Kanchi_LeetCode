class Solution:
    
    def __init__(self):
        self.adjacencyList = {}
        # initialising the results array to JFK because as per the problem description the itinerary must begin with "JFK". 
        self.results = ["JFK"]
        self.length_of_the_given_input = None
    
    def createAdjacencyList(self, tickets):
        for start , end in tickets:
            if start in self.adjacencyList:
                self.adjacencyList[start].append(end)
            else:
                self.adjacencyList[start] = [end]
     
    # ***************** this can be one more way of creating the adjacency list in the sorted order - where you create the adjacency list first from the given input and then sort the complete adjacency list for each node. 
    # ***** but this method takes a lot of time for larger inputs because this has a time complexity of O(n^2) as we have to first loop through each node in the adjacency list and then perform a sorting operation on the respective list which is O(n). 
    # ******* therefore loop with sorting in each iteration becomes O(n^2) and so it is better to sort the input list first which takes only O(n) time and then create the adjacency list.
    # def sortAdjacencyList(self):
    #     for city in self.adjacencyList:
    #         if len(self.adjacencyList[city]) > 1:
    #             self.adjacencyList[city] = sorted(self.adjacencyList[city])
                
    def formItinerary(self , city):
        
        if len(self.results) == (self.length_of_the_given_input + 1):
            return True
            # that is because at this point, we have covered all the edges present in the input graph and so we have constructed a complete valid itenary.
        
        if city not in self.adjacencyList:
            return False
            # this means that there are no outgoing edges from the current city
            # so we need to backtrack from this particualr position 
            # and then we need to traverse the next smallest lexicographically smallest city
        
        # creating a copy of the adjacency list fot the current city
        # because we would be making modifications to the adjacency list
        # and so it would not be good to make modifications on the original adjacency list
        # therfore, creating a temporary copy and making the modifications on it would be the ideal choice in this case
        temp = list(self.adjacencyList[city])
        
        for index , connectingCity in enumerate(temp):
            self.adjacencyList[city].pop(index)
            self.results.append(connectingCity)
            
            if self.formItinerary(connectingCity):
                return True
                # at this point if we are returned True then that means
                # that this True as been returned from the 1st if condition in this function
                # and this means that we have successfully reconstructed a valid itenary
            
            # but if the above if condition is not executed then that means 
            # the function has been returned False
            # that means it is from the 2nd if condition from this function
            # which means that we have visited a city which does not have any outgoing edges
            # so now we need to backtrack from this position i.e go back on this edge
            # and then traverse the next lexicographically smallest edge
            
            # therefore STEP 1 : insert back the popped city from the adjacency List
            self.adjacencyList[city].insert(index , connectingCity)
            
            # STEP 2 : remove the added city from the result path
            self.results.pop()
            
        return False
            
    def sortGivenInput(self, tickets):
        # this is because as per the description we need to return the output which has the smallest lexical order when read as a single string. 
        # so before creating my adjacency list it is better to sort the given input
        # so that we can create the adjacency list in the sorted order itself
        
        # key is set to sort using second element of tickets
        # that meanbs if the first key is repeated multiple times then 
        # the sorting is done on the basis of the second key
        tickets.sort(key = lambda x: x[1])
        return tickets
    
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        sorted_tickets = self.sortGivenInput(tickets)
        self.createAdjacencyList(sorted_tickets)
        
        self.length_of_the_given_input = len(sorted_tickets)
        pathFound = self.formItinerary("JFK")
        
        return self.results
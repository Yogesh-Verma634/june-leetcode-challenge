class Solution:
   #city -> List[List[int]]
    def twoCitySchedCost(self, costs):
        output = 0
        
        '''
        sort the costs by the difference between the cost of two cities and minimize the CTC
        send first half candidates to city A and other half to city B
        '''
        costs = sorted(costs, key = lambda x: x[0] - x[1])
        half = len(costs)//2
                
        for i in range(half):
            output += costs[i][0] + costs[i+half][1]
    
        return output

costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
solution = Solution()
print(solution.twoCitySchedCost(costs))

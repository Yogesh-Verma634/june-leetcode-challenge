class Solution:
    #people: List[List[int]]
    def reconstructQueue(self, people):
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        output = []
        
        for person in people:
            output.insert(person[1], person)
        
        return output

solution = Solution()
queue = [[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]]
print(solution.reconstructQueue(queue))
# precondition; list of integers 
# postcondition; return true or false 

# divide: recur along smaller list. pop first array 
# conquer: compare current value with the rest of the entire list 

# that seems expensive, because for every value, we must check the rest of the list
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums: # O(n)
            if num in seen: # takes O(1) to compare 
                return True
            else: seen.add(num) # set is built as we search. 
        return False

            

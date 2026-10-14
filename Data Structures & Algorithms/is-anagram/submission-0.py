class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_table_s = {}
        for letter in s: 
            hash_table_s[letter] = hash_table_s.get(letter, 0) + 1
        hash_table_t = {}
        for letter in t: 
            hash_table_t[letter] = hash_table_t.get(letter, 0) + 1
        if hash_table_t == hash_table_s: return True
        else: return False 
            
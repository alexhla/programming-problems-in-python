class Solution:
    def lengthOfLongestSubstring(self, s):
        i = 0
        j = 0
        
        charmap = set()
        count = 0
        answer = 0
        
        while i < len(s) and j < len(s):
            
            if s[j] not in charmap:
                charmap.add(s[j])
                count += 1
                j += 1
            else:
                charmap.discard(s[i])
                i += 1
                count -= 1
                
            answer = max(answer,count)
            
        return answer
        

obj = Solution()
s1 = "pwwakewkkgg"
print("Longest Substring without Repeats in: {}" .format(s1))
print("Answer: {}" .format(obj.lengthOfLongestSubstring(s1)))
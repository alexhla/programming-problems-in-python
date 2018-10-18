class Solution:
    def myAtoi(self, s):

        if not s:
            return 0
        
        s.strip() # remove leading, trailing spaces
        l = s.split()
        print(l)
        if not l:
            return 0
        
        chars = l[0]
        sign = 1
        
        if chars[0] == '+' or chars[0] == '-':
            
            if len(chars) == 1: # only a single + or - with no numbers
                return 0
            
            count = 0
            for ch in chars:
                if ch == '+' or ch == '-':
                    count += 1
                else:
                    break
            
            if count >= 2:
                return 0
            if count == 1:    
                sign = 1 if chars[0]=='+' else -1
                chars = chars[1:]

        
        strnum = ''
        for ch in chars:
            if ch.isdigit() or ch == '.':
                strnum += ch
            else:
                break
                
        if not strnum:
            return 0
        
        num = int(float(strnum))

        answer = sign * num
        
        if answer >= 2147483648:
            answer = 2147483647
            
        if answer <= -2147483648:
            answer = -2147483648
            
        return answer

obj = Solution()
n = "-9434x.35"
print("String '{}' to Integer..." .format(n))
print("Answer: {}" .format(obj.myAtoi(n)))
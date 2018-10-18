class Solution:
    def myAtoi(self, s):

        if not s:  # empty string
            return 0
        
        s.strip() # remove leading, trailing spaces
        l = s.split() # split along default delimiter which is space 
        
        if not l:  # edge case: l contains nothing
            return 0
        
        chars = l[0] # take only first grouping of characters
        sign = 1
        
        if chars[0] == '+' or chars[0] == '-':
            
            if len(chars) == 1: # only a single + or - with no numbers
                return 0
            
            count = 0
            for ch in chars: # edge case: multiple signs +- | -+ | ++ | --
                if ch == '+' or ch == '-':
                    count += 1
                else:
                    break
                    
            if count >= 2:  # multiple signs invalid
                return 0
            if count == 1:    
                sign = 1 if chars[0]=='+' else -1  # save sign as an integer
                chars = chars[1:]  # discard sign from string

        
        strnum = ''
        for ch in chars:  # iterate over string keeping only digits and periods
            if ch.isdigit() or ch == '.':
                strnum += ch
            else:
                break  # stop on a non-digit, effectively discarding remaining characters
                
        if not strnum:  # if first character was a letter
            return 0
        
        num = int(float(strnum))  # call float() first for the cases with fractional numbers (3.0, 3.14, etc.)

        answer = sign * num  # apply sign
        
        if answer >= 2147483648:  # check for overflow
            answer = 2147483647       
        elif answer <= -2147483648:
            answer = -2147483648
            
        return answer

obj = Solution()
n = "-9434x.35"
print("String '{}' to Integer..." .format(n))
print("Answer: {}" .format(obj.myAtoi(n)))
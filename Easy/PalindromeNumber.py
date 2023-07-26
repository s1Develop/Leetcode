class Solution:
    def isPalindrome(self, x: int) -> bool:

        # if negative, false anyway
        if x<0:
            return False
        
        #copy the given integer to temp
        temp = x

        #initialize reverse_num
        reverse_num = 0

        while temp != 0:

            # last digit of temp
            last_digit = temp % 10 

            # reverse current number
            reverse_num = (reverse_num * 10) + last_digit

            # remove last digit from the number
            temp = temp // 10        

        # check if what we reverse is same as the original number
        return x == reverse_num
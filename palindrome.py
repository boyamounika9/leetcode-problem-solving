class Solution:
    def isPalindrome(self, x: int) -> bool:
        # t=bool("true")
        # f=bool("false")
        temp=x
        reverse=0
        if x<0:
            return False
        while x!=0:
            digit=x%10
            reverse=reverse*10+digit
            x//=10
        if temp==reverse:
            return True 
        else:
            return False
s=Solution()
s.isPalindrome(121)
s.isPalindrome(-121)
s.isPalindrome(10)
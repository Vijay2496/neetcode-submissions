class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([char for char in s if char.isalnum()])
        read=0
        write=len(s)-1
        while read<write:
            if(s[read].casefold()==s[write].casefold()):
                read+=1
                write-=1
            else:
                return False

        return True
        
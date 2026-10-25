class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashh={}
        trash={}

        for i in s:
            if i not in hashh:
                hashh[i]=1
            else:
                x=hashh[i]
                hashh[i]=x+1

        for j in t:
            if j not in trash:
                trash[j]=1
            else:
                y=trash[j]
                trash[j]=y+1

        if(hashh==trash):
            return True
        else:
            return False

    
class Solution:
    def last_word_sentence(self,s:str)->int:
        s=s.split()
        return (s[-1])

    


s=input()
obj1=Solution()
result=obj1.last_word_sentence(s)
print(result)

# coding: utf-8

# In[ ]:


#원판의 갯수와 옮기는 횟수 도출 함수
# n = 원판의 갯수, numofmove(n) = 원판을 옮기는 총 횟수
def numofmove(n):
    a = 0
    for i in range(0,n):
        a = a + 2**i
    return a
numofmove(5)


# In[ ]:


#원판의 갯수와 옮기는 과정 도출 함수
#n = 원판의 갯수, hanoiRecursive(n) = 원판을 옮기는 과정

#너무 어려워서 결국 풀지 못했습니다. 이후 다시 도전해보도록 하겠습니다.
#첨부된 코드는 외부 블로그에서 긁어온 자료입니다.(http://abh0518.net/tok/?p=523)

def hanoiRecursive(ndisks, startPeg=1, endPeg=3):
    global phase
    if ndisks:
        extraPeg = 6 - endPeg - startPeg
        hanoiRecursive(ndisks-1, startPeg, extraPeg)
        print(startPeg, "번 기둥의", ndisks, "번 원반을", endPeg, "번 기둥에 옮깁니다.")
        hanoiRecursive(ndisks-1, extraPeg , endPeg)
hanoiRecursive(5)


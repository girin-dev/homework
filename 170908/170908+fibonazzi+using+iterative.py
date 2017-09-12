
# coding: utf-8

# In[10]:


#fibonazzi using iterative
#하다가 결국 완성 못했습니다...

def f(n):
    if n == 0:
        return 1
    else:
        a = 0
        while a == n:
            a = a + 1
            m = n - a
            return f(m)+f(m-1)
f(3)


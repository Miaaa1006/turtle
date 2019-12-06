#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import turtle as t
def main():
    t.fillcolor("yellow") #颜色填充为黄色
    t.begin_fill()
    j = 1
    while j <= 5:
        t.forward(100)   #向前走50
        t.right(144)    #向右转144度
        j = j + 1
    t.end_fill()
    t.exitonclick()

if __name__ == "__main__" :
    main()


# In[ ]:





# In[ ]:





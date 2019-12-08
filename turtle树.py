#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import turtle as t
def draw_branch(branch_length):
    if branch_length >= 5:
        #绘制右侧树枝
        t.forward(branch_length)
        t.right(20)
        draw_branch(branch_length - 5)

        #绘制左侧树枝
        t.left(40)
        draw_branch(branch_length - 5)

        #返回根节点
        t.right(20)
        if branch_length <= 5:
            t.pencolor("red")
        else:
            t.pencolor("yellow")
        t.backward(branch_length)


def main():
    t.penup()
    t.backward(50)
    t.pendown()
    t.left(90)
    draw_branch(50)
    t.exitonclick()

if __name__ == "__main__" :
    main()

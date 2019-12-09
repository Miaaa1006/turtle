#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import turtle as t
def draw_branch(branch_length):
    if branch_length >= 6:
        #绘制右侧树枝
        t.forward(branch_length)
        t.right(30)
        draw_branch(branch_length - 6)

        #绘制左侧树枝
        t.left(60)
        draw_branch(branch_length - 6)

        #返回根节点
        t.right(30)
        if branch_length <= 10:
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

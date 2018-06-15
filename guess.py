# 用于生成随机数的模块
import random
# 用于窗口的模块
import tkinter as t

"""
猜数字游戏

窗口内按下生成则开始游戏，猜一个1-100的随机整数。
共有5次机会，机会用尽则游戏失败。
"""


# 生成随机数函数
def getNum():
    # 将随机数num设定为全局变量（global），因为在另一个函数guess中还要用到
    global num
    # 在1到10间随机生成一个整数
    num = random.randint(1, 100)
    # count：对猜数次数进行计数，共有五次机会；因为这个变量要在两个函数内使用，所以设置为全局变量（global）
    global count
    # 共有五次机会
    count = 5
    # 修改提示标签tip_count的文字内容
    tip_count.config(text='你有5次机会。')
    # 修改提示标签tip的文字内容
    tip.config(text='猜一猜？')


# 猜数字函数：pd输入的数字是否为函数getNum中生成的随机数num
def guess():
    # choice.get()：获取文本框内文字choice
    # 因为文本框获取的内容默认为字符串str，字符串无法与数字比较，所以这里将获取的内容强制转换为整型int型
    guess_num = int(choice.get())
    # 设置全局变量（global）count，注：这里的count与函数getNum中count为同一变量
    global count
    # 更新剩余游戏次数
    count = count - 1
    # pd是否能够继续进行游戏 游戏次数大于0则可以进行游戏
    if count > 0:
        # pd是否猜对，并更改提示标签的文字
        if guess_num < num:
            tip.config(text='猜小了')
        elif guess_num > num:
            tip.config(text='猜大了')
        # 大小相同则为猜对
        if guess_num == num:
            tip.config(text='猜对了！')
        # 更改提示次数标签的文字
        tip_count.config(text='你还有' + str(count) + '次机会。')
    else:
        # 若游戏次数小于或等于0，则游戏失败
        # 更改提示次数标签的文字
        tip_count.config(text='机会用尽。')
        # 更改提示标签的文字，显示游戏失败
        tip.config(text='游戏失败！')


# 窗口定义部分


# 创建窗口对象
window = t.Tk()
# 标题
window.title('猜数字')
# 窗口大小
window.minsize(400, 150)

# 标签
title = t.Label(window, text='～猜数字～')
# 放置标签
title.pack()

# 提示次数（标签）
tip_count = t.Label(window, text='')
# 放置
tip_count.pack()

# 提示文字（标签）
tip = t.Label(window, text='按下按钮，开始生成随机整数\t\t\t')
# 放置
tip.pack()

# 输入框：输入猜的数字
#  绑定tkinter.StringVar()
choice = t.StringVar()
# 设定内容
choice.set('')
# 创建输入框，宽度为40，文字内容绑定为choice
c = t.Entry(window, width=40, textvariable=choice)
# 放置
c.pack()

# 生成按钮
b = t.Button(text='生成', command=getNum)
# 放置
b.pack()

# 确认按钮
confirm = t.Button(text='确定', command=guess)
# 放置
confirm.pack()

# 显示窗口
window.mainloop()

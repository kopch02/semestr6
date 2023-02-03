import tkinter
import math

a = 260
h = int(a/2 * math.sqrt(3))

R = 150
R2 = 75

center = [130,75]

print(h)

def triangel_del():
    canvas.delete(t)


def triangel():
    global canvas, t,h,a
    t = canvas.create_polygon(0,
                              0,
                              a,
                              0,
                              a/2,
                              h,
                              0,
                              0,
                              fill="white",
                              outline='black')
    canvas.move(t, 100, 100)
    canvas.create_oval(center[0]+98,center[1]+98,center[0]+102,center[1]+102,fill = "green")



def left():
    global canvas, t,h,a

    canvas.delete(t)
    f = math.asin(175/R)
    x1 = math.cos(f) * R
    y1 = math.sin(f) * R

    f = math.asin(175/R)
    x2 = math.cos(f) * R
    y2 = math.sin(f) * R

    f = math.asin(325/R)
    x3 = math.cos(f) * R
    y3 = math.sin(f) * R

    print(x1,y1)
    print(x2,y2)
    print(x3,y3)

    t = canvas.create_polygon(0,
                              0,
                              a,
                              0,
                              a/2,
                              h,
                              0,
                              0,
                              fill="white",
                              outline='black')
    canvas.move(t, 100, 100)


def right():
    canvas.delete(t)
    t = canvas.create_polygon(0,
                              0,
                              a,
                              0,
                              a/2,
                              h,
                              0,
                              0,
                              fill="white",
                              outline='black')
    canvas.move(t, 100, 100)


t = tkinter.Tk()

canvas = tkinter.Canvas(t, height=480, width=640)
canvas.pack()

b1 = tkinter.Button(t, text="треугольник", command=triangel)
bd1 = tkinter.Button(t, text="удалить треугольник", command=triangel_del)

b_left = tkinter.Button(t, text="<-", command=left)
b_right = tkinter.Button(t, text="->", command=right)

b_left.place(x=50, y=490)
b_right.place(x=80, y=490)




b1.pack()
bd1.pack()

t.mainloop()
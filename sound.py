import turtle as t
from colormap import rgb2hex
import base64

enc = base64.b64encode(open("sound.mp3", "rb").read())
code=""
for e in enc:
    code+=str(e)
filling=False
code_arr=list(code)
t.speed(0)
for symb in code_arr:
    t.color(rgb2hex(int(code_arr[code_arr.index(symb)-1])*20,int(symb)*20,int(code_arr[code_arr.index(symb)+1])*20))

    #if (code_arr.index(symb)%300==0):
        #t.goto(int(code_arr[code_arr.index(symb)-1])*3,int(code_arr[code_arr.index(symb)+1])*3)
    t.goto(int(code_arr[code_arr.index(symb)-1])*3,int(code_arr[code_arr.index(symb)+1])*3)
    t.right(code_arr.index(symb))
    t.forward(int(symb)*20)
    t.right(int(symb)*-11)#убрать минус у 11 потом
    t.forward(int(symb)**2)
    if (code_arr.index(symb)%5==0):
        if (not filling):
            t.begin_fill()
            filling=True
    if (code_arr.index(symb)%3==0):
        if (filling):
            filling=False
            t.end_fill()
        
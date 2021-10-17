import turtle as t
import math
import random
from colormap import rgb2hex
import base64

enc = base64.b64encode(open("sound.mp3", "rb").read())
code=""
for e in enc:
    code+=str(e)
filling=False
code_arr=list(code)
t.speed(0)
i = 0
t.pensize(5)
for symb in code_arr:
    i+=1
    t.color(rgb2hex(int(code_arr[code_arr.index(symb)-1])*20,int(symb)*20,int(code_arr[code_arr.index(symb)+1])*20))

    t.goto((int(symb)+1)*9,(int(symb)+1)*9)
    t.right((int(symb)+random.randint(1, 20))*20)
    t.forward((int(symb)+1)*27)
    if (i%2==0):
        if (not filling):
            t.begin_fill()
            filling=True
    if (i%3==0):
        if (filling):
            filling=False
            t.end_fill()

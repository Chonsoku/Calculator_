import tkinter as tk

font = ('Courier', 78)
root = tk.Tk()
res = tk.Label(root, font=font, text='0')
res.grid(row=0, column=0)
vvod = tk.Label(root, font=font, text='')
vvod.grid(row=1, column=0)
container = tk.Frame(root)
container.grid(row=2, column=0)


def zerofunction():
    vvod["text"] += '0'


butty0 = tk.Button(container, font=font, text='0', command=zerofunction)
butty0.grid(row=4, column=2)


def onefunction():
    vvod['text'] += '1'


butty1 = tk.Button(container, font=font, text='1', command=onefunction)
butty1.grid(row=1, column=1)


def twofunction():
    vvod['text'] += '2'


butty2 = tk.Button(container, font=font, text='2', command=twofunction)
butty2.grid(row=1, column=2)


def threefunction():
    vvod['text'] += '3'


butty3 = tk.Button(container, font=font, text='3', command=threefunction)
butty3.grid(row=1, column=3)


def fourfunction():
    vvod['text'] += '4'


butty4 = tk.Button(container, font=font, text='4', command=fourfunction)
butty4.grid(row=2, column=1)


def fivefunction():
    vvod['text'] += '5'


butty5 = tk.Button(container, font=font, text='5', command=fivefunction)
butty5.grid(row=2, column=2)


def sixfunction():
    vvod['text'] += '6'


butty6 = tk.Button(container, font=font, text='6', command=sixfunction)
butty6.grid(row=2, column=3)


def sevenfunction():
    vvod['text'] += '7'


butty7 = tk.Button(container, font=font, text='7', command=sevenfunction)
butty7.grid(row=3, column=1)


def eightfunction():
    vvod["text"] += '8'


butty8 = tk.Button(container, font=font, text="8", command=eightfunction)
butty8.grid(row=3, column=2)


def ninefunction():
    vvod["text"] += '9'


butty9 = tk.Button(container, font=font, text="9", command=ninefunction)
butty9.grid(row=3, column=3)


def multiplicationfunction():
    res["text"] = float(res['text']) * float(vvod['text'])


buttymultiplication = tk.Button(container, font=font, text='*', command=multiplicationfunction)
buttymultiplication.grid(row=3, column=4)


def additionfunction():
    res['text'] = float(res['text']) + float(vvod['text'])
    vvod['text'] = ''


buttyaddition = tk.Button(container, font=font, text="+", command=additionfunction)
buttyaddition.grid(row=1, column=4)


def subtractionfunction():
    res['text'] = float(res['text']) - float(vvod['text'])
    vvod['text'] = ''


buttysubtraction = tk.Button(container, font=font, text="-", command=subtractionfunction)
buttysubtraction.grid(row=2, column=4)


def divisionfunction():
    res['text'] = float(res['text']) // float(vvod['text'])
    vvod['text'] = ''


buttydivision = tk.Button(container, font=font, text='/', command=divisionfunction)
buttydivision.grid(row=4, column=4)


def pointfunction():
    vvod['text'] += '.'


buttypoint = tk.Button(container, font=font, text='.', command=pointfunction)
buttypoint.grid(row=4, column=3)

def deletefunction():
    vvod['text'] = ''


buttyDEL = tk.Button(container, font=('Courier', 42), text='DEL', command=deletefunction)
buttyDEL.grid(row=4, column=1)

root.mainloop()
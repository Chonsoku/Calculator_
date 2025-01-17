import tkinter as tk

font = ('Courier', 78)
root = tk.Tk()
res = tk.Label(root, font=font, text='0')
res.grid(row=0, column=0)
vvod = tk.Label(root, font=font, text='')
vvod.grid(row=1, column=0)
container = tk.Frame(root)
container.grid(row=2, column=0)

def update_display(value):
    vvod["text"] += str(value)

def create_button(text, command, row, column, width=5, height=2):
    button = tk.Button(container, font=font, text=text, command=command, width=width, height=height)
    button.grid(row=row, column=column)

def zerofunction():
    update_display(0)
def onefunction():
    update_display(1)
def twofunction():
    update_display(2)
def threefunction():
    update_display(3)
def fourfunction():
    update_display(4)
def fivefunction():
    update_display(5)
def sixfunction():
    update_display(6)
def sevenfunction():
    update_display(7)
def eightfunction():
    update_display(8)
def ninefunction():
    update_display(9)

def multiplicationfunction():
    global last_operation
    last_operation = '*'
    last_value = float(vvod['text']) if vvod['text'] else 0
    res["text"] = str(float(res["text"]) * last_value)
    vvod['text'] = ''

def additionfunction():
    global last_operation
    last_operation = '+'
    last_value = float(vvod['text']) if vvod['text'] else 0
    res["text"] = str(float(res["text"]) + last_value)
    vvod['text'] = ''

def subtractionfunction():
    global last_operation
    last_operation = '-'
    last_value = float(vvod['text']) if vvod['text'] else 0
    res["text"] = str(float(res["text"]) - last_value)
    vvod['text'] = ''

def divisionfunction():
    global last_operation
    last_operation = '/'
    last_value = float(vvod['text']) if vvod['text'] else 1
    if last_value != 0:
        res["text"] = str(float(res["text"]) / last_value)
    vvod['text'] = ''

def pointfunction():
    if '.' not in vvod['text']:
        vvod['text'] += '.'
def deletefunction():
    res['text'] = '0'


create_button('0', zerofunction, 4, 2)
create_button('1', onefunction, 1, 1)
create_button('2', twofunction, 1, 2)
create_button('3', threefunction, 1, 3)
create_button('4', fourfunction, 2, 1)
create_button('5', fivefunction, 2, 2)
create_button('6', sixfunction, 2, 3)
create_button('7', sevenfunction, 3, 1)
create_button('8', eightfunction, 3, 2)
create_button('9', ninefunction, 3, 3)
create_button('*', multiplicationfunction, 3, 4)
create_button('+', additionfunction, 1, 4)
create_button('-', subtractionfunction, 2, 4)
create_button('/', divisionfunction, 4, 4)
create_button('.', pointfunction, 4, 3)
create_button('DEL', deletefunction, 4, 1, width=42, height=2)

root.mainloop()
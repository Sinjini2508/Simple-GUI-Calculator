import tkinter

window = tkinter.Tk()

window.title('Calculator')
window.wm_iconbitmap(
    'C:\\Users\\Sinjini\\Downloads\\3700465-business-calculating-calculator-finance-maths-technological_108748.ico')


def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


def backspace():
    global expression
    expression = expression[:-1]
    input_text.set(expression)


def btn_clear():
    global expression
    expression = ''
    input_text.set(expression)


def btn_equal():
    global expression
    expression = str(eval(expression))
    input_text.set(expression)


expression = ''
input_text = tkinter.StringVar()

input_frame = tkinter.Frame(window, width=312, height=100, bd=0)
input_frame.pack(side =tkinter.TOP)

input_field = tkinter.Entry(input_frame, font=('Times New Roman', 30, 'bold'), textvariable=input_text)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

btns_frame = tkinter.Frame(window, width=300, height=250, bg='black')
btns_frame.pack()

clear = tkinter.Button(btns_frame, text='C', bd=0, command=btn_clear, height=5, width=22, font=('Times New Roman', 15))
clear.grid(row=1, column=0, columnspan=2, padx=1, pady=1, sticky='nesw')

back = tkinter.Button(btns_frame, text='Backspace', bd=0, command=lambda: backspace(), height=5, width=10,
                      font=('Times New Roman', 15))
back.grid(row=1, column=2, padx=1, pady=1, sticky='nesw')

div = tkinter.Button(btns_frame, text='/', bg='Yellow', fg='Black', command=lambda: btn_click('/'), height=5, width=10,
                     font=('Times New Roman', 15))
div.grid(row=1, column=3, padx=1, pady=1, sticky='nesw')

seven = tkinter.Button(btns_frame, text='7', command=lambda: btn_click('7'), height=5, width=10,
                       font=('Times New Roman', 15))
seven.grid(row=2, column=0, padx=1, pady=1, sticky='nesw')

eight = tkinter.Button(btns_frame, text='8', command=lambda: btn_click('8'), height=5, width=10,
                       font=('Times New Roman', 15))
eight.grid(row=2, column=1, padx=1, pady=1, sticky='nesw')

nine = tkinter.Button(btns_frame, text='9', command=lambda: btn_click('9'), height=5, width=10,
                      font=('Times New Roman', 15))
nine.grid(row=2, column=2, padx=1, pady=1, sticky='nesw')

mult = tkinter.Button(btns_frame, text='*', bg='Yellow', fg='Black', command=lambda: btn_click('*'), height=5, width=10,
                      font=('Times New Roman', 15))
mult.grid(row=2, column=3, padx=1, pady=1, sticky='nesw')

four = tkinter.Button(btns_frame, text='4', command=lambda: btn_click('4'), height=5, width=10,
                      font=('Times New Roman', 15))
four.grid(row=3, column=0, padx=1, pady=1, sticky='nesw')

five = tkinter.Button(btns_frame, text='5', command=lambda: btn_click('5'), height=5, width=10,
                      font=('Times New Roman', 15))
five.grid(row=3, column=1, padx=1, pady=1, sticky='nesw')

six = tkinter.Button(btns_frame, text='6', command=lambda: btn_click('6'), height=5, width=10,
                     font=('Times New Roman', 15))
six.grid(row=3, column=2, padx=1, pady=1, sticky='nesw')

minus = tkinter.Button(btns_frame, text='-', bg='Yellow', fg='Black', command=lambda: btn_click('-'), height=5,
                       width=10, font=('Times New Roman', 15))
minus.grid(row=3, column=3, padx=1, pady=1, sticky='nesw')

one = tkinter.Button(btns_frame, text='1', command=lambda: btn_click('1'), height=5, width=10,
                     font=('Times New Roman', 15))
one.grid(row=4, column=0, padx=1, pady=1, sticky='nesw')

two = tkinter.Button(btns_frame, text='2', command=lambda: btn_click('2'), height=5, width=10,
                     font=('Times New Roman', 15))
two.grid(row=4, column=1, padx=1, pady=1, sticky='nesw')

three = tkinter.Button(btns_frame, text='3', command=lambda: btn_click('3'), height=5, width=10,
                       font=('Times New Roman', 15))
three.grid(row=4, column=2, padx=1, pady=1, sticky='nesw')

plus = tkinter.Button(btns_frame, text='+', bg='Yellow', fg='Black', command=lambda: btn_click('+'), height=5, width=10,
                      font=('Times New Roman', 15))
plus.grid(row=4, column=3, padx=1, pady=1, sticky='nesw')

zero = tkinter.Button(btns_frame, text='0', command=lambda: btn_click('0'), height=5, width=10,
                      font=('Times New Roman', 15))
zero.grid(row=5, column=0, padx=1, pady=1, sticky='nesw')

point = tkinter.Button(btns_frame, text='.', command=lambda: btn_click('.'), height=5, width=10,
                       font=('Times New Roman', 15))
point.grid(row=5, column=1, padx=1, pady=1, sticky='nesw')

mod = tkinter.Button(btns_frame, text='% (Modulus)', command=lambda: btn_click('%'), height=5, width=10, bg='yellow',
                     font=('Times New Roman', 15))
mod.grid(row=5, column=2, padx=1, pady=1, sticky='nesw')

equal = tkinter.Button(btns_frame, text='=', bg='Yellow', fg='Black', command=btn_equal, height=5, width=10,
                       font=('Times New Roman', 15))
equal.grid(row=5, column=3, padx=1, pady=1, sticky='nesw')

window.mainloop()

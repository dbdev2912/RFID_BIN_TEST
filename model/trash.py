import tkinter as tk

root = tk.Tk()

def validate(newtext):
    print('validate: {}'.format(newtext))
    return True
vcmd = root.register(validate)

def key(event):
    print('key: {}'.format(event.char))

def var(*args):
    print('var: {} (args {})'.format(svar.get(), args))
svar = tk.StringVar()
svar.trace('w', var)

entry = tk.Entry(root,
                 textvariable=svar, 
                 validate="key", validatecommand=(vcmd, '%P'))
entry.bind('<Key>', key)
entry.pack()
root.mainloop()
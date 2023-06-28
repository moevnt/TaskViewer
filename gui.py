from tkinter import ttk, Tk
import tkinter as tk
from tkinter.messagebox import showinfo

import psutil


def get_proc():
	processes = list()
	for proc in psutil.process_iter(['name', 'pid', 'ppid']):
		processes.append(proc.info)
	return processes


def items_selected(event):
	selected_indices = listbox.curselection()

	# get selected items
	selected_langs = ",".join([listbox.get(i) for i in selected_indices])
	msg = f'You selected: {selected_langs}'
	showinfo(title='Information', message=msg)


root = Tk()
root.title('Task Viewer')
proc = get_proc()
var = tk.Variable(value=proc)

listbox = tk.Listbox(
	root,
	listvariable=var,
	height=25,
	width=50,
	selectmode=tk.EXTENDED
)

listbox.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

listbox.bind('<<ListboxSelect>>', items_selected)

root.mainloop()

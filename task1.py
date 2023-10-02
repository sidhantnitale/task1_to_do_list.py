from tkinter import *
from tkinter import ttk

class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title("To Do List Application")
        self.root.geometry('650x450+300+150')

        self.label = Label(self.root, text='To Do List App', font='Arial 25 bold', width=10, bd=5, bg='light blue', fg='red')
        self.label.pack(side='top', fill='both')

        self.label2 = Label(self.root, text="Add Task", font='Arial 18 bold', width=10, bd=5, bg='white', fg='black')
        self.label2.place(x=40, y=54)

        self.label3 = Label(self.root, text="The task to be performed", font='Arial 18 bold', width=17, bd=5, bg='orange', fg='black')
        self.label3.place(x=320, y=54)

        self.main_text = Listbox(self.root, height=9, bd=5, width=23, font='Arial 20 bold')
        self.main_text.place(x=280, y=100)

        self.text = Text(self.root, bd=5, height=2, width=30, font='Arial 10 bold')
        self.text.place(x=20, y=120)

        self.button = Button(self.root, text="Add", font='Arial 20 bold', width=10, bd=5, bg='orange', fg='black', command=self.add)
        self.button.place(x=30, y=180)

        self.button2 = Button(self.root, text="Delete", font='Arial 20 bold', width=10, bd=5, bg='orange', fg='black', command=self.delete)
        self.button2.place(x=30, y=280)

        self.button3 = Button(self.root, text="Complete Task", font='Arial 20 bold', width=15, bd=5, bg='orange', fg='black', command=self.complete)
        self.button3.place(x=30, y=380)
        self.completed_tasks = []

    def add(self):
        content = self.text.get(1.0, END)
        self.main_text.insert(END, content)

        with open('data.txt', 'a') as file:
            file.write(content)

        self.text.delete(1.0, END)

    def delete(self):
        selected_items = self.main_text.curselection()
        if selected_items:
            for item in selected_items:
                task = self.main_text.get(item)
                self.main_text.delete(item)
                self.remove_task_from_file(task)

    def complete(self):
        selected_items = self.main_text.curselection()
        if selected_items:
            for item in selected_items:
                task = self.main_text.get(item)
                self.main_text.delete(item)
                self.main_text.insert(END, "✓ " + task)
                self.completed_tasks.append(task)

    def remove_task_from_file(self, task):
        with open('data.txt', 'r+') as f:
            lines = f.readlines()
            f.seek(0)
            for line in lines:
                if line.strip() != task.strip():
                    f.write(line)
            f.truncate()

def main():
    root = Tk()
    ui = Todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()

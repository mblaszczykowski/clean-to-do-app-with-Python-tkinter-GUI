

import tkinter
import tkinter.messagebox







usuntekst = '🗑️'


root = tkinter.Tk()
root.title("to-do")
root.geometry("304x400")
root.resizable(False, False)
root.configure(background='white')

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)

        donelist.insert(tkinter.END, usuntekst)

    else:
        pass

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")



def load_tasks():
    try:    
        with open('list.txt', 'r') as f:
            tasks = f.readlines()
            print(tasks)


        for zadanie in tasks:
            if zadanie!="\n" and zadanie!= "\n̶":
                listbox_tasks.insert(tkinter.END, zadanie)
                donelist.insert(tkinter.END, usuntekst)
    except:
        pass
global klikniete

def save_tasks():
    
    tasksss = listbox_tasks.get(0, listbox_tasks.size())
    print(tasksss)

    with open('list.txt', 'w') as f:
        print(len(tasksss))
        for i in range(len(tasksss)):
            print(i)
            f.write(tasksss[i])
            #f.write('\n')
            if i != len(tasksss)-1:
               f.write('\n')

    
    root.destroy()



def clickevent(_Event=None):
    try:
        print('to usuwamy ')
        #print(donelist.get(donelist.curselection()))
        print(donelist.curselection()[0])

        ktore = donelist.curselection()[0]
        listbox_tasks.delete(ktore)
        donelist.delete(ktore)
    except: pass

    entry_task.focus()


# bo trzeba przekreslac albo odkreslac
global klikniete
klikniete = False
def przekreslamy(_Event=None):
    try:
        global klikniete

        index = listbox_tasks.curselection()[0]

        print('tekst')
        starytekst = listbox_tasks.get(index, "end")[0]
        print(starytekst)

        if '\u0336' in starytekst:
            klikniete=True


        # to funkcja od przekreslania
        
        if klikniete==False:

            nowytekst = ''
            for c in starytekst:
                nowytekst += c + '\u0336'

            nowytekst = nowytekst[:len(nowytekst)-1]

            print(nowytekst)
            klikniete = True

        else:
            nowytekst = ''

            nowytekst = starytekst.replace('\u0336', "")
            print(nowytekst)
            klikniete = False

        
        #listbox_tasks.delete(index, old_item)
        listbox_tasks.delete(index)
        listbox_tasks.insert(index, nowytekst)



    except: pass
    entry_task.focus()


# Create GUI
frame_tasks = tkinter.Frame(root, bg='white')
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=14, width=21, font=("Helvetica", 20), bg='white', fg='black', bd=0)
listbox_tasks.pack(side=tkinter.LEFT, padx=8, pady=5)


listbox_tasks.bind('<<ListboxSelect>>', przekreslamy)



donelist = tkinter.Listbox(frame_tasks, height=14, width=2, font=("Helvetica", 20), bg='white', fg='black', bd=0)
donelist.pack(side=tkinter.LEFT, pady=5, padx=5)

donelist.bind('<<ListboxSelect>>', clickevent)



scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tkinter.Entry(root, width=25, highlightbackground='white', fg='black', bg='white', selectbackground='black')
entry_task.place(x=5,y=366)
entry_task.focus()

button_add_task = tkinter.Button(root, text="➕", command=add_task, bg='white', fg='black', highlightbackground='white')
button_add_task.place(x=245, y=364)



root.protocol("WM_DELETE_WINDOW", save_tasks)


load_tasks()

root.mainloop()
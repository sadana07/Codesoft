import tkinter as tk

app=tk.Tk()
app.title("To-do-List")
app.geometry("550x400")
app.iconbitmap("checklist.ico")
app.configure(bg="#0B1D51")

label=tk.Label(app, text="Task Manager", font=("Broadway", 12, "bold"))
quote=tk.Label(app, text="'Make each day your masterpiece'", font=("Harlow Solid Italic", 25, "italic"), bg="#0B1D51", fg="white")
quote.pack(side="bottom", pady=10)
label.pack(pady=5)
font_style=("Bauhaus 93", 10)

list=[]
entry=tk.Entry(app, width=30, font=font_style)
entry.pack(pady=15)

button=tk.Frame(app, background="#0B1D51")
button.pack(pady=10)

checkboxes=tk.Frame(app, background="#0B1D51")
checkboxes.pack(pady=15)

def add_list():
    list_txt=entry.get().strip()
    if list_txt!="":
        var=tk.IntVar()
        checkbox=tk.Checkbutton(checkboxes, text=list_txt, variable=var)
        checkbox.pack(anchor='w')
        list.append((checkbox, var))
        entry.delete(0, tk.end)
def delete_list():
    for checkbox, var in list[:]:
        if var.get()==1:
            checkbox.destroy()
            list.remove((checkbox, var))
tk.Button(button, text="Add", font=font_style, bg="white", fg="#0B1D51", width=15, command=add_list).grid(row=0, column=0, padx=15)
tk.Button(button, text="Delete", font=font_style, bg="white", fg="#0B1D51", width=15, command=delete_list).grid(row=0, column=1, padx=15)
app.mainloop()
import tkinter as tk
from tkinter import filedialog

class TextEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Editor de texto")
        self.text = tk.Text(self.master)
        self.text.pack(fill='both', expand=True)
        self.create_menu()

    def create_menu(self):
        menubar = tk.Menu(self.master)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Abrir", command=self.open_file)
        file_menu.add_command(label="Guardar", command=self.save_file)
        file_menu.add_command(label="Salir", command=self.master.quit)
        menubar.add_cascade(label="Archivo", menu=file_menu)
        self.master.config(menu=menubar)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as f:
                self.text.delete(1.0, 'end')
                self.text.insert('end', f.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename()
        if file_path:
            with open(file_path, 'w') as f:
                f.write(self.text.get(1.0, 'end'))

if __name__ == '__main__':
    root = tk.Tk()
    TextEditor(root)
    root.mainloop()

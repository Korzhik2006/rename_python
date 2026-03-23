import tkinter as tk
from tkinter import filedialog, messagebox
# Импортируем функцию из нашего второго файла
from logic import rename_files

def start_process():
    folder = entry_dir.get()
    pattern = entry_pattern.get()
    
    if not folder or not pattern:
        messagebox.showwarning("Внимание", "Заполните все поля!")
        return
        
    try:
        # Вызываем логику из logic.py
        total = rename_files(folder, pattern)
        messagebox.showinfo("Готово", f"Переименовано файлов: {total}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Что-то пошло не так: {e}")

def select_dir():
    path = filedialog.askdirectory()
    if path:
        entry_dir.delete(0, tk.END)
        entry_dir.insert(0, path)

# Создание интерфейса
root = tk.Tk()
root.title("Renamer Pro")
root.geometry("400x250")

tk.Label(root, text="Папка с файлами:").pack(pady=(20, 0))
frame = tk.Frame(root)
frame.pack(pady=5)
entry_dir = tk.Entry(frame, width=30)
entry_dir.pack(side=tk.LEFT, padx=5)
tk.Button(frame, text="Обзор", command=select_dir).pack(side=tk.LEFT)

tk.Label(root, text="Шаблон имени:").pack(pady=(10, 0))
entry_pattern = tk.Entry(root, width=42)
entry_pattern.pack(pady=5)

tk.Button(root, text="ЗАПУСТИТЬ", command=start_process, 
          bg="#2196F3", fg="white", font=("Arial", 10, "bold"), height=2, width=20).pack(pady=20)

root.mainloop()

import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.status = "À faire"

    def mark_done(self):
        self.status = "Terminé"

    def __str__(self):
        return f"Titre : {self.title}\nDescription : {self.description}\nStatut : {self.status}"

class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def edit_task(self, index, new_title, new_description):
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            task.title = new_title
            task.description = new_description

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def show_all_tasks(self):
        return self.tasks

    def show_todo_tasks(self):
        return [task for task in self.tasks if task.status == "À faire"]

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Todo List App")

        self.task_list = TaskList()

        self.title_label = tk.Label(master, text="Titre:")
        self.title_label.grid(row=0, column=0, sticky="e", padx=10, pady=10)

        self.title_entry = tk.Entry(master)
        self.title_entry.grid(row=0, column=1, padx=10, pady=10)

        self.description_label = tk.Label(master, text="Description:")
        self.description_label.grid(row=1, column=0, sticky="e", padx=10, pady=10)

        self.description_entry = tk.Entry(master)
        self.description_entry.grid(row=1, column=1, padx=10, pady=10)

        self.add_button = tk.Button(master, text="Ajouter une tâche", command=self.add_task)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.task_listbox = tk.Listbox(master, height=10, selectmode=tk.SINGLE)
        self.task_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.show_all_button = tk.Button(master, text="Afficher toutes les tâches", command=self.show_all_tasks)
        self.show_all_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.show_todo_button = tk.Button(master, text="Afficher les tâches à faire", command=self.show_todo_tasks)
        self.show_todo_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.mark_done_button = tk.Button(master, text="Marquer comme terminée", command=self.mark_task_done)
        self.mark_done_button.grid(row=6, column=0, columnspan=2, pady=10)

        self.remove_button = tk.Button(master, text="Supprimer la tâche", command=self.remove_task)
        self.remove_button.grid(row=7, column=0, columnspan=2, pady=10)

    def add_task(self):
        title = self.title_entry.get()
        description = self.description_entry.get()

        if title and description:
            task = Task(title, description)
            self.task_list.add_task(task)
            self.task_listbox.insert(tk.END, f"{task.title} - {task.description}")
            self.clear_entries()
        else:
            messagebox.showwarning("Erreur", "Veuillez remplir tous les champs.")

    def show_all_tasks(self):
        tasks = self.task_list.show_all_tasks()
        self.show_tasks("Liste de toutes les tâches", tasks)

    def show_todo_tasks(self):
        tasks = self.task_list.show_todo_tasks()
        self.show_tasks("Liste des tâches à faire", tasks)

    def mark_task_done(self):
        selected_index = self.task_listbox.curselection()

        if selected_index:
            task_index = selected_index[0]
            self.task_list.tasks[task_index].mark_done()
            self.show_all_tasks()
        else:
            messagebox.showwarning("Erreur", "Veuillez sélectionner une tâche à marquer comme terminée.")

    def remove_task(self):
        selected_index = self.task_listbox.curselection()

        if selected_index:
            task_index = selected_index[0]
            self.task_list.remove_task(task_index)
            self.show_all_tasks()
        else:
            messagebox.showwarning("Erreur", "Veuillez sélectionner une tâche à supprimer.")

    def show_tasks(self, title, tasks):
        if tasks:
            task_details = "\n\n".join([str(task) for task in tasks])
            messagebox.showinfo(title, task_details)
        else:
            messagebox.showinfo(title, "Aucune tâche trouvée.")

    def clear_entries(self):
        self.title_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

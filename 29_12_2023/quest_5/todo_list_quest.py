class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.status = "À faire"

    def __str__(self):
        return f"Titre : {self.title}\nDescription : {self.description}\nStatut : {self.status}"


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def show_all_tasks(self):
        print("Liste de toutes les tâches :")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")
        print()

    def show_todo_tasks(self):
        print("Liste des tâches à faire :")
        for index, task in enumerate(self.tasks, start=1):
            if task.status == "À faire":
                print(f"{index}. {task}")
        print()

    def mark_task_done(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            task.status = "Terminé"
            print(f"La tâche '{task.title}' a été marquée comme terminée.\n")
        else:
            print("Numéro de tâche invalide.\n")

# Fonction principale
def main():
    todo_list = TodoList()

    while True:
        print("===== Menu =====")
        print("1. Ajouter une tâche")
        print("2. Afficher toutes les tâches")
        print("3. Afficher les tâches à faire")
        print("4. Marquer une tâche comme terminée")
        print("5. Quitter")

        choice = input("Entrez le numéro de votre choix : ")

        if choice == "1":
            title = input("Entrez le titre de la tâche : ")
            description = input("Entrez la description de la tâche : ")
            task = Task(title, description)
            todo_list.add_task(task)
            print("Tâche ajoutée avec succès.\n")

        elif choice == "2":
            todo_list.show_all_tasks()

        elif choice == "3":
            todo_list.show_todo_tasks()

        elif choice == "4":
            task_index = int(input("Entrez le numéro de la tâche à marquer comme terminée : "))
            todo_list.mark_task_done(task_index)

        elif choice == "5":
            print("Programme terminé. Au revoir!")
            break

        else:
            print("Choix invalide. Veuillez réessayer.\n")

if __name__ == "__main__":
    main()

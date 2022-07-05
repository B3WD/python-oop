from task import Task

class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def get_task_names(self):
        return [t.name for t in self.tasks]

    def get_task_by_name(self, task_name):
        for t in self.tasks:
            if t.name == task_name:
                return t

    def get_completed_tasks(self):
        return [t for t in self.tasks if t.completed]

    def get_not_completed(self):
        return [t for t in self.tasks if not t.completed]

    def add_task(self, new_task : Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name : str):
        if task_name not in self.get_task_names():
            return f"Could not find task with the name {task_name}"

        task_to_complete = self.get_task_by_name(task_name)
        task_to_complete.completed = True
        return f"Completed task {task_name}"

    def clean_section(self):
        completed_tasks = self.get_completed_tasks()
        self.tasks = self.get_not_completed()
        return f"Cleared {len(completed_tasks)} tasks."

    def view_section(self):
        section_msg = f"Section {self.name}\n"
        tasks_msg = [f"{t.details()}" for t in self.tasks]
        return section_msg + "\n".join(tasks_msg)


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())
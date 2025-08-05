# File: task_management_system.py
from datetime import datetime, timedelta

class Task:
    def __init__(self, description, priority, time_bound, due_date=None, category=None):
        self.description = description
        self.priority = priority.lower()
        self.time_bound = time_bound.lower() == 'yes'
        self.due_date = due_date
        self.category = category
        self.completed = False
    
    def __str__(self):
        status = "✓" if self.completed else "✗"
        due_info = f", Due: {self.due_date.strftime('%Y-%m-%d')}" if self.due_date else ""
        return f"[{status}] {self.description} ({self.priority} priority{', time-bound' if self.time_bound else ''}{due_info})"

def task_management_system():
    tasks = []
    
    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Complete")
        print("4. Get Recommendations")
        print("5. Exit")
        
        choice = input("Choose option (1-5): ")
        
        match choice:
            case "1":
                description = input("Enter task description: ")
                priority = input("Priority (high/medium/low): ")
                time_bound = input("Is it time-bound? (yes/no): ")
                
                due_date = None
                if time_bound.lower() == 'yes':
                    due_str = input("Due date (YYYY-MM-DD, leave blank for today): ")
                    due_date = datetime.strptime(due_str, "%Y-%m-%d").date() if due_str else datetime.now().date()
                
                category = input("Category (work/personal/health/other): ")
                
                tasks.append(Task(description, priority, time_bound, due_date, category))
                print("Task added successfully!")
            
            case "2":
                if not tasks:
                    print("No tasks available.")
                    continue
                
                print("\nAll Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            
            case "3":
                if not tasks:
                    print("No tasks to mark complete.")
                    continue
                
                print("\nPending Tasks:")
                for i, task in enumerate([t for t in tasks if not t.completed], 1):
                    print(f"{i}. {task}")
                
                try:
                    task_num = int(input("Enter task number to mark complete: ")) - 1
                    pending_tasks = [t for t in tasks if not t.completed]
                    if 0 <= task_num < len(pending_tasks):
                        pending_tasks[task_num].completed = True
                        print("Task marked complete!")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
            
            case "4":
                if not tasks:
                    print("No tasks to recommend.")
                    continue
                
                print("\nTask Recommendations:")
                now = datetime.now().date()
                
                # Critical tasks: high priority, time-bound, due today or overdue
                critical = [t for t in tasks 
                           if not t.completed 
                           and t.priority == 'high' 
                           and t.time_bound 
                           and t.due_date and t.due_date <= now]
                
                # Urgent tasks: high priority, time-bound, due soon
                urgent = [t for t in tasks 
                         if not t.completed 
                         and t.priority == 'high' 
                         and t.time_bound 
                         and t.due_date and now < t.due_date <= now + timedelta(days=3)]
                
                # Important tasks: high priority but not time-bound
                important = [t for t in tasks 
                           if not t.completed 
                           and t.priority == 'high' 
                           and not t.time_bound]
                
                # Other tasks
                other = [t for t in tasks 
                        if not t.completed 
                        and t not in critical + urgent + important]
                
                if critical:
                    print("\n🚨 CRITICAL (due now or overdue):")
                    for task in critical:
                        print(f"- {task}")
                
                if urgent:
                    print("\n⚠️ URGENT (due in next 3 days):")
                    for task in urgent:
                        print(f"- {task}")
                
                if important:
                    print("\n⭐ IMPORTANT (high priority):")
                    for task in important:
                        print(f"- {task}")
                
                if other:
                    print("\n📝 OTHER TASKS:")
                    for task in other:
                        print(f"- {task}")
                
                if not any([critical, urgent, important, other]):
                    print("All tasks are completed! 🎉")
            
            case "5":
                print("Exiting Task Management System.")
                break
            
            case _:
                print("Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    task_management_system()
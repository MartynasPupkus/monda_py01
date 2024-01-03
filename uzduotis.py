def add_task(task_list: list, task_name: str, done=False):
    task = (task_name, done)
    task_list.append(task)
    return task_list

def remove_task(task_list: list, task_index: int):
    pass

def print_tasks(task_list: list, hide_done=False):
    for index, task in enumerate(task_list):
         if task['done']:
              is_done = 'x'
        else:
            is_done = '-'
        
        print(f'{index:} [{is_done}] {task['name']}')
    
def mark_done(task_list: list, task_index: int):
    pass
input_task_id(task_list: list)

def main(task_list)
    while True:
        print('--- [Tasks] ---')
        print('9: Exit')
        print('1: Print all tasks')
        print('2: Add a task')
        choice = input('Choice:   ')
        if choice.startswith('0'):
                break
        if choice.startswith('1'):
            print_tasks(task_list)
        if choice.startswith('2'):
             task_list = add_task(task_list, input('Task name:   '))
        if choice.startswith('4'):
             task_id = remove_task(remove_task, input('Choose task ID to remove:  '))
        if task_id.isnumeric():
             task_id = int(task_id)
        else:
             print('Wrong Task ID, it must be a number')
            continue
     
     if task_id > len(task_list):
         print('Task ID is too high')
    task_list = remove_task(task_list, task_id)
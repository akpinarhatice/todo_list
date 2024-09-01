from collections import OrderedDict

def get_menu():
    print("Please select the action you want to perform:")
    print("1. Show All To-Do Lists")
    print("2. Create A New To-Do List")
    selection_input = input("Enter Selection Number: ")
    if selection_input == "1":
        show_todo_list()
        selection_input2 = input("To make a new selection press '1', to exit '2' and to remove item '3', to check list '4' ")
        if selection_input2 == "1":
            get_menu()
        elif selection_input2 == "2":
            return exit()
        elif selection_input2 == "3":
            show_todo_list()
            remove_item_list()
            get_menu()
        elif selection_input2 == "4":
            show_todo_list()
            check_item_list()
    elif selection_input == "2":
        add_item_to_list()
        print("test")
        return get_menu()
    else:
        print("Please make a valid choice")
        return get_menu()

def add_item_to_list():
    item = input("Please write an item for to-do list:\n")
    if not item:
        print("Cannot be leave blank.")
        return add_item_to_list()
    index = len(todo_list.keys()) + 1
    todo_list[str(index)] = {"TODO:": item, "is_done": False}
    print("New job is added to list:\n", "{}.".format(index), item)
    return get_menu()

def show_todo_list():
    print("All To-Do List:\n")
    for key, value in todo_list.items():
        is_done_txt = "(It is done!)" if value["is_done"] else "(It's not over!)"
        print(f"{key}. {value['TODO:']} {is_done_txt}")

def check_item_list():
    check_item = input("Please enter the value of the item to be checked: ")
    items = list(todo_list.items())
    for key, value in items:
        if key == check_item:
            value["is_done"] = not value["is_done"]
            todo_list.clear()
            for index, (key, value) in enumerate(items, start=1):
                todo_list[str(index)] = value
            show_todo_list()

def remove_item_list():
    delete_item = input("Please enter the value of the item to be deleted: ")
    keys_to_remove = [key for key in todo_list if key == delete_item]
    for key in keys_to_remove:
        del todo_list[key]
        print("Deleted successfully.")
        items = list(todo_list.items())
        todo_list.clear()
        for index, (key, value) in enumerate(items, start=1):
            todo_list[str(index)] = value
        show_todo_list()


todo_list = OrderedDict()
get_menu()
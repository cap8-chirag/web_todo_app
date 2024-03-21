def get_todos(filepath):
    """ this function reads the list of items from the text file"""
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos


def write_todos(filepath, todos):
    """ this function writes the list of items from the text file"""
    with open(filepath, "w") as file:
        file.writelines(todos)


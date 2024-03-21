import streamlit as st
from modules import functions

print("I am running again at top")
st.title("My todo app")
filepath = "Data/todos.txt"
todos = functions.get_todos(filepath)


def add_todo():
    to_do = st.session_state["new_todo"] + "\n"
    todos.append(to_do)
    functions.write_todos(filepath, todos)
    st.session_state["new_todo"]=""


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(filepath, todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Enter a todo",
              on_change=add_todo,
              key="new_todo")

print("I am running again at bottom")





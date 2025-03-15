import streamlit as st

st.title("📝 To-Do List App by Arisha")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Sidebar Heading
st.sidebar.header("📌 Manage Your Tasks")


new_task = st.sidebar.text_input("➕ Add a new task:", placeholder="Enter your task here...")

if st.sidebar.button("Add Task"):
    if new_task.strip():
        st.session_state.tasks.append({"task": new_task, "completed": False})  
        st.success("Task added successfully! ✅")
    else:
        st.warning("Task cannot be empty! ❌")


st.subheader("📋 Your To-Do List")
if not st.session_state.tasks:
    st.info("No tasks added yet. Start by adding a task from the sidebar!")
else:
    for index, task in enumerate(st.session_state.tasks):
        col1, col2, col3 = st.columns([0.7, 0.15, 0.15])

        completed = col1.checkbox(f"{task['task']}", task["completed"], key=f"check_{index}")
        if completed != task["completed"]:
            st.session_state.tasks[index]["completed"] = completed

        # Update Task
        if col2.button("✏ Edit", key=f"edit_{index}"):
            new_text = st.text_input("Update Task:", task["task"], key=f"input_{index}")
            if new_text and st.button("Save", key=f"save_{index}"):
                st.session_state.tasks[index]["task"] = new_text
               

        # Delete Task 
        if col3.button("❌ Del", key=f"delete_{index}"):
            del st.session_state.tasks[index]
            

# Clear All Button
if st.button("🗑️ Clear All Tasks"):
    st.session_state.tasks = []
    st.success("All tasks deleted successfully! 🎉")

# Footer
st.markdown("-By Arisha-")
st.caption(" Stay happy with simple To-Do List App!😊")



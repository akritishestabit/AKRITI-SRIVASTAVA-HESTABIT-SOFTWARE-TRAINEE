const todoInput = document.getElementById("todoInput");
const addBtn = document.getElementById("addBtn");
const todoList = document.getElementById("todoList");

let todos = [];

try {
    const storedTodos = localStorage.getItem("todos");
    todos = storedTodos ? JSON.parse(storedTodos) : [];
} catch (error) {
    console.error("Failed to load todos from localStorage", error);
    todos = [];
}

function saveTodos() {
    try {
        localStorage.setItem("todos", JSON.stringify(todos));
    } catch (error) {
        console.error("Failed to save todos", error);
    }
}

function renderTodos() {
    todoList.innerHTML = "";

    todos.forEach((todo, index) => {
        const li = document.createElement("li");
        li.textContent = todo;

        const editBtn = document.createElement("button");
        editBtn.textContent = "Edit";
        editBtn.onclick = () => editTodo(index);

        const deleteBtn = document.createElement("button");
        deleteBtn.textContent = "Delete";
        deleteBtn.onclick = () => deleteTodo(index);

        const btnGroup = document.createElement("div");
        btnGroup.append(editBtn, deleteBtn);

        li.appendChild(btnGroup);
        todoList.appendChild(li);
    });
}

function addTodo() {
    try {
        const value = todoInput.value.trim();
        if (value === "") return;

        todos.push(value);
        saveTodos();
        renderTodos();
        todoInput.value = "";
    } catch (error) {
        console.error("Error while adding todo", error);
    }
}

function deleteTodo(index) {
    try {
        todos.splice(index, 1);
        saveTodos();
        renderTodos();
    } catch (error) {
        console.error("Error while deleting todo", error);
    }
}

function editTodo(index) {
    try {
        const updated = prompt("Edit your task:", todos[index]);
        if (updated !== null && updated.trim() !== "") {
            todos[index] = updated.trim();
            saveTodos();
            renderTodos();
        }
    } catch (error) {
        console.error("Error while editing todo", error);
    }
}

addBtn.addEventListener("click", addTodo);
renderTodos();

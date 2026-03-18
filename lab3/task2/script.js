const form = document.getElementById('todo-form');
const input = document.getElementById('todo-input');
const todoList = document.getElementById('todo-list');
const stats = document.getElementById('todo-stats');

form.addEventListener('submit', function (event) {
    event.preventDefault();
    const taskText = input.value.trim();
    if (taskText === '') return;

    addTodoItem(taskText);
    input.value = '';
});

function addTodoItem(text) {
    const listItem = document.createElement('li');
    listItem.className = 'todo-item';

    const leftSection = document.createElement('div');
    leftSection.className = 'todo-left';

    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';

    const span = document.createElement('span');
    span.textContent = text;
    span.className = 'todo-text';

    checkbox.addEventListener('change', function () {
        span.classList.toggle('done');
        updateStats();
    });

    const deleteButton = document.createElement('button');
    deleteButton.textContent = '🗑';
    deleteButton.className = 'delete-btn';

    deleteButton.addEventListener('click', function () {
        todoList.removeChild(listItem);
        updateStats();
    });

    leftSection.appendChild(checkbox);
    leftSection.appendChild(span);

    listItem.appendChild(leftSection);
    listItem.appendChild(deleteButton);

    todoList.appendChild(listItem);

    updateStats(); 
}

function updateStats() {
    const items = document.querySelectorAll('.todo-text');
    const total = items.length;
    let incompleted = 0;
    items.forEach(item => {
        if (!item.classList.contains('done')) incompleted++;
    });
    stats.textContent = `Total: ${total}, Incompleted: ${incompleted}`;
}

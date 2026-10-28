document.addEventListener('DOMContentLoaded', function () {
    const columns = document.querySelectorAll('.row > div');
    const pendingList = columns[0];
    const completedList = columns[1];
    const form = document.querySelector('form');
    const input = form.querySelector('input.form-control');

    function createTaskCard(taskText) {
        const card = document.createElement('div');
        card.className = 'card m-1';
        card.innerHTML = `
            <div class="card-body">
                <span class="task-text">${taskText}</span>
                <span style="position: relative; float: right;">
                    <a class="btn btn-success"><i class="fa fa-check"></i> Mark as Done</a>
                    <a class="btn btn-danger"><i class="fa fa-trash"></i></a>
                    <a class="btn btn-primary"><i class="fa fa-pencil"></i></a>
                </span>
            </div>
        `;
        return card;
    }

    form.addEventListener('submit', function (e) {
        e.preventDefault();
        const text = input.value.trim();
        if (text !== '') {
            const newCard = createTaskCard(text);
            pendingList.appendChild(newCard);
            input.value = '';
            pendingList.scrollTop = pendingList.scrollHeight;
        }
    });

    pendingList.addEventListener('click', function (e) {
        const btn = e.target.closest('a.btn');
        if (!btn) return;

        const card = btn.closest('.card');
        const cardBody = card.querySelector('.card-body');
        let textNode = cardBody.querySelector('.task-text') || cardBody.firstChild;
        let currentText = textNode.textContent.trim();

        if (btn.classList.contains('btn-success')) {
            const completedCard = document.createElement('div');
            completedCard.className = 'card m-1';
            completedCard.innerHTML = `<div class="card-body">${currentText}</div>`;
            completedList.appendChild(completedCard);
            card.remove();
        } else if (btn.classList.contains('btn-danger')) {
            card.remove();
        } else if (btn.classList.contains('btn-primary')) {
            const updatedText = prompt('Edit your task:', currentText);
            if (updatedText !== null && updatedText.trim() !== '') {
                textNode.textContent = updatedText.trim() + ' ';
            }
        }
    });
});
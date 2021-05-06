input = document.getElementById('filter');
categories = document.getElementById('categories');
input.value = localStorage.getItem('filter');
categories.value = localStorage.getItem('categories');
dialog = true;

document.querySelector('#closeDialog').onclick = function () {
    dialog = false;
    document.querySelector('.dialog').style.display = 'none';
}
input.addEventListener('keyup', function () {
    filter = input.value.toLowerCase();
    localStorage.setItem('filter', input.value);
    filterElements = document.querySelectorAll('.content');
    filterElements.forEach(item => {
        if (item.querySelector('.caption').innerHTML.toLowerCase().indexOf(filter) < 0) {
            item.style.display = 'none';
        }
        else {
            item.style.display = '';
        }
    });
})

categories.onclick = function () {
    localStorage.setItem('categories', categories.value);
}

function  filterLoad() {
    filter = input.value.toLowerCase();
    filterElements = document.querySelectorAll('.content');
    filterElements.forEach(item => {
        if (item.querySelector('.caption').innerHTML.toLowerCase().indexOf(filter) < 0) {
            item.style.display = 'none';
        }
        else {
            item.style.display = '';
        }
    });
}

filterLoad()
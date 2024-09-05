document.addEventListener('DOMContentLoaded', loadNews);
document.getElementById('newsForm').addEventListener('submit', addNews);

function loadNews() {
    const newsList = document.getElementById('newsList');
    const news = JSON.parse(localStorage.getItem('news')) || [];

    news.forEach((item, index) => {
        const li = createNewsElement(item, index);
        newsList.appendChild(li);
    });
}

function addNews(e) {
    e.preventDefault();

    const newsInput = document.getElementById('newsInput');
    const newsText = newsInput.value;

    const news = JSON.parse(localStorage.getItem('news')) || [];
    news.push(newsText);
    localStorage.setItem('news', JSON.stringify(news));

    const li = createNewsElement(newsText, news.length - 1);
    document.getElementById('newsList').appendChild(li);
    newsInput.value = '';
}

function createNewsElement(text, index) {
    const li = document.createElement('li');
    li.innerText = text;

    const deleteButton = document.createElement('span');
    deleteButton.innerText = '❌';
    deleteButton.className = 'delete-button';
    deleteButton.onclick = function() {
        deleteNews(index);
    };

    li.appendChild(deleteButton);
    return li;
}

function deleteNews(index) {
    const news = JSON.parse(localStorage.getItem('news')) || [];
    news.splice(index, 1);
    localStorage.setItem('news', JSON.stringify(news));
    document.getElementById('newsList').innerHTML = '';
    loadNews();
}
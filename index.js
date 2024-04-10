function bodyLoaded() {
    const main = document.getElementById('main');
    for (let i = 1; i < 51; i++) {
        main.appendChild(newMaze(i));
    }
}

function newMaze(mazeId) {
    const elem = document.createElement('a');
    elem.className = 'maze';
    elem.innerText = 'maze-' + mazeId;
    elem.href = '@' + mazeId;
    return elem;
}
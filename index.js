async function bodyLoaded() {
    const main = document.getElementById('main');
    const r = await fetch('/maze/max.txt');
    const max = parseInt(await r.text());
    for (let i = 1; i < max+1; i++) {
        main.appendChild(newMaze(i));
    }
}

function newMaze(mazeId) {
    const elem = document.createElement('a');
    elem.className = 'maze';
    elem.innerText = mazeId.toString().padStart(3, '0');
    elem.href = '@' + mazeId;
    return elem;
}
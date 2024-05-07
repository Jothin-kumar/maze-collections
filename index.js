const usp = new URLSearchParams(window.location.search);
const level = usp.get('level') || 'medium';

async function bodyLoaded() {
    document.getElementById('lvl-' + level).classList.add('current-lvl');
    const main = document.getElementById('main');
    const msgElem = document.getElementById('main-msg');
    const r = await fetch(`/maze/${level}/max.txt`);
    if (!r.ok) {
        msgElem.innerText = 'Failed to load mazes';
        msgElem.style.color = 'red';
        return;
    }
    const max = parseInt(await r.text());
    for (let i = 1; i < max+1; i++) {
        main.appendChild(newMaze(i));
    }

    msgElem.style.display = 'none';
}

function newMaze(mazeId) {
    const elem = document.createElement('a');
    elem.className = 'maze';
    elem.innerText = mazeId.toString().padStart(3, '0');
    elem.href = level === "medium" ? `@${mazeId}`: `/${level}/@${mazeId}`;
    return elem;
}

function toLevel(elem) {
    const toLevel = elem.id === "lvl-easy" ? "easy" : elem.id === "lvl-medium" ? "medium" : "hard";
    usp.set('level', toLevel);
    window.location.search = usp.toString();
}
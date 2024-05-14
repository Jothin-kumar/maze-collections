const usp = new URLSearchParams(window.location.search);
const level = usp.get('level') || 'medium';

async function bodyLoaded() {
    document.getElementById('lvl-' + level).classList.add('current-lvl');
    const main = document.getElementById('main');
    const msgElem = document.getElementById('main-msg');
    const ratingsRequest = await fetch(`/maze/${level}/ratings.txt`);
    if (!ratingsRequest.ok) {
        msgElem.innerText = 'Failed to load mazes';
        msgElem.style.color = 'red';
        return;
    }
    const ratings = (await ratingsRequest.text()).split('\n').map(x => parseFloat(x));
    for (let i = 0; i < ratings.length; i++) {
        main.appendChild(newMaze(i+1, ratings[i]));
    }

    msgElem.style.display = 'none';
}

function newMaze(mazeId, rating) {
    const elem = document.createElement('a');
    elem.className = 'maze';
    elem.innerText = mazeId.toString().padStart(3, '0');
    elem.href = level === "medium" ? `@${mazeId}`: `/${level}/@${mazeId}`;
    elem.setAttribute('tooltip', `Rating: ${rating}`);
    enableTooltip(elem);
    return elem;
}

function toLevel(elem) {
    const toLevel = elem.id === "lvl-easy" ? "easy" : elem.id === "lvl-medium" ? "medium" : "hard";
    usp.set('level', toLevel);
    window.location.search = usp.toString();
}

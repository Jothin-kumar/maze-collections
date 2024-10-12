const usp = new URLSearchParams(window.location.search);
const level = usp.get('level') || 'easy';

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
    const ratings = (await ratingsRequest.text()).split('\n').map(x => parseInt(x));
    const mazes = [];
    for (let i = 0; i < ratings.length; i++) {
        mazes.push([newMaze(i+1, ratings[i]), i+1, ratings[i]]) // Format: [mazeElem, id, rating]
    }
    mazes.sort((a, b) => a[2] - b[2]);
    mazes.forEach(maze => main.appendChild(maze[0]));

    msgElem.style.display = 'none';
}

function newMaze(mazeId, rating) {
    const elem = document.createElement('a');
    elem.className = 'maze';
    elem.innerHTML = `${mazeId.toString().padStart(3, '0')}<br><span class="rating">${rating}</span>`;
    elem.href = level === "easy" ? `@${mazeId}`: `/${level}/@${mazeId}`;
    return elem;
}

function toLevel(elem) {
    const toLevel = elem.id === "lvl-easy" ? "easy" : elem.id === "lvl-medium" ? "medium" : "hard";
    usp.set('level', toLevel);
    window.location.search = usp.toString();
}

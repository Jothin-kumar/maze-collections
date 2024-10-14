class cookieManager {
    constructor() {
        this.cookies = {};
        document.cookie.split("; ").forEach(cookie => {
            const [name, value] = cookie.split("=");
            this.cookies[name] = value;
        });
    }
    set(name, value) {
        this.cookies[name] = value;
        document.cookie = `${name}=${value}`;
    }
    get(name) {
        return this.cookies[name];
    }
}
const usp = new cookieManager();
window.level = usp.get('level') || 'easy';

async function bodyReload() {
    document.getElementById('lvl-easy').classList.remove('current-lvl');
    document.getElementById('lvl-medium').classList.remove('current-lvl');
    document.getElementById('lvl-hard').classList.remove('current-lvl');
    document.getElementById('lvl-' + level).classList.add('current-lvl');
    const mazesList = document.getElementById('mazes-list');
    mazesList.innerHTML = '';
    const msgElem = document.getElementById('main-msg');
    const ratingsRequest = await fetch(`https://mazes.jothin.tech/maze/${level}/ratings.txt`);  // For compatibility with A-Maze integration.
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
    mazes.forEach(maze => mazesList.appendChild(maze[0]));

    msgElem.style.display = 'none';
}

function newMaze(mazeId, rating) {
    const elem = document.createElement('a');
    elem.className = 'maze';
    elem.innerHTML = `${mazeId.toString().padStart(3, '0')}<br><span class="rating">${rating}</span>`;
    elem.onclick = () => window.mazeClickCallback(level, mazeId);
    return elem;
}

function toLevel(elem) {
    const toLevel = elem.id === "lvl-easy" ? "easy" : elem.id === "lvl-medium" ? "medium" : "hard";
    usp.set('level', toLevel);
    window.level = toLevel;
    bodyReload()
}

function configureMazeClickCallback(f) {
    window.mazeClickCallback = f
}
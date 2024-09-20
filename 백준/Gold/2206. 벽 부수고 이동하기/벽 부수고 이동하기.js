class Queue {
    constructor() {
        this.queue = [];
        this.front = 0;
        this.rear = 0;
    }
    enqueue(value) {
        this.queue[this.rear++] = value;
    }
    dequeue() {
        const value = this.queue[this.front];
        delete this.queue[this.front];
        this.front++;
        return value
    }
    size() {
        return this.rear - this.front;
    }
}




const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const [n, m] = input[0].split(' ').map(Number);
let answer = -1;
const array = Array.from({ length: n }, () =>
    Array.from({ length: m }, () => null)
)
for (let i = 1; i <= n; i++) {
    const row = input[i].split('');
    for (let j = 0; j < m; j++) {
        array[i - 1][j] = Number(row[j]);
    }
}

const [dx, dy] = [[-1, 1, 0, 0], [0, 0, -1, 1]];
const in_range = (nx, ny) => {
    return nx >= n || nx < 0 || ny >= m || ny < 0;
}
const queue = new Queue();

queue.enqueue([0, 0, 0, 1]);

const visited = Array.from({ length: n }, () =>
    Array.from({ length: m }, () => false)
)
const b_visited = Array.from({ length: n }, () =>
    Array.from({ length: m }, () => false)
)
visited[0][0] = true;
while (queue.size()) {
    const [x, y, c, a] = queue.dequeue();
    if (x === (n - 1) && y === (m - 1)) {
        answer = a;
        break;
    }
    for (let i = 0; i < 4; i++) {
        let nx = x + dx[i];
        let ny = y + dy[i];
        if (in_range(nx, ny)) continue;
        if (array[nx][ny] === 1 && c === 1) {
            continue;
        }
        if (c === 1 && b_visited[nx][ny]) continue;
        if (visited[nx][ny]) continue;
        if (array[nx][ny] === 0) {
            queue.enqueue([nx, ny, c, a + 1]);
        }
        else {
            queue.enqueue([nx, ny, 1, a + 1]);
        }
        if (c === 1) b_visited[nx][ny] = true;
        else visited[nx][ny] = true;
    }
}




console.log(answer);
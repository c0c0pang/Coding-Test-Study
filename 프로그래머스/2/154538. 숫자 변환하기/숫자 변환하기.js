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
    return value;
  }

  size() {
    return this.rear - this.front;
  }

  peek() {
    return this.queue[this.front];
  }
}
function solution(x, y, n) {
    const NUM = 1000000;
    var answer = 0;
    let check = false;
    const visited = Array.from({length:NUM+1},()=>false);
    const queue = new Queue();
    queue.enqueue([x,0]);
    while(queue.size()!==0){
        let [v,c] = queue.dequeue();
        if(v===y){
            check = true;
            answer = c;
            break;
        }
        if(v>y) continue;
        if(visited[v]) continue;
        visited[v] = true;
        queue.enqueue([v*3,c+1]);
        queue.enqueue([v*2,c+1]);
        queue.enqueue([v+n,c+1]);
    }
    return check ? answer:-1;
}
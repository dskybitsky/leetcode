export function longestCycle(edges: number[]): number {
    let answer = -1;

    const n = edges.length;

    const visit: number[] = [];

    for (let i = 0; i < n; i++) {
        visit[i] = 0;
    }

    for (let i = 0; i < n; i++) {
        if (!visit[i]) {
            const dist = new Map<number, number>();
            dist.set(i, 1);
            answer = Math.max(answer, dfs(i, edges, dist, visit));
        }   
    }

    return answer;
};

function dfs(node: number, edges: number[], dist: Map<number, number>, visit: number[]): number {
    visit[node] = 1;

    const neighbor = edges[node];

    if (neighbor >= 0) {
        if (!visit[neighbor]) {
            dist.set(neighbor, dist.get(node) + 1);

            return dfs(neighbor, edges, dist, visit);    
        } else if (dist.has(neighbor)) {
            return dist.get(node) - dist.get(neighbor) + 1;
        }
    }

    return -1;
}
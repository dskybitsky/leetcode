export function makeConnected(n: number, connections: number[][]): number {
    if (connections.length < (n - 1)) {
        return -1;
    }

    const adjMap = buildAdjMap(connections);

    const visit: boolean[] = [];

    for (let i = 0; i < n; i++) {
        visit[i] = false;
    }

    const result = 0;

    for (let i = 0; i < n; i++) {
        if (!visit[i]) {
            result++;
            dfs(i, adjMap, visit);
        }
    }

    return result - 1;
}

function dfs(node: number, adjMap: Map<number, Set<number>>, visit: boolean[]): void {
    visit[node] = true;

    if (adjMap.has(node)) {
        for (const neighbor of adjMap.get(node)) {
            if (!visit[neighbor]) {
                dfs(neighbor, adjMap, visit);
            }
        }
    }
}

function buildAdjMap(edges: number[][]): Map<number, Set<number>> {
    const map = new Map<number, Set<number>>();

    for (let i = 0; i < edges.length; i++) {
        const [v1, v2] = edges[i];

        if (!map.has(v1)) {
            map.set(v1, new Set<number>());
        }

        map.get(v1).add(v2);

        if (!map.has(v2)) {
            map.set(v2, new Set<number>());
        }

        map.get(v2).add(v1);
    }

    return map;
}
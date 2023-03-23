export function makeConnected(n: number, connections: number[][]): number {
    if (connections.length < (n - 1)) {
        return -1;
    }

    const vertices = new Map<number, boolean>();

    for (let i = 0; i < n; i++) {
        vertices.set(i, true);
    }

    const adjMap = buildAdjMap(connections);

    let result = 0;

    while (vertices.size > 0) {
        const v = vertices.keys().next().value;

        const vertsToVisit = [v];
        const vertsVisited = new Map<number, boolean>();

        while (vertsToVisit.length > 0) {
            const v1 = vertsToVisit.shift();
        
            vertices.delete(v1);

            if (adjMap.has(v1)) {
                for (const [v2] of adjMap.get(v1)) {
                    if (!vertsVisited.has(v2)) {
                        vertsToVisit.push(v2);
                        vertsVisited.set(v2, true);
                        adjMap.get(v2).delete(v1);
                    }
                }
            }        
        }

        result++;
    }

    return result - 1;
}

function buildAdjMap(edges: number[][]): Map<number, Map<number, boolean>> {
    const map = new Map<number, Map<number, boolean>>();

    for (let i = 0; i < edges.length; i++) {
        const [v1, v2] = edges[i];

        if (!map.has(v1)) {
            map.set(v1, new Map<number, boolean>());
        }

        map.get(v1).set(v2, true);

        if (!map.has(v2)) {
            map.set(v2, new Map<number, boolean>());
        }

        map.get(v2).set(v1, true);
    }

    return map;
}
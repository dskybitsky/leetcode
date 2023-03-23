export function makeConnected(n: number, connections: number[][]): number {
    if (connections.length < (n - 1)) {
        return -1;
    }

    const vertices = new Map<number, boolean>();

    for (let i = 0; i < n; i++) {
        vertices.set(i, true);
    }

    const adjMap = buildAdjMap(connections)

    let result = 0;

    while (vertices.size > 0) {
        const v = vertices.keys().next().value;

        const verts = [v];
        const visitedVerts = new Map<number, boolean>();

        while (verts.length > 0) {
            const v1 = verts.shift();

            if (adjMap.has(v1)) {
                for (const [v2] of adjMap.get(v1)) {
                    if (!visitedVerts.has(v2)) {
                        verts.push(v2);
                        visitedVerts.set(v2, true);
                    }
                }
            }        
        }

        result++;
        
        vertices.delete(v);

        for (const [vv] of visitedVerts) {
            vertices.delete(vv);
        }
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
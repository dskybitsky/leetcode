export function countPairs(n: number, edges: number[][]): number {
    const vertices = new Set<number>();

    for (let i = 0; i < n; i++) {
        vertices.add(i);
    }

    const adjMap = buildAdjMap(edges);

    let result = n * (n - 1) / 2;

    while (vertices.size > 0) {
        const [v] = vertices;

        const vertsToVisit = [v];
        const vertsVisited = new Set<number>();

        vertsVisited.add(v);

        while (vertsToVisit.length > 0) {
            const v1 = vertsToVisit.shift();
        
            vertices.delete(v1);

            if (adjMap.has(v1)) {
                for (const [v2] of adjMap.get(v1)) {
                    if (!vertsVisited.has(v2)) {
                        vertsToVisit.push(v2);
                        vertsVisited.add(v2);
                        
                        adjMap.get(v1).delete(v2);
                        adjMap.get(v2).delete(v1);

                        vertices.delete(v2);
                    }
                }
            }
        }

        result -= vertsVisited.size * (vertsVisited.size - 1) / 2
    }

    return result;
};

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
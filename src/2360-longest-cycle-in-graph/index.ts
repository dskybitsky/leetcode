export function longestCycle(edges: number[]): number {
    const vertices = new Set<number>();

    for (let i = 0; i < edges.length; i++) {
        vertices.add(i);
    }

    let result = -1;

    const adjMap = buildAdjMap(edges);

    while (vertices.size > 0) {
        const [v] = vertices;

        const vertsToVisit = [v];
        const vertsVisited = new Map<number, number>();

        vertsVisited.set(v, 0);

        let distance = 1;

        while (vertsToVisit.length > 0) {
            const v1 = vertsToVisit.shift();

            vertices.delete(v1);
        
            if (adjMap.has(v1)) {
                for (const v2 of adjMap.get(v1)) {
                    if (!vertsVisited.has(v2)) {
                        vertsToVisit.push(v2);
                        vertsVisited.set(v2, distance);
                        distance++;
                        vertices.delete(v2);
                    } else {
                        result = Math.max(result, distance - vertsVisited.get(v2));
                    }
                }
            }
        }
    }

    return result;
};

function buildAdjMap(edges: number[]): Map<number, Set<number>> {
    const map = new Map<number, Set<number>>();

    for (let i = 0; i < edges.length; i++) {
        if (edges[i] >= 0) {
            const v1 = i;
            const v2 = edges[i];

            if (!map.has(v1)) {
                map.set(v1, new Set<number>());
            }
    
            map.get(v1).add(v2);
        }
    }

    return map;
};

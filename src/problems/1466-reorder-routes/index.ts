export function minReorder(n: number, connections: number[][]): number {
    const adjMap = buildAdjMap(connections);

    let result = 0;

    const vertsToVisit = [0];
    const vertsVisited = new Map<number, boolean>();

    vertsVisited.set(0, true);

    while (vertsToVisit.length > 0) {
        const v1 = vertsToVisit.shift();
    
        if (adjMap.has(v1)) {
            for (const [v2, dir] of adjMap.get(v1)) {
                if (!vertsVisited.has(v2)) {
                    vertsToVisit.push(v2);
                    vertsVisited.set(v2, true);

                    if (dir > 0) {
                        result++;
                    }
                }
            }
        }        
    }

    return result;
};

function buildAdjMap(roads: number[][]): Map<number, Map<number, number>> {
    const map = new Map<number, Map<number, number>>();

    for (let i = 0; i < roads.length; i++) {
        const [v1, v2] = roads[i];

        if (!map.has(v1)) {
            map.set(v1, new Map<number, number>());
        }

        map.get(v1).set(v2, 1);

        if (!map.has(v2)) {
            map.set(v2, new Map<number, number>());
        }

        map.get(v2).set(v1, -1);
    }

    return map;
}
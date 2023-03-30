export function minScore(n: number, roads: number[][]): number {
    const unprocessed = new Map<number, boolean>();

    for (let i = 1; i <= n; i++) {
        unprocessed.set(i, true);
    }

    const adjMap = buildAdjMap(roads);

    const verts = [1];
    const visitedVerts = new Map<number, boolean>();

    let minW = 10000;

    while (verts.length > 0) {
        const v = verts.shift();

        for (const [v2, w] of adjMap.get(v)) {
            minW = Math.min(minW, w);

            if (!visitedVerts.has(v2)) {
                verts.push(v2);
                visitedVerts.set(v2, true);
            }
        }
    }

    return minW;
};

function buildAdjMap(roads: number[][]): Map<number, Map<number, number>> {
    const map = new Map<number, Map<number, number>>();

    for (let i = 0; i < roads.length; i++) {
        const [v1, v2, dist] = roads[i];

        if (!map.has(v1)) {
            map.set(v1, new Map<number, number>());
        }

        map.get(v1).set(v2, dist);

        if (!map.has(v2)) {
            map.set(v2, new Map<number, number>());
        }

        map.get(v2).set(v1, dist);
    }

    return map;
}
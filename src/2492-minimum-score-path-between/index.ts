export function minScore(n: number, roads: number[][]): number {
    const unprocessed = new Map<number, boolean>();

    for (let i = 1; i <= n; i++) {
        unprocessed.set(i, true);
    }

    const adjMap = buildAdjMap(roads);

    const spt = new Map<number, boolean>();

    const dist = new Map<number, number>();

    dist.set(1, 0);

    spt.set(1, true);

    for (const [v2, w] of adjMap.get(1)) {
        dist.set(v2, w);
    }

    while (unprocessed.size > 0) {
        let minV: number | undefined = undefined;

        for (const [v, d] of dist) {
            if (
                !spt.has(v)
                && (minV === undefined || d < dist.get(minV))
            ) {
                minV = v;
            }
        }

        if (minV === undefined) {
            break;
        }

        spt.set(minV, true);

        for (const [v2, w] of adjMap.get(minV)) {
            dist.set(v2, Math.min(dist.get(minV), w));     
        }
    }

    return Math.min(...Array.from(dist.values()));
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
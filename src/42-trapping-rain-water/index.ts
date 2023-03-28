export function trap(height: number[]): number {
    let peak = getNextPeak(height);

    if (peak < 0) {
        return 0;
    }

    let nextPeak = getNextHeighestPeak(height, peak);

    let result = 0;

    while (nextPeak > 0) {
        const maxHeight = Math.min(height[peak], height[nextPeak]);

        for (let i = peak + 1; i < nextPeak; i++) {
            if (height[i] < maxHeight) {
                result += maxHeight - height[i];
            }
        }

        peak = nextPeak;

        nextPeak = getNextHeighestPeak(height, peak);
    }

    return result;
};

function getNextHeighestPeak(height: number[], peak: number): number {
    let nextPeak = peak;
    let maxNextPeak = -1;

    while (true) {
        nextPeak = getNextPeak(height, nextPeak + 1);

        if (nextPeak < 0) {
            return maxNextPeak;
        }
    
        if (height[nextPeak] >= height[peak]) {
            return nextPeak;
        }

        if (maxNextPeak === - 1 || height[nextPeak] > height[maxNextPeak]) {
            maxNextPeak = nextPeak;
        }
    }
}

function getNextPeak(height: number[], from = 0): number {
    for (let i = from; i < height.length; i++) {
        if (
            (i === 0 || height[i - 1] <= height[i])
            && (i === height.length - 1 || height[i] > height[i + 1])
        ) {
            return i;
        }
    }

    return -1;
}

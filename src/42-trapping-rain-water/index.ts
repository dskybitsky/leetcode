export function trap(height: number[]): number {
    let peak = getNextPeak(height);

    if (peak < 0) {
        return 0;
    }

    let nextPeak = getNextPeak(height, peak + 1);

    let result = 0;

    while (nextPeak > 0) {
        const maxHeight = Math.min(height[peak], height[nextPeak]);

        for (let i = peak + 1; i < nextPeak; i++) {
            if (height[i] < maxHeight) {
                result += maxHeight - height[i];
            }
        }

        peak = nextPeak;

        nextPeak = getNextPeak(height, peak + 1);
    }

    return result;
};


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
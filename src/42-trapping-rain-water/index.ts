export function trap(height: number[]): number {
    let lastPeak: number | null = null;

    for (let i = 1; i < height.length; i++) {
        if (height[i - 1] > height[i]) {
            if (lastPeak === null) {
                lastPeak = i - 1;
            }
        }
    }
};

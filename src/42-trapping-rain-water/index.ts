export function trap(height: number[]): number {
    let ans = 0;

    if (!height.length) {
        return 0;
    }

    const leftMax = [height[0]];

    for (let i = 1; i < height.length; i++) {
        leftMax[i] = Math.max(height[i], leftMax[i - 1]);
    }

    const rightMax = new Array(height.length);

    rightMax[height.length - 1] = height[height.length - 1];

    for (let i = height.length - 2; i >= 0; i--) {
        rightMax[i] = Math.max(height[i], rightMax[i + 1]);
    }

    for (let i = 0; i < height.length; i++) {
        ans += Math.min(leftMax[i], rightMax[i]) - height[i];
    }

    return ans;
};
export function trap(height: number[]): number {
    let result = 0;

    let p1 = 0;
    let p2 = 0;

    while (p1 < height.length) {
        while (p1 < height.length - 1 && height[p1 + 1] >= height[p1]) {
            p1++;
        }

        if (p1 === height.length - 1) {
            return result;
        }

        let interResult = 0;

        p2 = p1 + 1;

        while (p2 < height.length && height[p2] < height[p1]) {
            interResult += height[p1] - height[p2];
            p2++;
        }

        if (p2 === height.length) {
            return result;
        }

        result += interResult;

        p1 = p2;
    }

    return result;
};

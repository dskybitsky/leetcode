export function canPlaceFlowers(flowerbed: number[], n: number): boolean {
    let left = n;
    let hasAdjacent = false;

    if (n <= 0) {
        return true;
    }

    for (let i = 0; i < flowerbed.length; i++) {
        hasAdjacent = (flowerbed[i - 1] ?? 0) === 1
            || (flowerbed[i + 1] ?? 0) === 1;

        if (flowerbed[i] === 0 && !hasAdjacent) {
            flowerbed[i] = 1;
            left--;
        }

        if (left === 0) {
            return true;
        }
    }

    return false;
};
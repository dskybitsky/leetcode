export function minPathSum(grid: number[][], node = [0, 0], sum = 0): number {
    const [nodeI, nodeJ] = node;

    if (nodeI === grid.length - 1 && nodeJ === grid[nodeI].length - 1) {
        return sum + grid[nodeI][nodeJ];
    }

    return Math.min(
        nodeI < grid.length - 1 ? minPathSum(grid, [nodeI + 1, nodeJ], sum + grid[nodeI][nodeJ]) : 200 * 200 * 100,
        nodeJ < grid[nodeI].length - 1 ? minPathSum(grid, [nodeI, nodeJ + 1], sum + grid[nodeI][nodeJ]) : 200 * 200 * 100,
    );
};
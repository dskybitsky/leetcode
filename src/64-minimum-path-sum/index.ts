export function minPathSum(grid: number[][]): number {
    const dp: number[][] = [];

    for (let i = 0; i < grid.length; i++) {
        dp[i] = [];

        for (let j = 0; j < grid[i].length; j++) {
            if (i === 0 && j === 0) {
                dp[i][j] = grid[i][j];
            } else if (i === 0) {
                dp[i][j] = grid[i][j] + dp[i][j - 1];
            } else if (j === 0) {
                dp[i][j] = grid[i][j] + dp[i - 1][j];
            } else {
                dp[i][j] = grid[i][j] + Math.min(dp[i][j - 1], dp[i - 1][j]);
            }
        }
    }

    return dp[grid.length - 1][grid[grid.length - 1].length - 1];
};
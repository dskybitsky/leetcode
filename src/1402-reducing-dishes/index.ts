let memo: number[][] = [];

export function maxSatisfaction(satisfaction: number[], from = 0): number {
    memo = [];

    for (let i = 0; i < satisfaction.length; i++) {
        memo[i] = [];
    }

    if (from > satisfaction.length - 1) {
        return 0;
    }

    satisfaction.sort((a, b) => a - b);

    return dp(satisfaction);
};

function dp(sat: number[], from = 0, q = 1): number {
    if (from > sat.length - 1) {
        return 0;
    }

    if (memo[from][q] !== undefined) {
        return memo[from][q];
    }

    const result = Math.max(
        sat[from] * q + dp(sat, from + 1, q + 1),
        dp(sat, from + 1, q)
    );

    memo[from][q] = result;

    return result;
}
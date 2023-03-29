export function maxSatisfaction(satisfaction: number[], from = 0): number {
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

    return Math.max(
        sat[from] * q + dp(sat, from + 1, q + 1),
        dp(sat, from + 1, q)
    );
}
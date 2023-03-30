let memo = [];

export function mincostTickets(days: number[], costs: number[], offset = 0): number {
    if (offset === 0) {
        memo = [];
    }

    if (memo[offset]) {
        return memo[offset];
    }

    if (offset >= days.length) {
        return 0;
    }

    const nextOffset1 = getNextOffset(1, days, offset);
    const nextOffset7 = getNextOffset(7, days, offset);
    const nextOffset30 = getNextOffset(30, days, offset);

    const result = Math.min(
        costs[0] + mincostTickets(days, costs, nextOffset1),
        costs[1] + mincostTickets(days, costs, nextOffset7),
        costs[2] + mincostTickets(days, costs, nextOffset30)
    );

    memo[offset] = result;

    return result;
};

function getNextOffset(daysPaid: number, days: number[], offset = 0): number {
    let i = offset;

    while (
        i < days.length 
        && (days[i] - days[offset] + 1 <= daysPaid)
    ) {
        i++;
    }

    return i;
}
export function maxSatisfaction(satisfaction: number[], from = 0): number {
    satisfaction.sort((a, b) => a - b);

    let result = 0;
    let suffixResult = 0;

    for (let i = satisfaction.length - 1; i >= 0; i--) {
        if (suffixResult + satisfaction[i] < 0)  {
            return result;
        }

        suffixResult += satisfaction[i];
        result += suffixResult;
    }

    return result;
};
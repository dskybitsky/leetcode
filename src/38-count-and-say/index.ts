export function countAndSay(n: number): string {
    if (n === 1) {
        return '1';
    }

    const prev = countAndSay(n - 1);

    let count = 1;

    let result = '';

    for (let i = 1; i < prev.length; i++) {
        if (prev[i] !== prev[i - 1]) {
            result = result + `${count}${prev[i - 1]}`;
            count = 1;
        } else {
            count++;
        }
    }

    if (count > 0) {
        result = result + `${count}${prev[prev.length - 1]}`;
    }

    return result;
}
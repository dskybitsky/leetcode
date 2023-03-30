export function divide(dividend: number, divisor: number): number {
    const minNum = -2147483648;
    const maxNum = 2147483647;

    const sign = dividend > 0 && divisor > 0 || dividend < 0 && divisor < 0 
        ? 1
        : -1;

    const resAbs = divideAbs(Math.abs(dividend), Math.abs(divisor));

    const res = sign > 0 ? resAbs : 0 - resAbs;

    const resTrunc = res < minNum 
        ? minNum
        : (res > maxNum ? maxNum : res);

    return resTrunc;
};

function divideAbs(dividend: number, divisor: number): number {
    if (divisor === 1) {
        return dividend;
    }

    let result = 0;

    while (dividend >= divisor) {
        let currentDivisor = divisor;
        let currentMult = 1;
    
        while (dividend >= currentDivisor) {
            dividend -= currentDivisor;

            result += currentMult;
            
            currentDivisor += currentDivisor;
            currentMult += currentMult;
        }
    }

    return result;
}
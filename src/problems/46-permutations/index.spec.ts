import { permute } from "./index";

describe('permute', () => {
    test('case 1', () => {
        expect(permute([1, 2, 3]))
            .toEqual([[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]);
    });
});
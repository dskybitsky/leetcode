import { BrowserHistory } from "./index";

describe('Browser History', () => {
    test('case 1', () => {
        const browserHistory = new BrowserHistory("leetcode.com");

        browserHistory.visit("google.com");
        browserHistory.visit("facebook.com");
        browserHistory.visit("youtube.com");

        expect(browserHistory.back(1)).toEqual("facebook.com");
        expect(browserHistory.back(1)).toEqual("google.com");
        expect(browserHistory.forward(1)).toEqual("facebook.com");

        browserHistory.visit("linkedin.com");
        
        expect(browserHistory.forward(2)).toEqual("linkedin.com");
        expect(browserHistory.back(2)).toEqual("google.com");
        expect(browserHistory.back(7)).toEqual("leetcode.com");
    });
});
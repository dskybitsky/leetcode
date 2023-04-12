class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        path_parts = path.split("/")

        for part in path_parts:
            if part == '/':
                continue

            if part == '.':
                continue

            if part == '..':
                if len(stack) > 0:
                    stack.pop()

                continue

            if len(part) == 0:
                continue

            stack.append(part)

        return "/" + "/".join(stack)
    
if __name__ == '__main__':
    sol = Solution()

    assert sol.simplifyPath("/home/") == "/home"
    assert sol.simplifyPath("/../") == "/"
    assert sol.simplifyPath("/home//foo/") == "/home/foo"
'''
####################################################################################################
####################################### Array implementation #######################################
####################################################################################################

Time Complexity:  O(1)              	(for each operation as using list indexes directly)
Space Complexity: O(n)              	(for history list)

class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]   # list of visited pages
        self.curr = 0               # current index

    def visit(self, url: str) -> None:
        # discard forward history
        self.history = self.history[:self.curr+1]
        self.history.append(url)
        self.curr += 1

    def back(self, steps: int) -> str:
        self.curr = max(0, self.curr - steps)
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        self.curr = min(len(self.history) - 1, self.curr + steps)
        return self.history[self.curr]

####################################################################################################
######################################## Doubly LinkedList #########################################
####################################################################################################
Time Complexity:  O(n)              	(for Doubly LinkedList)
Space Complexity: O(n)              	(for Doubly LinkedList)
'''

class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:
    def __init__(self, homepage: str):
        self.curr = ListNode(homepage)

    def visit(self, url: str) -> None:
        self.curr.next = ListNode(url, self.curr)
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        while steps and self.curr.prev:
            steps -= 1
            self.curr = self.curr.prev
        return self.curr.val

    def forward(self, steps: int) -> str:
        while steps and self.curr.next:
            steps -= 1
            self.curr = self.curr.next
        return self.curr.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

if __name__ == "__main__":
    # Paste this below your BrowserHistory class

    from typing import List, Tuple, Union

    def run_case(name: str,
                 homepage: str,
                 ops: List[Tuple[str, Union[str, int]]],
                 expected_returns: List[str]) -> None:
        """
        ops: sequence of ("visit", url) or ("back", steps) or ("forward", steps)
        expected_returns: only the strings returned by back/forward, in order.
        """
        bh = BrowserHistory(homepage)
        actual_returns: List[str] = []
        for op, arg in ops:
            if op == "visit":
                bh.visit(arg)  # no return collected
            elif op == "back":
                actual_returns.append(bh.back(arg))
            elif op == "forward":
                actual_returns.append(bh.forward(arg))
            else:
                raise ValueError(f"Unknown op: {op}")

        ok = actual_returns == expected_returns
        print(f"[{name}] {'PASS' if ok else 'FAIL'}")
        if not ok:
            print("  expected:", expected_returns)
            print("  actual  :", actual_returns)
        print("-" * 60)


    # Case 1: Prompt example
    run_case(
        name="Example from prompt",
        homepage="leetcode.com",
        ops=[
            ("visit", "google.com"),
            ("visit", "facebook.com"),
            ("visit", "youtube.com"),
            ("back", 1),
            ("back", 1),
            ("forward", 1),
            ("visit", "linkedin.com"),
            ("forward", 2),
            ("back", 2),
            ("back", 7),
        ],
        expected_returns=[
            "facebook.com",
            "google.com",
            "facebook.com",
            "linkedin.com",
            "google.com",
            "leetcode.com",
        ],
    )

    # Case 2: Back/forward overflow around a tiny history
    run_case(
        name="Tiny history with overflows",
        homepage="a.com",
        ops=[
            ("back", 1),  # no back available
            ("forward", 1),  # no forward available
            ("visit", "b.com"),  # forward cleared
            ("back", 5),  # clamp to start
            ("forward", 5),  # clamp to end
        ],
        expected_returns=[
            "a.com",
            "a.com",
            "a.com",
            "b.com",
        ],
    )

    # Case 3: Big back, then forward, then visit (clears forward), then overflow forward
    run_case(
        name="Clear forward after visit",
        homepage="start.com",
        ops=[
            ("visit", "a.com"),
            ("visit", "b.com"),
            ("visit", "c.com"),
            ("back", 3),  # go to start.com
            ("forward", 2),  # to b.com
            ("visit", "d.com"),  # clears forward
            ("forward", 10),  # stays on d.com
            ("back", 1),  # to b.com
        ],
        expected_returns=[
            "start.com",
            "b.com",
            "d.com",
            "b.com",
        ],
    )

    # Case 4: Repeated URLs + long back
    run_case(
        name="Repeated URLs and long back",
        homepage="home.com",
        ops=[
            ("visit", "x.com"),
            ("visit", "x.com"),
            ("back", 1),  # to first x.com
            ("back", 1),  # to home.com
            ("forward", 2),  # to second x.com
            ("back", 10),  # clamp to home.com
        ],
        expected_returns=[
            "x.com",
            "home.com",
            "x.com",
            "home.com",
        ],
    )

    # Case 5: Mixed moves with clamps
    run_case(
        name="Mixed moves",
        homepage="h.com",
        ops=[
            ("visit", "1.com"),
            ("visit", "2.com"),
            ("visit", "3.com"),
            ("back", 2),  # to 1.com
            ("forward", 1),  # to 2.com
            ("forward", 5),  # clamp to 3.com
            ("visit", "4.com"),
            ("back", 3),  # to 1.com
            ("forward", 3),  # to 4.com
        ],
        expected_returns=[
            "1.com",
            "2.com",
            "3.com",
            "1.com",
            "4.com",
        ],
    )

    # Case 6: Start -> forward (no-op), then normal nav, then forward to end, then more
    run_case(
        name="Forward from start + more navigation",
        homepage="leetcode.com",
        ops=[
            ("forward", 3),  # no forward yet
            ("visit", "a.co"),
            ("visit", "b.co"),
            ("back", 5),  # back to leetcode.com
            ("forward", 5),  # forward to b.co
            ("visit", "c.co"),  # clears forward
            ("back", 1),  # to b.co
            ("forward", 1),  # to c.co
        ],
        expected_returns=[
            "leetcode.com",
            "leetcode.com",
            "b.co",
            "b.co",
            "c.co",
        ],
    )

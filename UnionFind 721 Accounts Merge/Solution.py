'''
N = total number of accounts
E = total number of unique emails across all accounts

Time Complexity:
	Building Union-Find
	* Each email is processed at least once → E find calls
	* Each union does 2 finds
	 O(E · α(E)) ≈ O(E)

	Grouping emails by root
	* Iterates over all unique emails → E
	* Each find is amortized α(E)
	 O(E · α(E)) ≈ O(E)

	Sorting emails in each group
	* Worst case (all emails in one group):
	O(E log E)

	O(E · α(E) + E log E)
	≈ O(E log E)

Space Complexity:
	Union-Find storage
	* parent map → O(E) rank map → O(E)
	O(E)

	Grouped emails
	* Stores every email exactly once
	O(E)

	Auxiliary maps
	* email_to_name → O(E) Output list → O(E)
	O(E)

	O(E)
'''

from collections import defaultdict
from typing import List

class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, x: str) -> str:
        if x not in self.parent:
            self.rank[x] = 0
            self.parent[x] = x

        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: str, y: str):
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return

        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        email_to_name = {}

        # Phase 1: build DSU
        for name, *emails in accounts:
            for email in emails:
                email_to_name[email] = name
                uf.find(email)

            for i in range(1, len(emails)):
                uf.union(emails[0], emails[i])

        # Phase 2: group emails by root
        grouped = defaultdict(list)
        for email in uf.parent.keys():
            root = uf.find(email)
            grouped[root].append(email)

        # Phase 3: build result
        res = []
        for root, emails in grouped.items():
            name = email_to_name[root]
            res.append([name] + sorted(emails))

        return res

if __name__ == "__main__":
    solution = Solution()

    test_cases = {
        # 1. Provided Example 1 (basic merging)
        "example_1": [
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["John", "johnsmith@mail.com", "john00@mail.com"],
            ["Mary", "mary@mail.com"],
            ["John", "johnnybravo@mail.com"]
        ],

        # 2. Provided Example 2 (no overlaps at all)
        "example_2": [
            ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
            ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
            ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
            ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
            ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"]
        ],

        # 3. Single account only
        "single_account": [
            ["Alice", "alice@mail.com"]
        ],

        # 4. Multiple accounts, same name, no shared emails (should NOT merge)
        "same_name_no_overlap": [
            ["Bob", "bob1@mail.com"],
            ["Bob", "bob2@mail.com"],
            ["Bob", "bob3@mail.com"]
        ],

        # 5. Chain merging (A ↔ B ↔ C)
        "chain_merge": [
            ["Tom", "a@mail.com", "b@mail.com"],
            ["Tom", "b@mail.com", "c@mail.com"],
            ["Tom", "c@mail.com", "d@mail.com"]
        ],

        # 6. Duplicate emails inside same account
        "duplicate_emails_in_account": [
            ["Sam", "sam@mail.com", "sam@mail.com", "sam2@mail.com"]
        ],

        # 7. Same email used by different names (per problem, should merge anyway)
        "same_email_different_names": [
            ["Alex", "shared@mail.com"],
            ["Bob", "shared@mail.com"]
        ],

        # 8. Large merge group + isolated account
        "large_and_isolated": [
            ["John", "1@mail.com", "2@mail.com"],
            ["John", "2@mail.com", "3@mail.com"],
            ["John", "3@mail.com", "4@mail.com"],
            ["Mary", "mary@mail.com"]
        ],

        # 9. Multiple independent merge groups
        "multiple_groups": [
            ["A", "a1@mail.com", "a2@mail.com"],
            ["A", "a2@mail.com", "a3@mail.com"],
            ["B", "b1@mail.com"],
            ["B", "b1@mail.com", "b2@mail.com"],
            ["C", "c1@mail.com"]
        ],

        # 10. Emails already sorted vs unsorted input
        "sorted_vs_unsorted": [
            ["Zed", "z3@mail.com", "z1@mail.com", "z2@mail.com"],
            ["Zed", "z2@mail.com", "z4@mail.com"]
        ]
    }

    for name, accounts in test_cases.items():
        print(f"\n===== Test Case: {name} =====")
        result = solution.accountsMerge(accounts)
        print(result)

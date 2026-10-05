'''
Key idea

Each gene string is a node.
A mutation changes exactly one character, so two genes are connected if they differ at exactly one position.

For example:
		AACCGGTT
		   |
		   v
		AACCGGTA

Each mutation costs 1, so BFS gives us the minimum number of mutations.
We only need to consider mutations that exist in bank.

####################################################################################################

from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        bank = set(bank)

        if endGene not in bank:
            return -1

        queue = deque([(startGene, 0)])
        genes = "ACGT"

        while queue:
            current, mutations = queue.popleft()

            if current == endGene:
                return mutations

            for i in range(8):
                for gene in genes:
                    if gene == current[i]:
                        continue

                    mutated = current[:i] + gene + current[i + 1:]

                    if mutated in bank:
                        bank.remove(mutated)
                        queue.append((mutated, mutations + 1))

        return -1

####################################################################################################
Example

	startGene = "AACCGGTT"
	endGene   = "AAACGGTA"
	bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

BFS explores:
				AACCGGTT
					↓
				AACCGGTA
					↓
				AACCGCTA
					↓
				AAACGGTA

Therefore:		3

####################################################################################################
Why remove genes from bank?

This is important:					bank.remove(mutated)

Once we've visited a gene, there's no reason to visit it again. BFS has already reached it using the minimum possible number of mutations.

This prevents cycles such as:					A → B → A → B → ...

and keeps the search efficient.

####################################################################################################
Complexity

The gene length is fixed at 8, and there are only 4 possible characters.

For every visited gene:					8 positions × 4 characters = 32 possible mutations

So with N = len(bank):

Time: O(N × 8 × 4) → effectively O(N)

Space: O(N) for the BFS queue and bank set.

####################################################################################################
Pattern to remember

This is a classic BFS shortest-path problem where the graph is implicit:
> State → generate all valid one-step neighbors → BFS

The same pattern appears in problems like Word Ladder (127) and Open the Lock (752).
'''
from collections import defaultdict, deque

class Solution:
    def is_one_edit_distance(self, gene_a: str, gene_b: str) -> bool:
        return sum(a != b for a, b in zip(gene_a, gene_b)) == 1

    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        if endGene not in bank:
            return -1

        nodes = list(set(bank) | {startGene})
        graph = defaultdict(list)
        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                gene_a = nodes[i]
                gene_b = nodes[j]
                if self.is_one_edit_distance(gene_a, gene_b):
                    graph[gene_a].append(gene_b)
                    graph[gene_b].append(gene_a)

        queue = deque([startGene])
        visited = {startGene}
        mutations = 0

        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()
                if current == endGene:
                    return mutations

                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            mutations += 1
        return -1

if __name__ == "__main__":
    solution = Solution()

    # 1. Direct one-mutation case
    startGene = "AACCGGTT"
    endGene = "AACCGGTA"
    bank = ["AACCGGTA"]
    result = solution.minMutation(startGene, endGene, bank)
    print(result)  # Expected: 1

    # 2. Two mutations
    startGene = "AACCGGTT"
    endGene = "AAACGGTA"
    bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    result = solution.minMutation(startGene, endGene, bank)
    print(result)  # Expected: 2

    # 3. End gene is not in bank
    startGene = "AACCGGTT"
    endGene = "AACCGGTA"
    bank = []
    result = solution.minMutation(startGene, endGene, bank)
    print(result)  # Expected: -1

    # 4. Start and end are the same
    startGene = "AACCGGTT"
    endGene = "AACCGGTT"
    bank = []
    result = solution.minMutation(startGene, endGene, bank)
    print(result)  # Expected: 0

    # 5. End gene is same as start and bank contains unrelated genes
    startGene = "AACCGGTT"
    endGene = "AACCGGTT"
    bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    result = solution.minMutation(startGene, endGene, bank)
    print(result)  # Expected: 0

    # 6. One mutation, but bank contains many unrelated genes
    startGene = "AAAAAAAA"
    endGene = "AAAAAAAC"
    bank = [
        "CCCCCCCC",
        "GGGGGGGG",
        "TTTTTTTT",
        "AAAAAAAC",
        "ACAAAAAA"
    ]
    result = solution.minMutation(startGene, endGene, bank)
    print(result)  # Expected: 1

    # 7. Multiple mutations with a valid chain
    startGene = "AAAAAAAA"
    endGene = "CCCCCCCC"
    bank = [
        "CAAAAAAA",
        "CCAAAAAA",
        "CCCAAAAA",
        "CCCCAAAA",
        "CCCCCAAA",
        "CCCCCCAA",
        "CCCCCCCA",
        "CCCCCCCC"
    ]
    result = solution.minMutation(startGene, endGene, bank)
    print(result)  # Expected: 8

    # 8. Intermediate mutation missing from bank
    startGene = "AAAAAAAA"
    endGene = "AAAAAAAC"
    bank = [
        "AAAAAACC",
        "AAAAACCC",
        "AAAACCCC",
        "AAACCCCC",
        "AACCCCCC",
        "ACCCCCCC",
        "CCCCCCCC"
    ]
    result = solution.minMutation(startGene, endGene, bank)
    print(result)  # Expected: -1

    # 9. Several possible mutations, shortest path should be chosen
    startGene = "AAAAAAAA"
    endGene = "CCCCCCCC"
    bank = [
        "CAAAAAAA",
        "CCAAAAAA",
        "CCCAAAAA",
        "CCCCAAAA",
        "CCCCCCCC",

        # Longer/distracting path
        "AAAAAAAC",
        "AAAAAACC",
        "AAAAACCC",
        "AAAACCCC",
        "AAACCCCC",
        "AACCCCCC",
        "ACCCCCCC"
    ]
    result = solution.minMutation(startGene, endGene, bank)
    print(result)  # Expected: 5

    # 10. No possible mutation to endGene
    startGene = "AAAAAAAA"
    endGene = "CCCCCCCC"
    bank = [
        "CAAAAAAA",
        "CCAAAAAA",
        "CCCAAAAA",
        "CCCCAAAA"
        # Missing "CCCCCCCC"
    ]
    result = solution.minMutation(startGene, endGene, bank)
    print(result)  # Expected: -1

    # 11. End gene exists in bank but is unreachable
    startGene = "AAAAAAAA"
    endGene = "CCCCCCCC"
    bank = [
        "CAAAAAAA",
        "CCAAAAAA",
        "CCCAAAAA",
        "CCCCCCCC"
    ]
    result = solution.minMutation(startGene, endGene, bank)
    print(result)  # Expected: -1

    # 12. Mutation requires changing different positions
    startGene = "AACCGGTT"
    endGene = "TTGGCCAA"
    bank = [
        "TACCGGTT",
        "TTCGGTTT",
        "TTGGGTTT",
        "TTGGGCAA",
        "TTGGCCAA"
    ]
    result = solution.minMutation(startGene, endGene, bank)
    print(result)  # Expected: -1

    # 13. Duplicate entries in bank
    startGene = "AACCGGTT"
    endGene = "AACCGGTA"
    bank = [
        "AACCGGTA",
        "AACCGGTA",
        "AACCGGTA"
    ]
    result = solution.minMutation(startGene, endGene, bank)
    print(result)  # Expected: 1

    # 14. Bank contains startGene
    startGene = "AACCGGTT"
    endGene = "AACCGGTA"
    bank = [
        "AACCGGTT",
        "AACCGGTA"
    ]
    result = solution.minMutation(startGene, endGene, bank)
    print(result)  # Expected: 1

    # 15. Maximum-ish chain using only valid mutations
    startGene = "AAAAAAAA"
    endGene = "TTTTTTTT"
    bank = [
        "TAAAAAAA",
        "TTAAAAAA",
        "TTTAAAAA",
        "TTTTAAAA",
        "TTTTTAAA",
        "TTTTTTAA",
        "TTTTTTTA",
        "TTTTTTTT"
    ]
    result = solution.minMutation(startGene, endGene, bank)
    print(result)  # Expected: 8
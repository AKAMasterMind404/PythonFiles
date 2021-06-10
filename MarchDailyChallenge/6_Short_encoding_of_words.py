class Solution:
    def minimumLengthEncoding(self, words: list) -> int:
        words.sort(key=lambda x: len(x), reverse=True)
        root = {}
        output = 0

        for word in words:
            node = root
            valid = True

            for i in range(-1, -len(word) - 1, -1):
                next_node_candidate = {}
                next_node_final = node.setdefault(word[i], next_node_candidate)

                if id(next_node_candidate) == id(next_node_final):
                    valid = False

                node = next_node_final

            if not valid:
                output += len(word) + 1

        return output
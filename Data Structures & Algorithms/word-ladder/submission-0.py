class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
            
            words = set(wordList)

            if endWord not in words:
                return 0

            q = deque()
            q.append((beginWord, 1))

            while q:
                word, steps = q.popleft()

                if word == endWord:
                    return steps

                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":

                        newWord = word[:i] + ch + word[i+1:]

                        if newWord in words:
                            words.remove(newWord)
                            q.append((newWord, steps + 1))

            return 0
        
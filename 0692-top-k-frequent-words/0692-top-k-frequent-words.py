class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        freq=Counter(words)
        sort_words=sorted(freq.keys(),key=lambda word:(-freq[word],word))
        return sort_words[:k]
        
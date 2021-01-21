class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        word_idx = {word: i for i, word in enumerate(words)}
        res = []
        for i, word in enumerate(words):
            if word == "":
                continue
            # if the reversed word is also in the word_list
            if word[::-1] in word_idx and word_idx[word[::-1]] != i:
                res.append([i, word_idx[word[::-1]]])
            # if the word itself is a palindrome
            if word[::-1] == word and "" in word_idx:
                res.append([i, word_idx[""]])
                res.append([word_idx[""], i])
            
            for j in range(1, len(word)):
                # if reverse of the first j chars in word_list and the rest of word is a palindrome
                if word[j:] == word[j:][::-1] and word[:j][::-1] in word_idx:
                    res.append([i, word_idx[word[:j][::-1]]])
                # if the first j chars is a palindrome and the reverse of the rest of word is in word_idx
                if word[:j] == word[:j][::-1] and word[j:][::-1] in word_idx:
                    res.append([word_idx[word[j:][::-1]], i])
        return res


    # Solution 2
    # Trie
    # ref: https://fizzbuzzed.com/top-interview-questions-5/
    def isPalindrome(word):
            return True if word == word[::-1] else False
        
        class Trie:
            def __init__(self):
                self.children = defaultdict(Trie)
                self.endIndex = -1
                # store the word index that is a palindrome below the cur node 
                self.palindromesBelow = []
            
            def addWord(self, word, index):
                current = self
                for i, char in enumerate(reversed(word)):
                    # if the first len(word)-i chars is a palindrome, add index to current.palindromeBelow
                    if isPalindrome(word[:len(word)-i]):
                        current.palindromesBelow.append(index)
                    current = current.children[char]
                current.endIndex = index
            
        def makeTrie(words):
            trie = Trie()
            for i, word in enumerate(words):
                trie.addWord(word, i)
            return trie
        
        def getPalindrome(trie, word, index):
            pa_list = []
            match = True
            while word:
                # all past chars can be paired and the rest of word is a palindrome
                if trie.endIndex >= 0 and isPalindrome(word):
                    pa_list.append(trie.endIndex)
                # if word[0] not in trie.children, it can not pair with any word in word_list
                if word[0] not in trie.children:
                    match = False
                    break
                trie = trie.children[word[0]]
                word = word[1:]
            if match:
                # word find its reverse in the trie
                if trie.endIndex >= 0:
                    pa_list.append(trie.endIndex)
                # word matching ends, any word that is a palindrome below the current node is a valid pair
                pa_list.extend(trie.palindromesBelow)
            return [pa_idx for pa_idx in pa_list if pa_idx != index]
        
        trie = makeTrie(words)
        res = []
        for i, word in enumerate(words):
            pa_idx = getPalindrome(trie, word, i)
            for idx in pa_idx:
                res.append([i, idx])
        return res
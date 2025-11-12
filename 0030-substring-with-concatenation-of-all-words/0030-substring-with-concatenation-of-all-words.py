class Solution(object):
    def findSubstring(self, s, words):
        numWords = len(words)
        wordLength = len(words[0])
        frequency = {}
        currentFrequency = {}
        substrings = []

        for i in range(numWords):
            if words[i] in frequency:
                frequency[words[i]] += 1
            else:
                frequency[words[i]] = 1
        
        for i in range(max(wordLength % len(s), 1)):
            currentWord = ""
            currentFrequency = {}
            start = i
            wordsInSubstring = 0

            for j in range(start, len(s) - wordLength + 1, wordLength):
                currentWord = s[j: j + wordLength]
                wordsInSubstring += 1
                
                if currentWord in frequency:
                    if currentWord in currentFrequency:
                        currentFrequency[currentWord] += 1
                    else:
                        currentFrequency[currentWord] = 1

                    if currentFrequency == frequency:
                        substrings.append(start)
                        currentFrequency[s[start: start + wordLength]] -= 1
                        start += wordLength
                        wordsInSubstring -= 1
                    elif wordsInSubstring == numWords:
                        currentFrequency[s[start: start + wordLength]] -= 1
                        start += wordLength
                        wordsInSubstring -= 1
                else:
                    currentFrequency = {}
                    start = j + wordLength
                    wordsInSubstring = 0


        return substrings
        
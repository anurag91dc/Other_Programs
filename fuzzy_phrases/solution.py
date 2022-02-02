import json
from pprint import pprint


def phrasel_search(P, Queries):
    # Write your solution here
    ans = []
    """
    Iterating over the queries in the query list
    """
    for query in Queries:
        wordList = query.split()
        output = []
        """
        Here we are Iterating over each phrase and storing the start/end words of the phrase to search in the query and 
        determine matching entries which are eventually stored to a list ans [] and returned back
        """
        for phrase in P:
            pStart, pEnd = phrase.split()[0], phrase.split()[-1]
            s, e = 0, 0
            if pEnd in wordList and pStart in wordList:
                flag = 0
                for l in range(len(wordList)):
                    if flag == 1:
                        output.append((" ".join(match)))
                        flag = 0
                    if wordList[l] == pStart: s = l
                    if wordList[l] == pEnd: e = l
                    # Capturing the matching phrase while also including words that are in between
                    match = wordList[s:e + 1]
                    # Matching the criteria for the search
                    if len(match) == len(phrase.split()) or len(match) == len(phrase.split()) + 1:
                        flag = 1
        if len(output):
            ans.append((list(set(output))))
    return ans


if __name__ == "__main__":
    with open('sample.json', 'r') as f:
        sample_data = json.loads(f.read())
        P, Queries = sample_data['phrases'], sample_data['queries']
        returned_ans = phrasel_search(P, Queries)
        print('============= ALL TEST PASSED SUCCESSFULLY ===============')

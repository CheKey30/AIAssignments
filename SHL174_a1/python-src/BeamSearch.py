import StringDouble
import ExtractGraph
import heapq
import math

'''
Node is used to store the generated sentences
tokens : a list to store tokens in the sentence
prob: the probability of the sentence
score: the score of the sentence
'''
class Node:
    tokens = []
    prob = 0.0
    score = 0.0
    def __init__(self, tokens, prob,score):
        self.tokens = tokens
        self.prob = prob
        self.score = score

    def __lt__(self, other):
        if self.score<other.score:
            return True
        else:
            return False


class BeamSearch:

    graph = {}
    topK = []

    def __init__(self, input_graph):
        self.graph = input_graph
        self.topK = []
        return

    def beamSearchV1(self, pre_words, beamK, maxToken):
    	# Basic beam search.
        return self.beamSearchV2(pre_words,beamK,0,maxToken)

    def beamSearchV2(self, pre_words, beamK, param_lambda, maxToken):
        self.topK = []
    	# Beam search with sentence length normalization.
        # sentence is used to store the final best sentence
        sentence = ""
        # probability is used to store the highest score, not prob
        probability = float("-inf")
        # use a queue to do the BFS
        queue = [Node(pre_words.split(' '), 1.0, 0.0)]
        while queue:
            current = queue.pop(0)
            #if the sentence length is not longer than the maxToken and the last word has next words, then add words to sentence
            if len(current.tokens)<maxToken and current.tokens[-1] in self.graph.graph:
                for key in self.graph.graph[current.tokens[-1]]:
                    newNode = Node(current.tokens[:]+[key], current.prob*self.graph.graph[current.tokens[-1]][key], 0.0)
                    newNode.score = math.log(newNode.prob)/pow(len(newNode.tokens),param_lambda)
                    # use a heap to store the topK sentences
                    if len(self.topK)<beamK:
                        heapq.heappush(self.topK,newNode)
                        queue.append(newNode)
                    else:
                        if newNode.score>self.topK[0].score:
                            heapq.heapreplace(self.topK,newNode)
                            queue.append(newNode)
        # find the best sentence
        for node in self.topK:
            if node.score>probability:
                sentence = ' '.join(node.tokens)
                probability = node.score
        return StringDouble.StringDouble(sentence, probability)

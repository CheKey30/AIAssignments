import StringDouble
import ExtractGraph
import heapq
import math

class BeamSearch:

    graph = []
    topK = []

    def __init__(self, input_graph):
        self.graph = input_graph
        self.topK = []
        return

    def beamSearchV1(self, pre_words, beamK, maxToken):
    	# Basic beam search.
        return self.beamSearchV2(pre_words,beamK,0,maxToken)

    def beamSearchV2(self, pre_words, beamK, param_lambda, maxToken):
    	# Beam search with sentence length normalization.
        sentence = ""
        probability = 0.0
        queue = [([pre_words],1.0)]
        while queue is not None:
            current = queue.pop()
            if len(current[0]) > maxToken or current[0][-1] not in self.graph:
                continue
            for subGraph in self.graph[current[0][-1]]:
                currentProb = current[1]
                for key in subGraph:
                    newNode = (current[0][:].append(key),currentProb*subGraph[key])
                    if len(self.topK)<beamK:
                        heapq.heappush(self.topK,newNode)
                    else:
                        if newNode[1]>self.topK[0][1]:
                            heapq.heapreplace(self.topK, newNode)


        for list in self.topK:
            if list[1]>probability:
                sentence = ' '.join(list[0])
                probability = list[1]
        probability = (math.log(probability))/math.pow(maxToken,param_lambda)
        return StringDouble.StringDouble(sentence, probability)

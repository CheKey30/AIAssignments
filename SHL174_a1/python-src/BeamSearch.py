import StringDouble
from Beam import Beam
import math

class BeamSearch:

    graph = []

    def __init__(self, input_graph):
        self.graph = input_graph
        return


    def beamSearchV1(self, pre_words, beamK, maxToken):
    	# Basic beam search.
        return self.beamSearchV2(pre_words,beamK,0,maxToken)

    def beamSearchV2(self, pre_words, beamK, param_lambda, maxToken):
    	# Beam search with sentence length normalization.
        prev_beam = Beam(beamK)
        prev_beam.add(0.0,1.0,False,pre_words.split(" "))
        while True:
            current_beam = Beam(beamK)
            for(score, prob, complete, prefix) in prev_beam:
                if complete == True:
                    current_beam.add(score, prob, complete, prefix)
                else:
                    for key in self.graph.graph[prefix[-1]]:
                        if key == "</s>":
                            current_beam.add((1/pow(len(prefix[:]),param_lambda))*math.log(prob),
                                             prob,True,prefix[:])
                        else:
                            current_beam.add((1 / pow(len(prefix[:] + [key]), param_lambda)) * math.log(prob),
                                             prob * self.graph.graph[prefix[-1]][key], False, prefix[:] + [key])
            (best_score,best_prob,best_complete, best_prefix) = max(current_beam)
            if best_complete or len(best_prefix)-1 == maxToken:
                return StringDouble.StringDouble(' '.join(best_prefix), best_score)
            prev_beam = current_beam





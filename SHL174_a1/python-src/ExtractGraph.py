class ExtractGraph:

    # key is head word; value stores next word and corresponding probability.
    graph = {}

    sentences_add = "..\\data\\assign1_sentences.txt"

    def __init__(self):
        # Extract the directed weighted graph, and save to {head_word, {tail_word, probability}}
        file = open(self.sentences_add)
        line = file.readline()
        while line:
            tokens = line.split(' ')
            for i in range(len(tokens)-1):
                if tokens[i] in self.graph:
                    if tokens[i+1] in self.graph[tokens[i]]:
                        self.graph[tokens[i]][tokens[i+1]]+=1
                    else:
                        self.graph[tokens[i]][tokens[i+1]]=1
                else:
                    self.graph[tokens[i]] = {}
            line = file.readline()

        for key in self.graph.keys():
            total = 0
            for subkey in self.graph[key].keys():
                total+=self.graph[key][subkey]
            for subkey in self.graph[key].keys():
                self.graph[key][subkey] = self.graph[key][subkey]/total
        return


    def getProb(self, head_word, tail_word):
        if head_word in self.graph and tail_word in self.graph[head_word]:
            return self.graph[head_word][tail_word]
        else:
            return 0.0



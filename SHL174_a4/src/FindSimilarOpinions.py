import gensim.models.keyedvectors as word2vec


class FindSimilarOpinions:
    extracted_opinions = {}
    word2VecObject = []
    cosine_sim = 0

    def __init__(self, input_cosine_sim, input_extracted_ops):
        self.cosine_sim = input_cosine_sim
        self.extracted_opinions = input_extracted_ops
        word2vec_add = "..//data//assign4_word2vec_for_python.bin"
        self.word2VecObject = word2vec.KeyedVectors.load_word2vec_format(word2vec_add, binary=True)
        return

    def get_word_sim(self, word_1, word_2):
        return self.word2VecObject.similarity(word_1, word_2)

    def findSimilarOpinions(self, query_opinion):
        similar_opinions = {}
        term1, term2 = query_opinion.split(",")
        term1 = term1.strip()
        term2 = term2.strip()
        for key in self.extracted_opinions:
            keys = key.split(",")
            key1 = keys[0].strip()
            key2 = keys[1].strip()
            if key1 in self.word2VecObject.vocab and key2 in self.word2VecObject.vocab and self.get_word_sim(key1,term1)>self.cosine_sim and self.get_word_sim(key2,term2)>self.cosine_sim-0.2:
                similar_opinions[key] = self.extracted_opinions[key]
        return similar_opinions


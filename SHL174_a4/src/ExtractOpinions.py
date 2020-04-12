from stanfordcorenlp import StanfordCoreNLP
import re

class ExtractOpinions:
    # Extracted opinions and corresponding review id is saved in extracted_pairs, where KEY is the opinion and VALUE
    # is the set of review_ids where the opinion is extracted from.
    # Opinion should in form of "attribute, assessment", such as "service, good".
    extracted_opinions = {}

    def __init__(self):
        return

    def extract_pairs(self, review_id, review_content):
        # example data, which you will need to remove in your real code. Only for demo.
        # self.extracted_opinions = {'service, good': [1, 2, 5], 'service, excellent': [4, 6]}
        # print(review_content)
        texts = re.split(r"([.!?])", review_content)
        texts.append("")
        texts = ["".join(i) for i in zip(texts[0::2], texts[1::2])]
        nlp = StanfordCoreNLP(r'stanford-corenlp-full-2018-10-05')
        for text in texts:
            depends = nlp.dependency_parse(text.strip())
            tags = nlp.pos_tag(text.strip())
            # print(depends)
            # print(tags)
            for i in range(len(tags)):
                if tags[i][1]=='JJ':
                    for j in range(len(depends)):
                        if depends[j][2] == i+1 and tags[depends[j][1]-1][1]=="NN":
                            key = tags[depends[j][1]-1][0]+","+tags[i][0]
                            if key in self.extracted_opinions:
                                if review_id not in self.extracted_opinions[key]:
                                    self.extracted_opinions[key].append(review_id)
                            else:
                                self.extracted_opinions[key] = [review_id]
                        if depends[j][1] == i+1 and tags[depends[j][2]-1][1]=="NN":
                            key = tags[depends[j][2] - 1][0] + "," + tags[i][0]
                            if key in self.extracted_opinions:
                                if review_id not in self.extracted_opinions[key]:
                                    self.extracted_opinions[key].append(review_id)
                            else:
                                self.extracted_opinions[key] = [review_id]
        nlp.close()
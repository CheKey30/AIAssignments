import heapq
class Beam:
    def __init__(self, beam_width):
        self.heap = list()
        self.beam_width = beam_width

    def add(self, score, prob, complete, prefix):
        heapq.heappush(self.heap, (score, prob, complete, prefix))
        if len(self.heap) > self.beam_width:
            heapq.heappop(self.heap)

    def __iter__(self):
        return iter(self.heap)
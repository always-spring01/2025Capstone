'''
유사한 파일을 코사인 유사도로 탐지
'''
from sentence_transformers import util
from vectorization import Vectorization
from convert import Converter
import pickle

class Verification():
    def __init__(self, filename, threshold=0.7):
        self.convertdir = "./convert/"
        self.vectorizationdir = "./vectorization/"
        self.vectorization = Vectorization("sbert", "all-MiniLM-L6-v2")
        self.vectorization.process(filename)
        self.threshold = threshold
        with open(f"{self.convertdir}{filename}.pkl", 'rb') as f:
            self.sentences = pickle.load(f)
        with open(f"{self.vectorizationdir}{filename}.pkl", 'rb') as f:
            self.embeddings = pickle.load(f)
    
    def set_threshold(self, threshold):
        self.threshold = threshold
    
    def verify(self, query):
        qe = self.vectorization.vectorization(query)
        max_sim = 0
        max_idx = 0
        for idx in range(len(self.embeddings)):
            current_sim = util.cos_sim(self.embeddings[idx], qe)
            if current_sim > max_sim:
                max_sim = current_sim
                max_idx = idx
        if max_sim >= self.threshold:
            print(f"[verification.py] {float(max_sim)} : {self.sentences[max_idx]}")

# Debug
if __name__ == '__main__':
    converter = Converter()
    converter.convert("file2.txt")
    verification = Verification("file2", 0.5)
    while True:
        query = input("[verification.py] input : ")
        if (query == "exit"): break
        verification.verify(query)
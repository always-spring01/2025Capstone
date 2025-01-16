'''
전처리한 문서를 불러와 임베딩 벡터로 변환
'''
from sentence_transformers import SentenceTransformer
import os, pickle

class Vectorization():
    def __init__(self, type="sbert", name="all-MiniLM-L6-v2"):
        self.inputdir = "./convert/"
        self.outputdir = "./vectorization/"
        if type == "sbert":
            print("[vectorization.py] Set SBERT Model")
            self.model = SentenceTransformer(name)
        else:
            self.model = None
        os.makedirs(self.outputdir, exist_ok=True)
    
    def process(self, filename):
        with open(f"{self.inputdir}{filename}.pkl", 'rb') as f:
            file = pickle.load(f)
        embeddings = []
        for sentence in file:
            embeddings.append(self.model.encode(sentence))
        with open(f"{self.outputdir}{filename}.pkl", 'wb') as f:
            pickle.dump(embeddings, f)
        print(f"[vectorization.py] Embeddings complete : {len(embeddings)}/{len(file)}")
    
    def vectorization(self, query):
        return self.model.encode(query)

# Debug
if __name__ == '__main__':
    vectorization = Vectorization()
    vectorization.process("file1")
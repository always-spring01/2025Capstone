'''
다양한 형식의 문서를 txt 파일로 변환하고 전처리
'''
import os, shutil, pickle

hwp_ext = ['.hwp', '.hwpx']
plain_ext = ['.txt', '.py']

preprocess_list = ['', '<표>', '<그림>']

class Converter():
    def __init__(self):
        os.makedirs("./convert", exist_ok=True)
        self.inputdir = "./files/"
        self.targetdir = "./convert/"

    def convert(self, targetfile):
        name, extension = os.path.splitext(targetfile)
        if extension in hwp_ext: # 한글 문서
            self.convert_hwp(name, extension)
        if extension in plain_ext: # 변환이 필요하지 않은 문서
            self.convert_plain(name, extension)
        print("[convert.py] Convert file complete!")
        result = self.preprocess(name + ".txt")
        print("[convert.py] Preprocessing file complete!")
    
    def convert_hwp(self, name, extension):
        exefile = "hwp5txt"
        resultfile = name + '.txt'
        command = f"--output \"{self.targetdir}{resultfile}\" \"{self.inputdir}{name}{extension}\""
        print(f"[convert.py] {exefile} {command}")
        os.system(f"{exefile} {command}")
    
    def convert_plain(self, name, extension):
        shutil.copy(self.inputdir + name + extension, self.targetdir + name + '.txt')

    def preprocess(self, filename):
        result = []
        with open(f"{self.targetdir}{filename}", 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                # split_line = [part.strip() for part in line.split('.') if part.strip()]
                # result.extend(split_line)
                result.append(line)
        result = [item for item in result if item not in preprocess_list]
        with open(f"{self.targetdir}{filename[:-4]}.pkl", 'wb') as f:
            pickle.dump(result, f)
        return result

# Debug
if __name__ == '__main__':
    converter = Converter()
    converter.convert("file1.hwp") # temp file
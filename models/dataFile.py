import os,sys
sys.path.append('./model')

def getDataFile(fileName):
    base_dir = os.path.dirname(__file__)
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\','/')
    base = base_dir.split('/models')[0]
    dataFile_dir = base + '/data/'
    dataFile = dataFile_dir + str(fileName)
    return dataFile

if __name__ == "__main__":
    print(getDataFile("测试视频-sportguy.mp4"))
class Reader:
    def __init__(self,path):
        self.path=path

    def readFile(self):
        with open(self.path) as f:
            content = f.readlines()
        content = [x.split() for x in content]
        temp=[0]*len(content)
        for i in range(0,len(content)):
            for j in range(0,len(content[i])):
                if(content[i][j] == 'Q'):
                    temp[j]=i
        return temp
class GetData():
    def getdata(dir):
        raw_data = open(dir, 'r')
        if raw_data.mode == 'r':
            contents = raw_data.read()
        return contents

    def separarPorLineas(data):
        return data.split('\n')
    
    def getMatrizDeNumeros(data):
        return [[*map(int,list(line))] for line in data]
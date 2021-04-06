import os, json
from itertools import takewhile, repeat, groupby

class index:
    
    words={}

    def readwords(self, file):
        byte_stream = groupby(takewhile(lambda c: bool(c), map(file.read, repeat(1))), str.isspace)
        return ("".join(group).lower() for pred, group in byte_stream if not pred)

    def build(self, path):
        self.words = {}
        for root, dirs, files in os.walk(path):
            print(f'Examining {root}')
            for name in files:
                try:
                    filename = os.path.join(root, name)
                    with open(filename) as file:
                        for word in self.readwords(file):
                            self.addword(word, filename)
                except:
                    print(f'Error with {name}')
        with open('words.json', 'w') as file:
            file.truncate(0)
            file.write(json.dumps(self.words, indent = 4))

    def addword(self, word, file):
        try:
            self.words[word]['count'] += 1
        except:
            self.words[word] = {'count': 1, 'filecounts':{}}
        try:
            self.words[word]['filecounts'][file] += 1
        except:
            self.words[word]['filecounts'][file] = 1

    def search(self, word):
        result = {'result':'notfound', 'words':{}}
        searchword = word.lower()
        if len(searchword) > 2:
            try:
                word = self.words[searchword]
                result['result'] = 'success'
                result['words'][searchword] = word
            except:
                pass
            for word in self.words:
                if word.startswith(searchword):
                    result['words'][word] = self.words[word]
                    result['result'] = 'success'
        return result
    
    def search_files(self, word):
        searchresult = self.search(word)
        files = {}
        for word in searchresult['words']:
            resultword = searchresult['words'][word]
            for result in resultword['filecounts']:
                count = resultword['filecounts'][result]
                try:
                    files[result]['count'] += count
                except:
                    filename = os.path.basename(result)
                    files[result] = {'count':count, 'filename':filename, 'path':result}
        return files

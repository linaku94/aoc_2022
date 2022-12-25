from ast import literal_eval

class alternate_list():
    def __init__(self, a):
        self.a = a
    
    def __lt__(self, b):
        return True if self.check_pair(self.a,b()) else False
    
    def __gt__(self,b):
        return False if self.check_pair(self.a,b()) else True
    
    def __eq__(self, b):
        return True if self.check_pair(self.a,b()) is None else False

    def __iter__(self):
        return iter(self.a)

    def __repr__(self):
        return repr(self.a)

    def __call__(self):
        return self.a

    @staticmethod
    def check_pair(p0, p1):
        for i, element in enumerate(p0):
            try:
                if type(p0[i]) is not type(p1[i]):
                    if type(p0[i]) is not list:
                        p0[i] = [p0[i]]
                    else:
                        p1[i] = [p1[i]]
                if type(p0[i]) is list and type(p1[i]) is list:
                    contr = alternate_list.check_pair(p0[i],p1[i])
                    if contr != None:
                        return contr                    
                    continue
                if p0[i]>p1[i]:
                    return False
                elif p0[i]<p1[i]:
                    return True
            except:
                return False
        if len(p0)==len(p1):
            return None
        return True

pairs = []
indices = []
lists = []
with open('input.txt', 'r') as file:
    for i,line in enumerate(file.readlines()):
        if line == '\n':
            A = alternate_list.check_pair(*pairs)
            if A is None or A is True:
                indices.append((i+1)//3)
            pairs = []
        else:
            line = literal_eval(line.strip())
            pairs.append(line)
            lists.append(alternate_list(line))

print(f"part 1 sum of correct pair indices: {sum(indices)}")

divider_packets = [alternate_list([[2]]), alternate_list([[6]])]
lists.extend(divider_packets)
lists = sorted(lists)

indices = [lists.index(a)+1 for a in divider_packets]
print(f"part 2 decoder key: {indices[0]*indices[1]}")
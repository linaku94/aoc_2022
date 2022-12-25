from ast import literal_eval

class alternate_list(list):
    def __lt__(self, b):
        return True if self.check_pair(self,b) else False
    
    def __gt__(self,b):
        return False if self.check_pair(self,b) else True

    def __le__(self,b):
        return True if self<b or self==b else False
    
    def __ge__(self,b):
        return True if self>b or self==b else False
    
    def __eq__(self,b):
        return True if self.check_pair(self,b) is None else False

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
                    compare = alternate_list.check_pair(p0[i],p1[i])
                    if compare != None:
                        return compare                    
                    continue
                if p0[i]>p1[i]:
                    return False
                elif p0[i]<p1[i]:
                    return True
            except:
                return False
        return None if len(p0)==len(p1) else True

indices = []
lists = []
with open('input.txt', 'r') as file:
    for i,line in enumerate(file.readlines()):
        if line == '\n':
            if lists[-1]>=lists[-2]:
                indices.append((i+1)//3)
        else:
            line = literal_eval(line.strip())
            lists.append(alternate_list(line))

print(f"part 1 sum of correct pair indices: {sum(indices)}")

divider_packets = [alternate_list([[2]]), alternate_list([[6]])]
lists.extend(divider_packets)
lists = sorted(lists)

indices = [lists.index(a)+1 for a in divider_packets]
print(f"part 2 decoder key: {indices[0]*indices[1]}")
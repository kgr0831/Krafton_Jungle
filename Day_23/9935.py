class Stack :

    def __init__(self, kBombStr) :
        self.items = []
        self.bomb = kBombStr
        self.bLen = len(kBombStr)

    def top(self) :
        if len(self.items) <= 0 :
            return None
        return self.items[-1]
    
    def pop(self) :
        if len(self.items) <= 0 :
            return None
        item = self.items[-1]
        del self.items[-1]
        return item
    
    def size(self) :
        return len(self.items)

    def push(self, kItem) :
        if self.size() + 1 < self.bLen :
            self.items.append(kItem)
        else :
            rr = ''
            num = self.size() - self.bLen
            print(f"num = {num}")
            for i in range(num) :
                rr += self.items[i]
            rr += kItem
            print(f"rr = {rr}")
            if rr == self.bomb :
                print('bomb')
                for i in range(num) :
                    del self.items[i]
            else :
                self.items.append(kItem)
            print(f"items = {self.items}")
    def get(self) :
        result = ''
        for c in self.items :
            result += c
        if result == '' :
            result = 'FRULA'
        return result

_inputStr = input()
_bombStr = input()

_Stack = Stack(_bombStr)

for i in range(len(_inputStr)) :
    _Stack.push(_inputStr[i])

print(_Stack.get())
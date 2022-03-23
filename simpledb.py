class SimpleDB:
    def __init__(self):
        self.ht = {}
        self.stack = []
    def set(self, key, value):
        """set sets the value associated with the key"""
        if len(self.stack)>0:
            self.stack[-1][key] = (value,True)
            return
        self.ht[key] = value

    def get(self, key):
        """
        get returns the value associated with the key
        get should raise a KeyError if the key doesn't exist
        """
        for hts in self.stack[::-1]:
            if key in hts:
                v,c =  hts[key]
                if c is False:
                  raise KeyError(v)
                else:
                  return v
        return self.ht[key]

    def unset(self, key):
        """unset should delete the key from the db"""
        if len(self.stack) == 0:
            del self.ht[key]
            return 
        stk = self.stack[-1]
        stk[key] = (None,False)

    def begin(self):
        """begin starts a new transaction"""
        workinghash = {}
        self.stack.append(workinghash)
        

    def commit(self):
        """
        commit commits all transactions
        it should raise an Exception if there is no ongoing transaction
        """
        if len(self.stack) == 0:
            raise
        while len(self.stack) > 0:
            hts = self.stack.pop(0)
            for k,(v,c) in hts.items():
                if c:
                    self.ht[k] = v
                else:
                    del self.ht[k]
       

    def rollback(self):
        """
        rollback undoes the most recent transaction
        it should raise an Exception if there is no ongoing transation
        """
        if len(self.stack) == 0:
            raise Exception
        self.stack.pop()
    def debug(self):
        print ("HASH TABLE:", self.ht)
        print ("STACKS : ", self.stack)


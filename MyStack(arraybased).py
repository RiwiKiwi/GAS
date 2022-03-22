class StackItemType:
    # making another class for the newItem
    def __init__(self, value):
        self.value = value #this is the thing you want to insert in your stack

class MyStack:
    #createStack with max_size
    def __init__(self, max_size):
        '''
        Maakt een lege stack aan
        preconditie: /
        postconditie: maakt een lege stack
        :param max_size: maximum groote van je stack want het is arraybased
        '''
        self.max_size = max_size
        self.myStack = [None] * max_size #name of the Stack = items
        self.size = 0

    #Implementation of destroyStack doesn't matter here because of the automatic garbage collection for Python

    #isEmpty function
    def isEmpty(self):
        '''
        Bepaalt of een stack leeg is
        preconditie: er is al een stack aangemaakt
        postconditie: bepaalt of de stack leeg is
        :return:(boolean) geeft true als het leeg is en anders false
        '''
        if self.size == 0 : # if the size  is Nothing
            return True #gives true if it's Empty
        else: #otherwise
            return False #else False if it isn't Empty

    # push function with newItem of the type StackItemType (see above)
    def push(self, newItem):
        '''
        Voegt het nieuwe item toe op het top van de stack
        preconditie: de stack is niet vol want anders kunnen we niets toevoegen
        postconditie: er wordt newItem toegevoegd aan de top van de stack
        :param newItem:the element newItem van QueueItemType
        :return:(boolean) geeft true als het gelukt is en anders false
        '''
        if self.size == len(self.myStack): #if the stack is full you can't insert anything
            return False #so return False
        else: #now we know that the stack isn't full we can insert our newItem
            self.myStack[self.size]= newItem # Translation: list[0] = newItem
            self.size += 1 #next time is our size now 1
            return True
    #pop function
    def pop(self):
        '''
        Verwijderd de top van de stack (#het laatst toegevoegde element)
        preconditie: de top is niet leeg
        postconditie: de top van de stack wordt verwijderd
        :return:
        '''
        # same implementation for the queue and stack
        save_value = self.myStack[-1]
        if save_value != None:
            del self.myStack[-1]
            self.myStack.append(None)
            self.size-= 1
            return save_value, True
        else:
            return False,False

    #getTop function
    def getTop(self):
        '''
         Plaatst de top van de stack in "Stacktop"
        preconditie: er is een element bij de top
        postconditie: er zal niets gebeuren en enkel de top zal eruit gehaald worden
        :return: (boolean) geeft true als het gelukt is en anders false
        '''
        if (not self.isEmpty()):  # if the stack isn't empty
            top = 0 # variable for getting the top
            for x in range(self.max_size - 1, -1, -1): #reverse the loop by -1
                if self.myStack[x] != None: #if the upcoming index on the stack  isn't empty
                    top = self.myStack[x] # that index  will be your top
                    break # so stop here
            return top, True # give that top and return True if it's done
        else:#otherwise
            return False, False #give false

    #save function
    def save(self):
        '''
        Print de stack terug
        preconditie: er is een stack aanwezig
        postconditie: de stack wordt terug gegeven
        :param: /
        :return: je gemaakte stack
        '''

        lijst= []
        for i in range(self.size):
            lijst.append(self.myStack[i])
        return lijst

    #load function
    def load(self, data):
        '''
        Voeg elementen bij in je stack
        preconditie: er is een stack aanwezig en die is leeg
        postconditie: voeg data van index i in de queue
        :param data: je opgeslagen info
        :return:/
        '''
        if len(data) > self.size:
            self.size = len(data)
        self.myStack = [None] * self.size
        for i in range(len(data)):
            self.myStack[i] = data[i]



if __name__ == "__main__":
    s = MyStack(2)
    print(s.isEmpty())
    print(s.getTop()[1])
    print(s.pop()[1])
    print(s.push(2))
    print(s.push(4))
    print(s.push(1))
    print(s.isEmpty())
    print(s.pop()[0])
    s.push(5)
    print(s.save())

    s.load(['a','b','c'])
    print(s.save())
    print(s.pop()[0])
    print(s.save())
    print(s.getTop()[0])
    print(s.save())




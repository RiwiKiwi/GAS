class QueueItemType:
    # making another class for the newItem
    def __init__(self, value):
        self.value = value #this is the thing you want to insert in your queue
        self.next = None
class MyQueue:
    #createQueue with max_size (the constructor)
    def __init__(self, max_size):
        '''
        Maakt een lege queue aan
        preconditie: /
        postconditie: maakt een lege queue
        :param max_size: de maximumgroote van de queue
        :return: /
        '''
        self.max_size = max_size
        self.myQueue = [None] * max_size
        self.size = 0  #size at start will be 0

    #Implementation of destroyQueue doesn't matter here because of the automatic garbage collection for Python

    # isEmpty function
    def isEmpty(self):
        '''
        Bepaalt of de queue leeg is 
        preconditie: er is al een queue aangemaakt
        postconditie: bepaalt of de queue leeg is
        :return: (boolean) geeft true als het leeg is en anders false
        '''
        if self.size == 0: # check if your queue is none
            return True
        else: #otherwise
            return False

    #enqueue function
    def enqueue(self, newItem):
        '''
        Voegt het nieuwe item toe aan het eind (staart) van de queue
        preconditie: de queue is niet vol want anders kunnen we niets toevoegen
        postconditie: er wordt newItem toegevoegd aan he eind van queue
        :param newItem: the element newItem van QueueItemType
        :return: (boolean) geeft true als het gelukt is en anders false
        '''
        if self.size <= self.max_size: # aslong your size is smaller than your max.size....
            self.myQueue[self.size]= newItem # #insert that newItem at the index= size
            self.size += 1 # everytime +1
            return True #true if it's done
        else: #otherwise
            return False #false if it's not done
    #dequeue function
    def dequeue(self):
        '''
        Verwijderd de kop van de queue (#het eerst toegevoegde element)
        preconditie: de kop van de queue is niet leeg
        postconditie: de kop van de queue wordt verwijderd
         :param: /
        :return: (boolean) geeft true als het gelukt is en anders false
        '''
        save_value= self.myQueue[0]

        if save_value != None:
            del self.myQueue[0]
            self.myQueue.append(None)
            self.size-= 1
            return save_value, True

        else:#otherwise
            return False, False

    #getFront function
    def getFront(self):
        '''
        Plaatst de kop van de queue in Queuefront
        preconditie: er is een element bij de kop
        postconditie: er zal niets gebeuren en enkel de kop eruit gehaald worden
         :param: /
        :return: (boolean) geeft true als het gelukt is en anders false
        '''
        if (self.isEmpty()): #if the queue is empty you can't get the top
            return False,False #so return false
        else:
            return self.myQueue[0],True

    #save function
    def save(self):
        '''
        Print de queue terug
        preconditie: er is een queue aanwezig
        postconditie: de queue wordt terug gegeven
         :param: /
        :return: je gemaakte queue
        '''
        lijst = []
        for i in range(self.size-1, -1, -1): #reverse loop
            lijst.append(self.myQueue[i])
        return lijst
    #load function
    def load(self, data):
        '''
        Voeg elementen bij in je queue
        preconditie: er is een queue aanwezig en die is leeg
        postconditie: voeg data van index i in de queue
        :param data: je opgeslagen info
        :return:/
        '''
        self.size = 0
        self.myQueue = [None] * len(data) #initialize the queue
        for i in reversed(data):
            self.enqueue(i)


q = MyQueue(10)
print(q.isEmpty())
print(q.getFront()[1])
print(q.dequeue()[1])
print(q.enqueue(2))
print(q.enqueue(4))
print(q.save())
print(q.isEmpty())
print(q.dequeue()[0])
q.enqueue(5)
print("5 is enqueue")
print(q.save())

q.load(['a', 'b', 'c'])
print(q.save())
print(q.dequeue()[0])
print(q.save())
print(q.getFront()[0])
print(q.save())



























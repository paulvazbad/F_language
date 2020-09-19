class SymbolTable:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.elements = {}

    def insert(self,id, tipo, attributes):
        newE = TableElement(id=id,tipo=tipo,attributes=attributes)
        self.elements[id] = newE
    
    def lookup(self,id):
        query = self.elements.get(id)
        if(query is not None):
            return query
        else:
            return None
    
    def update(self,id,value):
        if(self.elements[id] is None):
            raise Exception(id + " not found in SymbolTable")
        self.elements[id].attributes = value

    def delete(self,id):
        success = self.elements.pop(id,d=None)
        return success
    
    def print(self):
        for element in self.elements.values():
            element.print()

''' Definition of each element on the table'''

class TableElement:
    
    def __init__(self,tipo,id,attributes):
        #super().__init__(*args, **kwargs)
        self.tipo =tipo
        self.id = id
        self.attributes = attributes
   
    
    def print(self):
        print("<type: {0}, id: {1}, attributes: {2}>".format(self.tipo,self.id,self.attributes))
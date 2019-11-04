from SymbolTable import SymbolTable


SymbolT = SymbolTable()
SymbolT.print()
SymbolT.insert(id="var", tipo="int",attributes=None)
SymbolT.print()
SymbolT.insert(id="a", tipo="double",attributes=None)
SymbolT.insert(id="function", tipo="void",attributes=None)
SymbolT.print()
print(SymbolT.lookup(id="a"))

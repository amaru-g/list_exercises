# lista de compras para una ensalada
# Remover un item de la lista cuando el item sea adquirido.

ensalada= ['lechuga','tomate','queso','salsa']
print("debes comprar los siguientes ingredientes:",ensalada)
elemento=input("que acabas de comprar?")
ensalada.remove(str(elemento))
print("aun te queda comprar...",ensalada)


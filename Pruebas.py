from queue import Queue
from typing import List
from typing import Dict
from typing import Union

stockProductos = { 'Manzana': 10, 'Leche': 5, 'Pan': 3,'Factura': 0 }
pedido1 = { 'id': 1, 'cliente': 'Juan', 'productos': {'Manzana': 2, 'Pan': 4, 'Factura': 6} }
precio_productos = { 'Manzana': 3.5, 'Leche': 5.5, 'Pan': 3.5, 'Factura': 2.75 }


def prueba1():
    for producto in stockProductos:
        print(producto)
        print(stockProductos[producto])
        print()

def prepararEntrega(pedido: Dict[str, Union[int, str, Dict[str, int]]]) -> Dict[str, Union[int, str, float, Dict[str, int]]]:
    entrega = {}
    entrega['id'] = pedido['id']
    entrega['cliente'] = pedido['cliente']
    entrega['productos'] = pedido['productos']
    entrega['precio_total'] = 0
    entrega['estado'] = 'completo'
    return entrega

def prueba2(pedido):
    E = prepararEntrega(pedido)
    print("!!!!")
    print(E)
    print("!!!!")

Test1 = Queue()

print(Test1.qsize())
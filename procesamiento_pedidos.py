from queue import Queue
from typing import List
from typing import Dict
from typing import Union
import json

# ACLARACIÓN: El tipo de "pedidos" debería ser: pedidos: Queue[Dict[str, Union[int, str, Dict[str, int]]]]
# Por no ser soportado por la versión de CMS, usamos simplemente "pedidos: Queue"


# stock productos = { ”Manzana”: 10, ”Leche”: 5, ”Pan”: 3, ”Factura”: 0 }
# precio productos = { ”Manzana”: 3.5, ”Leche”: 5.5, ”Pan”: 3.5, ”Factura”: 2.75 }
# pedido = { ‘id‘: 1, ‘cliente‘: ‘Juan‘, ‘productos‘: {‘Manzana‘: 2, ‘Pan‘: 4, ‘Factura‘: 6} }
# entrega = { ‘id‘: 1, ‘cliente‘: ‘Juan‘, ‘productos‘: {‘Manzana‘: 2, ‘Pan‘: 3, ‘Factura‘: 0} ‘precio_total‘: 17.5, ‘estado‘: ‘incompleto‘}
# pedido_procesado = [{ ‘id‘: 21, ‘cliente‘: ‘Gabriela‘, ‘productos‘: {‘Manzana‘: 2} ‘precio_total‘: 7.0, ‘estado‘: ‘completo‘}, 
#                     {‘id‘: 1, ‘cliente‘: ‘Juan‘, ‘productos‘: {‘Manzana‘: 2, ‘Pan‘: 3, ‘Factura‘: 0} ‘precio_total‘: 17.5, ‘estado‘: ‘incompleto‘}]


def procesamiento_pedidos(pedidos: Queue, stock_productos: Dict[str, int], precios_productos: Dict[str, float]) -> List[Dict[str, Union[int, str, float, Dict[str, int]]]]:
  res : List[Dict[str, Union[int, str, float, Dict[str, int]]]] = []
  
  def prepararEntrega(pedido: Dict[str, Union[int, str, Dict[str, int]]]) -> Dict[str, Union[int, str, float, Dict[str, int]]]:
    entrega = {}
    entrega['id'] = pedido['id']
    entrega['cliente'] = pedido['cliente']
    entrega['productos'] = pedido['productos']
    entrega['precio_total'] = 0
    entrega['estado'] = 'completo'
    return entrega

  while not pedidos.empty():
    pedidoActual = pedidos.get() 
    entrega = prepararEntrega(pedidoActual)

    for producto in stock_productos:
    
      if producto in entrega['productos']:
      
        if stock_productos[producto] >= entrega['productos'][producto]:
          stock_productos[producto] = stock_productos[producto] - entrega['productos'][producto]
          entrega['precio_total'] += precios_productos[producto] * entrega['productos'][producto]
        
        else:
          entrega['productos'][producto] = stock_productos[producto]
          entrega['precio_total'] += precios_productos[producto] * entrega['productos'][producto]
          entrega['estado'] = 'incompleto'
          stock_productos[producto] = 0
    
    res.append(entrega)

  return res


def test():
  pedidos = Queue()
  pedidos.put({"id":21,"cliente":"Gabriela", "productos":{"Manzana":2}})
  pedidos.put({"id":1,"cliente":"Juan","productos":{"Manzana":2,"Pan":4,"Factura":6}})
  stock_productos = {"Manzana":10, "Leche":5, "Pan":3, "Factura":0}
  precios_productos = {"Manzana":3.5, "Leche":5.5, "Pan":3.5, "Factura":5}
  R = procesamiento_pedidos(pedidos, stock_productos, precios_productos)
  pedido_procesado = [{'id': 21, 'cliente': 'Gabriela', 'productos': {'Manzana': 2}, 'precio_total': 7.0, 'estado': 'completo'}
                      ,{'id': 1, 'cliente': 'Juan', 'productos': {'Manzana': 2, 'Pan': 3, 'Factura': 0}, 'precio_total': 17.5, 'estado': 'incompleto'}]
  for i in range(len(R)):
    print(R[i])
    print(pedido_procesado[i])
    print(R[i] == pedido_procesado[i])
    print()
  
  print(pedidos.empty())
  R2 = procesamiento_pedidos(pedidos, stock_productos, precios_productos)
  print(R2)
  pedidos.put({"id":14,"cliente":"Jose", "productos":{}})
  R3 = procesamiento_pedidos(pedidos, stock_productos, precios_productos)
  print(R3)


test()


# if __name__ == '__main__':
#   pedidos: Queue = Queue()
#   list_pedidos = json.loads(input())
#   [pedidos.put(p) for p in list_pedidos]
#   stock_productos = json.loads(input())
#   precios_productos = json.loads(input())
#   print("{} {}".format(procesamiento_pedidos(pedidos, stock_productos, precios_productos), stock_productos))

# Ejemplo input  
# pedidos: [{"id":21,"cliente":"Gabriela", "productos":{"Manzana":2}}, {"id":1,"cliente":"Juan","productos":{"Manzana":2,"Pan":4,"Factura":6}}]
# stock_productos: {"Manzana":10, "Leche":5, "Pan":3, "Factura":0}
# precios_productos: {"Manzana":3.5, "Leche":5.5, "Pan":3.5, "Factura":5}
from queue import Queue

# El tipo de fila debería ser Queue[int], pero la versión de python del CMS no lo soporta. Usaremos en su lugar simplemente "Queue"

def avanzarFila(fila: Queue, min: int):
  noResuelto : Queue = Queue()
  numero = fila.qsize()

  for contador in range(min + 1):

    if contador % 4 == 0: # Sumar persona a la fila
      numero += 1
      fila.put(numero)
    
    if contador % 10 == 1 and not fila.empty(): # Caja1
      fila.get() 
    
    if contador % 4 == 3 and not fila.empty(): # Caja2
      fila.get()
    
    if contador % 4 == 2 and not fila.empty(): #Caja3
      noResuelto.put(fila.get())
    
    if contador % 4 == 1 and not noResuelto.empty():
      fila.put( noResuelto.get() )
  
  return fila


# def test(n, m):
#   Test1 = Queue()
#   for i in range(1,n+1):
#     Test1.put(i)
#   print(Test1.queue)
#   T1 = avanzarFila(Test1, m)
#   print(list(T1.queue))

# test(3,5)



if __name__ == '__main__':
  fila: Queue = Queue()
  fila_inicial: int = int(input())
  for numero in range(1, fila_inicial+1):
    fila.put(numero)
  min: int = int(input())
  avanzarFila(fila, min)
  res = []
  for i in range(0, fila.qsize()):
    res.append(fila.get())
  print(res)


# Caja1: Empieza a atender 10:01, y atiende a una persona cada 10 minutos
# Caja2: Empieza a atender 10:03, atiende a una persona cada 4 minutos
# Caja3: Empieza a atender 10:02, y atiende una persona cada 4 minutos, pero no le resuelve el problema y la persona debe volver a la fila (se va al final y tarda 3 min en llegar. Es decir, la persona que fue atendida 10:02 vuelve a entrar a la fila a las 10:05)
# La fila empieza con las n personas que llegaron antes de que abra el banco. Cuando abre (a las 10), cada 4 minutos llega una nueva persona a la fila (la primera entra a las 10:00)


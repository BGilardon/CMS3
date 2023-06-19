from typing import List
from typing import Dict
import json

def unir_diccionarios(a_unir: List[Dict[str,int]]) -> Dict[str,List[str]]:
  res : Dict = {}
  for dic in a_unir:
    for key in dic:
      if key not in res:
        res[key] = [dic[key]]
      else:
        res[key].append(dic[key])
  return res


# def test():
#   def testear(test):
#     print(test)
#     print(unir_diccionarios(test))
#     print()
#   test1 = [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'a': 5}]
#   testear(test1)
#   test2 = [{}]
#   testear(test2)
#   test3 = [{},{'a':5},{}]
#   testear(test3)
#   test4 = [{'a':6},{'b':5},{'a':6},{'a':6},{'k':5}]
#   testear(test4)

if __name__ == '__main__':
  x = json.loads(input()) # Ejemplo de input: [{"a":2},{"b":3,"a":1}]
  print(unir_diccionarios(x))
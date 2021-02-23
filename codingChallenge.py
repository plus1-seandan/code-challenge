def solution(products): 
  #solves the problem in linear time o(n) using a hashmap. 
  def createMapping(products): 
    hashMap = {}
    for product in products: 
      id = product['parent_id']
      if id == None:
        id = -1 
      
      if id not in hashMap:
        hashMap[id] = []
      hashMap[id].append(product)
    return hashMap 
      
  #create dictionary of parent_ids 
  hashMap = createMapping(products); 
  ans = [] 

  #pop the initial roots and add to queue 
  queue = hashMap[-1]
  #remove from dictionary after adding to queue 
  del hashMap[-1]

  while queue: 
    product = queue.pop(0)
    ans.append(product)
    
    #add the products children to the queue 
    if product['id'] in hashMap: 
      queue += hashMap[product['id']]
      #delete from dictionary after adding to queue 
      del hashMap[product['id']]
  return ans 

#test 
'''
products = [
  {
    "name": "Accessories",
    "id": 1,
    "parent_id": 20,
  },
  {
    "name": "Watches",
    "id": 57,
    "parent_id": 1
  },
  {
    "name": "Men",
    "id": 20,
    "parent_id": None,
  }
]

print(solution(products))
'''
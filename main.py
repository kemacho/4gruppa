class TRoad:

  from pprint import pprint
  
  def __init__(self, road, n, new_road):
    self.road = list(road)
    self.n = n
    self.new_road = new_road


  def __light_change(self, trigger1 = False, trigger2 = False):

    if trigger2 == True:
      O = []
      for k in range(len(self.road)):
        if self.road[k] == 'O':
          O.append(k)
      #if O != []:
        #self.__move_car()
        #self.__add()
        #print("alo alo")
      for l in range(len(O)):
        self.road[O[l]] = 'R'
    
    if trigger1 == True:
       GR = []
       RE = []
       for k in range(len(self.road)):
        if self.road[k] == 'G':
          GR.append(k)
        elif self.road[k] == 'R':
          RE.append(k)

       for l in range(len(GR)):
         self.road[GR[l]] = 'O'
       for l in range(len(RE)):
        self.road[RE[l]] = 'G'

  
  def __move_car(self, trigger3 = False):
    
    car_ind = self.road.index('C')   
      
    if trigger3 == True: 
      self.road[car_ind + 1] = 'C'
      self.road[car_ind] = 'G'
      self.__add()
    else:
      self.road[car_ind + 1] = 'C'
      self.road[car_ind] = '.'
      self.__add()    
  

  def __add(self):
    str1 = ''
    str1 = ''.join(self.road) + ' ' + str(self.n - 1)
    self.new_road.append(str1)

  def __print(self):
    for i in range(len(self.new_road)):
      print(self.new_road[i])
       

  def simulate_traffic(self):
    
    i = 0
    cnt = 1
    trigger = False
    trigger_g = False
    
    print(''.join(self.road), self.n)
    
    while i < self.n:
      
      #позиция машины
      car_ind = self.road.index('C')
      
      #выход из цикла
      if car_ind == len(self.road) - 1:
        break

      #смена светофоров
      if trigger == True:
        self.__light_change(trigger2 = True)
        trigger = False
      if cnt == 5:
        self.__light_change(trigger1 = True)
        cnt = 0
        trigger = True

      #движение машины
      if trigger_g == True:
        if self.road[car_ind + 1] == '.':
          self.__move_car(trigger3 = True)
          trigger_g = False
        elif self.road[car_ind + 1] == 'G':
          self.__move_car(trigger3 = True)
          trigger_g = True
        else:
          self.__add()
          trigger_g = False
      else:
        if self.road[car_ind + 1] == '.':
          self.__move_car()
        elif self.road[car_ind + 1] == 'G':
          self.__move_car()
          trigger_g = True
        else:
          self.__add()
        
      #счетчики
      self.n -= 1
      cnt += 1
     
    self.__print()


T = TRoad(road="C...R..R...R..GG....G", n=40, new_road = [])
T.simulate_traffic()

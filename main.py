class TRoad:
  
  def __init__(self, road, n):
    self.road = list(road)
    self.n = n


  def __light_change(self, trigger = False, trigger1 = False):

    if trigger1 == True:
      O = []
      for k in range(len(self.road)):
        if self.road[k] == 'O':
          O.append(k)
        for l in range(len(O)):
          self.road[O[l]] = 'R'
    
    if trigger == True:
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



  

  
  def __move_car(self):
    
    car_ind = self.road.index('C')   
      
    if self.road[car_ind + 1] == '.':
      self.road[car_ind + 1] = 'C'
      self.road[car_ind] = '.'

    elif self.road[car_ind + 1] == 'G':
      self.road[car_ind + 1] = 'C'
      self.road[car_ind] = '.'
      

  #def __back_light(self):
    
    #car_ind = self.road.index('C') 
    
#    if self.road[car_ind + 1] == '.':
#      self.road[car_ind + 1] = 'C'
#      self.road[car_ind] = 'G'
#
#    elif self.road[car_ind + 1] == 'G':
#      self.road[car_ind + 1] = 'C'
#      self.road[car_ind] = 'G'
  

  def __print(self):
    print(''.join(self.road), self.n)


  
  def simulate_traffic(self):
    
    i = 0
    cnt = 1
    trigger2 = False
    
    print(''.join(self.road), self.n)
    
    while i < self.n:
      
      car_ind = self.road.index('C') 
      if car_ind == len(self.road) - 1:
        break
      
      if trigger2 == True:
        self.__light_change(trigger1 = True)
        trigger2 = False
      if cnt == 5:
        self.__light_change(trigger = True)
        cnt = 0
        trigger2 = True
        
      self.__move_car()
      self.__print()
      
      self.n -= 1
      cnt += 1
     

T = TRoad(road="C...R...R.R..GG....G", n=40)
T.simulate_traffic()

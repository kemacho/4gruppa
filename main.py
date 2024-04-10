class TRoad:
  
  def __init__(self, road, n):
    self.road = list(road)
    self.n = n


  def __light_change(self, trigger = False, trigger1 = False):
    pass


  
  def __move_car(self):
    
    #позиция машины
    car_ind = self.road.index('C')   


    
    #if self.road[car_ind + 1] == '.':
        #self.road[car_ind + 1] = 'C'
        #self.road[car_ind] = 'G'
      
    #elif self.road[car_ind + 1] == 'G':
        #self.road[car_ind + 1] = 'C'
        #self.road[car_ind] = 'G'

    #else:
    if self.road[car_ind + 1] == '.':
      self.road[car_ind + 1] = 'C'
      self.road[car_ind] = '.'

    elif self.road[car_ind + 1] == 'G':
      self.road[car_ind + 1] = 'C'
      self.road[car_ind] = '.'
      
     

  
  def __print(self):
    print(''.join(self.road), self.n)


  
  def simulate_traffic(self):
    
    i = 0
    cnt = 1
    trigger = False
    
    print(''.join(self.road), self.n)
    
    while i < self.n:
      if cnt == 5:
        self.__light_change(trigger = True)
        cnt = 0
        trigger = True
      if trigger == True:
        self.__light_change(trigger1 = True)
        trigger = False
        

      self.__move_car()
      
      self.__print()
      
      self.n -= 1
      cnt += 1
      cnt1 += 1
      



T = TRoad(road="C...R...R.R..GG....G", n=40)
T.simulate_traffic()

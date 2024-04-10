class TRoad:
  
  def __init__(self, road, n):
    self.road = list(road)
    self.n = n


  def __light_change(self, trigger = False):

    if trigger == True:
      GR = []
      RE = []
      O = []
      for k in range(len(self.road)):
        if self.road[k] == 'G':
          GR.append(k)
        elif self.road[k] == 'R':
          RE.append(k)

      for l in range(len(GR)):
         self.road[GR[l]] = 'O'
      for l in range(len(RE)):
        self.road[RE[l]] = 'G'

      for j in range(len(O)):
        self.road[O[l]] = 'R'



  
  def __move_car(self):
    
    #позиция машины
    car_ind = self.road.index('C')   

    if self.road[car_ind + 1] == '.':
        self.road[car_ind + 1] = 'C'
        self.road[car_ind] = 'G'
      
    elif self.road[car_ind + 1] == 'G':
        self.road[car_ind + 1] = 'C'
        self.road[car_ind] = 'G'

    else:
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
    cnt = 0
    print(''.join(self.road), self.n)
    while i < self.n:
      if cnt == 5:
        self.__light_change(trigger = True)
        cnt = 0

      self.__move_car()
      self.__print()
      self.n -= 1
      cnt += 1
      



T = TRoad(road="C...R...R.R..GG....G", n=40)
T.simulate_traffic()

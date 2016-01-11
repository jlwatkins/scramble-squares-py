# Hello World program in Python
from enum import Enum

class Direction(Enum):
    T = "Top"
    B = "Bottom"
    
class ImType(Enum):
    T_1 = "Image 1"
    T_2 = "Image 2"
    T_3 = "Image 3"
    T_4 = "Image 4"
    
class Edge():
    def __init__(self, direction, imtype):
        if not isinstance(direction, Direction) or not isinstance(imtype, ImType):
            raise TypeError("direction must be a Direction Enum and imtype must be an ImType Enum")
        self.direction = direction
        self.imtype = imtype
        
    def __str__(self):
        return str(str(self.direction) + " " + str(self.imtype))
        
class Square():
    def __init__(self, number, rotation, top, left, right, bottom):
        self.number = number
        self.top = top
        self.left = left
        self.right = right
        self.bottom = bottom
        self.rotation = rotation
        
    def rotate(self):
        return Square(self.number, self.rotation + 90, self.left, self.bottom, self.top, self.right)
        
    def __str__(self):
        return str("Piece # " + str(self.number) + " has " + str(self.top) + " " + str(self.left) + " " + str(self.right) + " " + str(self.bottom) + " (" + str(self.rotation) + ") ")

class Board():
    def __init__(self, s1, s2, s3, s4, s5, s6, s7, s8, s9):
        if not isinstance(s1, Square) or not isinstance(s2, Square) or not isinstance(s3, Square) or not isinstance(s4, Square) or not isinstance(s5, Square) or not isinstance(s6, Square) or not isinstance(s7, Square) or not isinstance(s8, Square) or not isinstance(s9, Square):
            raise TypeError("Invalid square type, must be of type Square for all 9 pieces input")
        print(str("Initialized Board with 9 Pieces"))
        self.complete = []
        self.complete.append(s1)
        self.complete.append(s1.rotate())
        self.complete.append(s1.rotate().rotate())
        self.complete.append(s1.rotate().rotate().rotate())
        self.complete.append(s2)
        self.complete.append(s2.rotate())
        self.complete.append(s2.rotate().rotate())
        self.complete.append(s2.rotate().rotate().rotate())
        self.complete.append(s3)
        self.complete.append(s3.rotate())
        self.complete.append(s3.rotate().rotate())
        self.complete.append(s3.rotate().rotate().rotate())
        self.complete.append(s4)
        self.complete.append(s4.rotate())
        self.complete.append(s4.rotate().rotate())
        self.complete.append(s4.rotate().rotate().rotate())
        self.complete.append(s5)
        self.complete.append(s5.rotate())
        self.complete.append(s5.rotate().rotate())
        self.complete.append(s5.rotate().rotate().rotate())
        self.complete.append(s6)
        self.complete.append(s6.rotate())
        self.complete.append(s6.rotate().rotate())
        self.complete.append(s6.rotate().rotate().rotate())
        self.complete.append(s7)
        self.complete.append(s7.rotate())
        self.complete.append(s7.rotate().rotate())
        self.complete.append(s7.rotate().rotate().rotate())
        self.complete.append(s8)
        self.complete.append(s8.rotate())
        self.complete.append(s8.rotate().rotate())
        self.complete.append(s8.rotate().rotate().rotate())
        self.complete.append(s9)
        self.complete.append(s9.rotate())
        self.complete.append(s9.rotate().rotate())
        self.complete.append(s9.rotate().rotate().rotate())
        print("Total of " + str(len(self.complete)) + " after rotating the 9 pieces.")
        self.sol = False
        
        # Checking each to make s ure they look correct
        # for s in self.complete:
        #  print(str(s))

    def clear(self):
        self.sq1 = None
        self.sq2 = None
        self.sq3 = None
        self.sq4 = None
        self.sq5 = None
        self.sq6 = None
        self.sq7 = None
        self.sq8 = None
        self.sq9 = None
        self.prevSq = set()
        
    def checkEdges(self, e1, e2):
        if e1.imtype is e2.imtype and e1.direction is not e2.direction:
          return True
        else:
          return False
    
    def checkBoard(self):
        print("Checking board")
        # Check 1 and 2 (1R and 2L)
        if not self.checkEdges(self.sq1.right, self.sq2.left):
          return False
          
        # Check 2 and 3 (2R and 3L)
        if not self.checkEdges(self.sq2.right, self.sq3.left):
          return False
          
        # Check 4 and 5 (4R and 5L)
        if not self.checkEdges(self.sq4.right, self.sq5.left):
          return False
          
        # Check 5 and 6 (5R and 6L)
        if not self.checkEdges(self.sq5.right, self.sq6.left):
          return False
        
        # Check 7 and 8 (7R and 8L)
        if not self.checkEdges(self.sq7.right, self.sq8.left):
          return False
        
        # Check 8 and 9 (8R and 9L)
        if not self.checkEdges(self.sq8.right, self.sq9.left):
          return False
        
        # Check 1 and 4 (1B and 4T)
        if not self.checkEdges(self.sq1.bottom, self.sq4.top):
          return False
        
        # Check 4 and 7 (4B and 7T)
        if not self.checkEdges(self.sq4.bottom, self.sq7.top):
          return False
        
        # Check 2 and 5 (2B and 5T)
        if not self.checkEdges(self.sq2.bottom, self.sq5.top):
          return False
        
        # Check 5 and 8 (5B and 8T)
        if not self.checkEdges(self.sq5.bottom, self.sq8.top):
          return False
        
        # Check 3 and 6 (3B and 6T)
        if not self.checkEdges(self.sq3.bottom, self.sq6.top):
          return False
        
        # Check 6 and 9 (6B and 9T)
        if not self.checkEdges(self.sq6.bottom, self.sq9.top):
          return False
        
        # Passed all tests
        print(str("Solution Found:"))
        print(str(self.sq1))
        print(str(self.sq2))
        print(str(self.sq3))
        print(str(self.sq4))
        print(str(self.sq5))
        print(str(self.sq6))
        print(str(self.sq7))
        print(str(self.sq8))
        print(str(self.sq9))
        self.sol = True
        return True


    def solve(self):
        counter = 0
        # Try All Options in Position 1 (TOP LEFT)
        for s1 in self.complete:
          self.prevSq = set()
          self.prevSq.add(s1.number)
          self.sq1 = s1
          counter += 1
          if self.sol is False:
            print("Completed " + str(counter) + " out of " + str(len(self.complete)))
          # Try All Options in Position 2 (TOP MIDDLE)
          counter2 = 0
          for s2 in self.complete:
            counter2 += 1
            if s2.number in self.prevSq:
              continue
            else:
              self.prevSq.add(s2.number)
              self.sq2 = s2
              if not self.checkEdges(self.sq1.right, self.sq2.left):
                continue
              if self.sol is False:
                print(str(counter) + ": " + str(float(counter2 / len(self.complete))))
              # Try All Options in Position 3 (TOP RIGHT)
              for s3 in self.complete:
                if s3.number in self.prevSq:
                  continue
                else:
                  self.prevSq.add(s3.number)
                  self.sq3 = s3
                  #print("Loop 3")
                  if not self.checkEdges(self.sq2.right, self.sq3.left):
                    continue
                  
                  # Try All Options in Position 4 (MIDDLE LEFT)
                  for s4 in self.complete:
                    if s4.number in self.prevSq:
                      continue
                    else:
                      self.prevSq.add(s4.number)
                      self.sq4 = s4
                      #print("Loop 4")
                      if not self.checkEdges(self.sq1.bottom, self.sq4.top):
                        continue
                      
                      # Try All Options in Position 5 (MIDDLE)
                      for s5 in self.complete:
                        if s5.number in self.prevSq:
                          continue
                        else:
                          self.prevSq.add(s5.number)
                          self.sq5 = s5
                          #print("Loop 5")
                          if not self.checkEdges(self.sq4.right, self.sq5.left):
                            continue
                          elif not self.checkEdges(self.sq2.bottom, self.sq5.top):
                            continue
                          
                          # Try All Options in Position 6 (MIDDLE RIGHT)
                          for s6 in self.complete:
                            if s6.number in self.prevSq:
                              continue
                            else:
                              self.prevSq.add(s6.number)
                              self.sq6 = s6
                              #print("Loop 6")
                              if not self.checkEdges(self.sq5.right, self.sq6.left):
                                continue
                              elif not self.checkEdges(self.sq3.bottom, self.sq6.top):
                                continue
                              
                              # Try All Options in Position 7 (BOTTOM LEFT)
                              for s7 in self.complete:
                                if s7.number in self.prevSq:
                                  continue
                                else:
                                  self.prevSq.add(s7.number)
                                  self.sq7 = s7
                                  #print("Loop 7")
                                  if not self.checkEdges(self.sq4.bottom, self.sq7.top):
                                    continue
                                  #Try All Options in Position 8 (BOTTOM MIDDLE)
                                  for s8 in self.complete:
                                    if s8.number in self.prevSq:
                                      continue
                                    else:
                                      self.prevSq.add(s8.number)
                                      self.sq8 = s8
                                      #print("Loop 8")
                                      if not self.checkEdges(self.sq7.right, self.sq8.left):
                                        continue
                                      elif not self.checkEdges(self.sq5.bottom, self.sq8.top):
                                        continue
                                      # Try All Options in Position 9 (BOTTOM RIGHT)
                                      for s9 in self.complete:
                                        if s9.number in self.prevSq:
                                          continue
                                        else:
                                          self.prevSq.add(s9.number)
                                          self.sq9 = s9
                                          self.checkBoard()
                                          self.prevSq.remove(s9.number)
                                      self.prevSq.remove(s8.number)
                                  self.prevSq.remove(s7.number)
                              self.prevSq.remove(s6.number)
                          self.prevSq.remove(s5.number)
                      self.prevSq.remove(s4.number)
                  self.prevSq.remove(s3.number)
              self.prevSq.remove(s2.number)
          self.prevSq.remove(s1.number)
                          
      
def hardcoded_yosemite():
    # Square 1
    t = Edge(Direction.T , ImType.T_1 )
    l = Edge(Direction.T , ImType.T_4 )
    r = Edge(Direction.B , ImType.T_2 )
    b = Edge(Direction.T , ImType.T_3 )
    piece1 = Square(1, 0, t, l, r, b)
    # Square 2
    t = Edge(Direction.T , ImType.T_1 )
    l = Edge(Direction.T , ImType.T_4 )
    r = Edge(Direction.B , ImType.T_2 )
    b = Edge(Direction.T , ImType.T_3 )
    piece2 = Square(2, 0, t, l, r, b)
    # Square 3
    t = Edge(Direction.T , ImType.T_1 )
    l = Edge(Direction.T , ImType.T_4 )
    r = Edge(Direction.B , ImType.T_2 )
    b = Edge(Direction.B , ImType.T_1 )
    piece3 = Square(3, 0, t, l, r, b)
    # Square 4
    t = Edge(Direction.B , ImType.T_3 )
    l = Edge(Direction.T , ImType.T_2 )
    r = Edge(Direction.B , ImType.T_4 )
    b = Edge(Direction.T , ImType.T_1 )
    piece4 = Square(4, 0, t, l, r, b)
    # Square 5
    t = Edge(Direction.B , ImType.T_3 )
    l = Edge(Direction.T , ImType.T_2 )
    r = Edge(Direction.B , ImType.T_4 )
    b = Edge(Direction.T , ImType.T_3 )
    piece5 = Square(5, 0, t, l, r, b)
    # Square 6
    t = Edge(Direction.B , ImType.T_4 )
    l = Edge(Direction.T , ImType.T_3 )
    r = Edge(Direction.T , ImType.T_1 )
    b = Edge(Direction.T , ImType.T_2 )
    piece6 = Square(6, 0, t, l, r, b)
    # Square 7
    t = Edge(Direction.T , ImType.T_4 )
    l = Edge(Direction.B , ImType.T_3 )
    r = Edge(Direction.B , ImType.T_1 )
    b = Edge(Direction.T , ImType.T_2 )
    piece7 = Square(7, 0, t, l, r, b)
    # Square 8
    t = Edge(Direction.B , ImType.T_3 )
    l = Edge(Direction.T , ImType.T_1 )
    r = Edge(Direction.T , ImType.T_2)
    b = Edge(Direction.T , ImType.T_4 )
    piece8 = Square(8, 0, t, l, r, b)
    # Square 9
    t = Edge(Direction.T , ImType.T_3 )
    l = Edge(Direction.B , ImType.T_1 )
    r = Edge(Direction.T , ImType.T_2 )
    b = Edge(Direction.T , ImType.T_3 )
    piece9 = Square(9, 0, t, l, r, b)
    # Return board with 9 pieces made above
    return Board(piece1, piece2, piece3, piece4, piece5, piece6, piece7, piece8, piece9)


if __name__ == "__main__":
    board = hardcoded_yosemite()
    eone = Edge(Direction.T, ImType.T_1)
    etwo = Edge(Direction.B, ImType.T_2)
    ethree = Edge(Direction.B, ImType.T_1)
    print(" ")
    print(str(eone))
    print(str(etwo))
    print(str(ethree))
    f1 = board.checkEdges(eone, etwo)
    t1 = board.checkEdges(eone,ethree)
    if f1:
      print("Problem with False 1")
    elif not t1:
      print("Problem with True 1")
    else:
      print("No problems with tests!")
      
    print("Beginning attempt to solve")
    board.solve()
    
    

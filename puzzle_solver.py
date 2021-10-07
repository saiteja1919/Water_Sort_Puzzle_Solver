from sys import exit
from collections import deque as dq

class Tube():
   __slots__ = ['holds', 'size']
   MAX_SIZE = 4

   def __init__(self):
      self.holds = dq()    #test tube with max size = 4, stack ds
      self.size = len(self.holds)

   def dont_touch(self):
      '''Return 1 if tube is either empty or full and contains single colur'''

      if(0 < self.size < self.MAX_SIZE): return 0
      for indx in range(self.size - 1):
         if(self.holds[indx] != self.holds[indx+1]):
            return 0
      return 1

   def check_transfer_to(self, aux_tube):
      """Checks and returns if total top colour can be transferred to auxilary tube --- returns (T/F, count)"""
      if(aux_tube.size == self.MAX_SIZE):   return (False, 0)

      top_color = self.holds[-1]
      if(aux_tube.size > 0 and  aux_tube.holds[-1] != top_color):   return(False, 0)

      top_color_count = 1
      indx = self.size - 2
      while(indx >= 0 and self.holds[indx] == self.holds[indx+1]):
         top_color_count += 1
         indx -= 1

      #ignore empty juggles
      if(aux_tube.size == 0 and top_color_count == self.size): return (False, 0)

      if(aux_tube.size + top_color_count > self.MAX_SIZE):  return (False, 0)

      return (True, top_color_count)

   def transfer_to(self, aux_tube, count):
      """Does the actual transfer of top color to aux_tube"""
      while(count > 0):
         color = self.holds.pop()
         aux_tube.holds.append(color)
         count -= 1
      
      self.size = len(self.holds)
      aux_tube.size = len(aux_tube.holds)

   def undo_transaction(self, aux_tube, count):
      '''Undo the transaction -- return transferred top color back to the current tube'''
      while(count > 0):
         count -= 1
         color = aux_tube.holds.pop()
         self.holds.append(color)

      self.size = len(self.holds)
      aux_tube.size = len(aux_tube.holds)


def solve(tube_values, tubes_cnt):

   for indx in range(tubes_cnt):
      cur_tube = tube_values[indx]

      if(cur_tube.dont_touch()):  continue

      for aux_indx in range(tubes_cnt):
         if(indx == aux_indx):   continue

         aux_tube = tube_values[aux_indx]
         verdict, length = cur_tube.check_transfer_to(aux_tube)
         if(verdict):
            #last_trans holds -- cur_idx, aux_idx, tranferred color, num elems transferred
            last_trans = (indx, aux_indx, cur_tube.holds[-1], length)
            cur_tube.transfer_to(aux_tube, length)
            ret_val = solve(tube_values, tubes_cnt)
            if(ret_val):
               print("Transfer {} color from {} to {}".format(last_trans[2], last_trans[0] + 1, last_trans[1] + 1))
               out_file.write("Transfer {} color from {} to {} \n".format(last_trans[2], last_trans[0] + 1, last_trans[1] + 1))
               return 1
            else:
               cur_tube.undo_transaction(aux_tube, last_trans[3])    #Undoing last transaction

   for indx in range(tubes_cnt):
      cur_tube = tube_values[indx]
      if(not cur_tube.dont_touch()):  return 0

   return 1


if __name__ == '__main__':
   tubes_cnt = int(input('Input count of tubes: '))
   colors_cnt = int(input('Enter number of colors: '))
   colors_set = set()
   out_file = open('Solving_steps.txt', 'r+')
   out_file.truncate(0)

   tube_values = []

   print("=== Enter space separated colors of tubes(from top to bottom) in different lines ====")
   print("=== Input empty line for empty tubes ====")
   for _ in range(tubes_cnt):
      temp = Tube()
      temp.holds = input().split()[::-1]
      temp.size = len(temp.holds)
      for color in temp.holds:
         colors_set.add(color)
      tube_values.append(temp)

   print("=== Received values ===")

   if(len(colors_set) != colors_cnt):
      print(colors_set)
      out_file.write("Please try with correct inputs. Wrong number of distinct colors entered.")
      out_file.close()
      exit('Wrong colors entered')
      
   print('\nPrinting transactions in reverse order')
   out_file.write('Follow steps in reverse ordrer\n\n')
   print('****************************')
   solve(tube_values, tubes_cnt)

   print('****************************')
   print('Final values of tubes')
   tube_index = 1
   for indx in range(tubes_cnt):
      print(tube_index, '--', *tube_values[indx].holds)
      tube_index += 1

   out_file.close()

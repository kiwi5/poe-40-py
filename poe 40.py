## return values summing up to exactly 40
# BONUS: window always on top
# BONUS: if compatible file's present --> read data from it w/o asking
# BONUS: reading from file & FURTHER manual reading - and saving the whole afterwards, for later (must be able to subtract from what's already there)
# TODO: shorten loops using list comprehension + so it'd only ever be adding what's =40, at all
# TODO: if 'kombin()' won't find ANY combination --> print this info & cease operation


# BONUS: additional features & things that may become TODOs once current ones are dealt with
# BUG: 
# CASE: 
# TODO: 

# ============================= IMPORTS: ===============================
from itertools import combinations
from re import sub
from sys import exit

# ============================ FUNCTIONS: ==============================
def spcInput():
   '''Asks for integer input: returns reversely sorted list of values (1-19).'''
   print("Input values separated with spaces or comas and press Enter:")
   while True:
      try:   
         # TEST: str("6 18 14 9 12 10 10 10 9 5 8 2 10")
         # TEST: str(" 43 5 -565-43-78_32+32,65,32  ,456 +_,64")
         tabl = input("> ")
         tabl = sub("(^[\D]+)|([\D]+$)","",sub("[\D]+",",",tabl))
         # allows nothing besides digits at beginning/end of input
         #  and changes any other non-digits in-between to comas
         tabl = tabl.split(",")
         tabl = [int(a) for a in tabl]
         print("Raw:  %r" % tabl)
      except (NameError, SyntaxError):
         # TODO: test how these catch now..
         print("Incorrect input: I take only numbers and spaces or comas.")
         continue
      
      [tabl.remove(n) for n in tabl[:] if n >= 19 or n <= 1]
      break
   tabl.sort(reverse=True)
   return tabl

def kombin(perc_array_, arr=[(40,)]):
   '''Returns all combinations summing up to 40, sorted up, \nand prints them in lines.'''
   # BUG: if there're *possible* TWO IDENTICAL combinations, then it treats one as duplicate!
   ## eg. '10 10 10 10 10 10 10 10' (that's 2x40 combos, and as such should be returned)
   # BONUS: sorted in algorithm itself (is that doable?)
   # BONUS: addition of [optional] simple argument for 'variable 40'
   # TODO.META:   1. de-duplicate after/while generation
   ##             2. the 'and' from the 'if' below & non-empty initial list --> are not necessary
   ##             3. <here was supposed to BE something, perhabs...>
   perc_array = perc_array_[:]
   perc_array.sort(reverse=True)
   # arr=[(40,)]    # non-empty, so that in 'if' below it doesn't go 'IndexError'
   # BUG: w/o resetting the 'arr=..' above, the function behaves as if initiated with values it had at its end in the previous loop
   ## I didn't expect Python to do that...
   for x in range(3,len(perc_array)):      # from 3, bc only 2*20 == 40
      LT = list(combinations(perc_array, x))      # alien code!
      LT.sort(reverse=True)
         # so that dups are adjacent
         # TODO: change this to de-dupl. w/o sorting + adjust the 'if' below
         # TODO: change, so that BEFORE THE 'FOR' the list has only unique elems (in the sort itself, already?)
         ##          or below, moving the iterator to the next unrepeating
         ##          (bc it checks pointlessly)
      for T in LT:
         if sum(T) == 40 and T != arr[-1]:
            # thanks to this "and" there're no dups = and no separate f()'s needed!
            arr.append(T)
   arr.sort(reverse=True)
      # so it returns sorted: by amount of elems in tuple asc. --> numerically
   #  # BONUS: sorting w/ highest amount on top
   #
   # print sequence:
   print("Raw combinations: ")
   if arr == [(40,)]:
      print(" No matches found.")
      print()
   else:
      # TODO: simplify printout, so it doesn't duplicate by itself (it's so for sorting by amount)    # ??
      # TODO: don't print entries with less elements than max (bc list can easily get lenghty)
      # BONUS: remove the element "[(40,)]" from 'arr' variable (or just from printing it)
      printout = []
      for a in arr:
         printout.append([len(a), a])
      printout.sort(reverse=True)
      for a in printout:
         print("%2d %r" % (printout.index(a), a))
      print()
   #
   return arr

def kombiOpt(list0_, ref):
   # TODO: turn this f() into a class (for more flexible printing, among others)
   ##       w/ method to printout elements sorted by their amount in "pair"
   list0 = list0_[:]
   list0.sort(reverse=True)
   arr = []
   if len(list0[0]) == 1:
      del list0[0]      # removes lone element, eg. "(40,)"
   for w in range(2,5): 
      # TODO: don't "i++" anymore, if for "i" had zero results (instead of range ending at "4")
      ## it serves as a (poor) limit to how far it tries to combine them
      LK = list(combinations(list0, w))      # alien code!
      LK.sort(reverse=True)
      #print(LK[0]) #
      for z in LK:         # each specific case
         seq = ref[:]
         out = False
         for y in z:    
            for x in y:
               try:
                  seq.remove(x)
               except (ValueError, IndexError):
                  out = True
                  break
            if out:
               break
         if not out:
            arr.append(z)
   arr.sort(reverse=True)  # BONUS: sorting by amount of elements in combination
   #
   # print sequence:
   print("Optimal combinations: ")
   if arr == []:
      print(" No matches found.")
      print()
   else:
      printout = []
      for b in arr:
         lengt = 0
         for a in b:
            lengt += len(a)
         printout.append([lengt, len(b), b])
      printout.sort(reverse=True)
      #
      # '''printout only of the top level, sorted by number of groups (thanks to "len(b)")'''
      print("   [item_count, group_count, (groups)")
      number = printout[0][0]
      for a in printout:
         if a[0] >= number:
            print("%2d %r" % (printout.index(a), a))
         else:
            print()
            break
   #
   # TODO: print sequence that '''prints only the single top result'''
   return arr

# TODO: 
#  def printBest():
#     list only combos of highest item count
#     ==  ommit entries of kombiOpt of count lower than the highest
#     AND if kombiOpt is empty --> list best from kombi

def checkAgain():
     '''Returns True if the user wants to check again, else it returns False.'''
     print("Do you want to check again? (y/n)")
     # BONUS: Enter/Esc
     return input("> ").lower().startswith("y")

# =============================== CODE: ================================
while True:
   perc = spcInput()
   print("Sorted:\n   %r %r \n" % (len(perc), perc))
   # TODO: always same indent, regardless of item count
   if sum(perc) < 40:
      print("That's not enough for the recipe, you need to loot some more.")
   else:
      kombiOpt(kombin(perc,[(40,)]), perc)          
      # w/o the explicit "[(40,)]" the loop goes awry..
      # this is bc the functions don't seem to start "from zero" next time they're called in Python (or at least the way I wrote them..?)
   if not checkAgain():
      exit()
input()

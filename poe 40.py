## return values summing up to exactly 40

# \tab == 3 spaces

# BONUS: window always on top
# BONUS: if compatible file's present --> read data from it w/o asking
# BONUS: reading from file & FURTHER manual reading - and saving the whole afterwards, for later (must be able to subtract from what's already there)
# BONUS: better handling of input cases with values ONLY beyond (1-19)

# TODO: shorten loops using list comprehension + so it'd only ever be adding what's =40, at all
# TODO: colored commandline - input|output|messages differently
# TODO: take items after ctrl+c && differentiate by type/id or w/e

# TODO:switch: 1.allow floats; 2.find all combinations EQUAL OR LESS THAN x; 3.map values to strings;
## thus, new use:    "what combinations of products are available within budget"
## this will likely be better off on a separate branch 

# DONE: if 'kombin()' won't find ANY combination --> print this info & cease operation

# BONUS: additional features & things that may become TODOs once current ones are dealt with
# BUG/FIXED:
# CASE: # WHY
# TODO/DONE:


# ============================= IMPORTS: ===============================
from itertools import combinations
from re import sub, search
from sys import exit


# ============================ FUNCTIONS: ==============================
def spcInput():
   """Asks for integer input. Returns list of values (1-19), sorted descending."""
   
   print("Input numeric values separated with spaces or comas and press Enter:")
   while True:
      try:   
         tabl = input("> ")
         tabl = sub(r"\D+", ",", tabl)
            # changes any non-digits to comas
         tabl = sub(r"(^\D+)|(\D+$)", "", tabl)
            # allows nothing besides digits at beginning/end of input
         hasDigits = search(r"\d", tabl)
            # bc: int() gives an empty string on 'alphabetical-only' input
         if not hasDigits:
            continue
         tabl = tabl.split(",")
         tabl = [int(a) for a in tabl]
      except (NameError, SyntaxError):    # WHY
         # TODO: test how do these catch now.. maybe it's well without, now?
         print("Incorrect input: I take only numbers and spaces or comas.\n")
         continue
         # TODO: is this 'continue' needed? does it go back or forward w/o?
      break
      
   tabl_1 = tabl[:]
   [tabl.remove(it) for it in tabl[:] if it > 19 or it < 1]
   tabl.sort(reverse=True)
   
   numberLength = len(str(len(tabl)))
   offsetChosen = 3
   offsetSecondary = 0
   if numberLength > offsetChosen:
      offsetSecondary = numberLength - 2
   
   print(f"\nRaw:  {' '*offsetSecondary}{tabl_1}")
   print(f"Sorted & filtered:\n  {len(tabl):>{offsetChosen}} {tabl}\n")
   return tabl


class kombin:
   """Returns all combinations summing up to 40, sorted descending. Has a "print()" function to print them in lines."""
   def __init__(self, item_array_, arr=None):
      if arr == None: 
         self.arr=[(40,)]
      else: 
         self.arr = arr
      self.item_array = item_array_[:]
      self.item_array.sort(reverse=True)
      self.printo = []
      self.createPrintList()
   
   #
      # BUG: if there're *possible* TWO IDENTICAL combinations, then it treats one as duplicate!
      ## eg. '10 10 10 10 10 10 10 10' (that's 2x40 combos, and as such should be returned)
      
      # FIXED: w/o resetting the 'arr=..' above, the function behaves as if initiated with values it had at its end in the previous loop
      ## I didn't expect Python to do that...
      ## so it's like, variables belonging to a LOOP, merely INITIATED by function?
      ## or rather: belonging/local to the function, BUT retained while in the loop, between function runs
      
      # BONUS: sorted in algorithm itself
      # DONE: addition of [optional] simple argument for 'variable 40'
      
      # TODO.META:   
      ## 1. de-duplicate after/while generation
      ## 2. the 'and' from the 'if' below & non-empty initial list --> are not necessary
      ## 3. ??

   def simpleCombins(self):
      """In each increasing combination of items, check which equals LIM and add it to the <wanted> array"""
      #FIXED: for 18,12,10 it skips here, bc range(3,3) == []
      ##  same with '12 18 6 4' vs '12 18 6 4 1'
      for n in range(3,len(self.item_array)+1):  # no less than 3 items, bc only 2*20 == 40
         tupleList = [c for c in combinations(self.item_array, n) if sum(c) == lim]
         if len(self.arr) > 1 and not tupleList: 
            break          # because    
         tupleList.sort(reverse=True)   # sorting --> duplicates become adjacent
         # TODO: change this to de-dupl. w/o sorting + adjust the 'if' below
         # TODO: change, so that BEFORE the 'for' the list has only unique elems 
         ##       in the sort itself, already?
         ##       or below, moving the iterator to the next unrepeating
         ##       (bc it checks pointlessly)
      
         for tupl in tupleList:
            if tupl != self.arr[-1]:
               self.arr.append(tupl)

      del self.arr[0]      # removes first element, eg. "(40,)" or other placeholder
      # NOTE: this is only needed so that the arr appending above goes w/o IndexError
      # TODO: find another way to check last elem w/o IndexError, even if list is empty

      self.arr.sort(reverse=True)
      # so the tuples are sorted: 
      ## by amount of elems in a tuple, descending --> 
      ## --> numerically within given amount, descending
      
   def createPrintList(self):
      """creation of the list to be printed"""
      if self.arr==[(40,)]:
         self.simpleCombins()

      if not self.arr:
         print(f"You have more than {lim}, but no exact matches found.\n")
      else:
         maxItems = max([len(tup) for tup in self.arr])
         self.printo = [[len(tup), tup] for tup in self.arr if len(tup) == maxItems]
         self.printo.sort(reverse=True)

         # TODO: wait, DON'T I already have amounts SPECIFIED?
         ## just read that and:
         ##    1) rm what's less
         #     OR
         ##    2) count them and 'cutTail()', bc they're already sorted
         
         # TODO: analyze if it NEEDS sorting here, anymore
         ## probably not, since arr's been sorted just before,
         ## and its order is retained here

   def print(self):
      """printing sequence"""
      # if not self.printo: 
      #    self.createPrintList()
      print("Simple combinations available: ")
      for tup in self.printo:
         print("%2d %r" % (self.printo.index(tup)+1, tup))
      print()
      # TODO: simplify printout, so it doesn't duplicate by itself (it's so for sorting by amount)    # ??
      
   # def __get__(self, obj, objtype):
   #    if not self.arr: self.simpleCombins()
   #    return self.arr


def kombiOpt(list0_, ref):
   """
   Takes:
      list0_   -  list of tuples (combinations).
      ref      -  a referential list from which they were generated.
   
   Generates:     sums of these combinations and compares them to the list.
   
   Returns:       only sums of combinations that don't require items not present in the list.
   """
   
   # TODO: turn this f() into a class (for more flexible printing, among others)
   ##       w/ method to printout elements sorted by their amount in "pair"
   
   if not list0_:
      return
   
   list0 = list0_[:]
   list0.sort(reverse=True)
      # DONE: if sort() or sth else informs @ empty list --> return HERE or above
   arr = []
   
   for w in range(2,5):
      # TODO: don't "i++" anymore, if for "i" had zero results (instead of range ending at "4")
      ## it serves as a (poor) limit to how far it tries to combine them
      ## OR maybe the upper range from some formula, based on lenght of arr?

      # print("w:",w) #
      komboList = list(combinations(list0, w))
         # BUG: these give an 'MemoryError' here
         ## 15 elems:   12 12 14 19 17 10 11 3 5 6 8 2 54 4 1 16
         ## 16 elems:   2 4 5 12 43 12 114 14 16 19 0 10 22 3 4 5 7 8 3 1
         ## stutter     2 4 5 12 43 12 114 14 16 19 0 10 22 3 4 5 
         ## stutter     2 4 5 12 43 12 114 14 16 19 0 10 22 3 4 5 7                       noticable
         ## stutter 14: 2 4 5 12 43 12 114 14 16 19 0 10 22 3 4 5 7 8      (w4, 26,11,2)  I was actually WAITING :D
         ## stutter 15: 2 4 5 12 43 12 114 14 16 19 0 10 22 3 4 5 7 8 3    (w4,112,14,3)  I thought it was DYING, but instead it printed *112* **TOP** results :D :D
         ## stutter 14: 12 12 14 19 17 10 11 3 5 6 8 2 54 4 1              (w4, 65,13,3)  stuttered HARD and only printed 65 results (of 3-groups)
         ## stutter 14: 12 12 14 19 17 10 11 3 5 6 8 2 54 4                (w4, 20,12,3)
         ## (22,12,2)   12 13 4 5 2 3 343 2 5 10 18 1 3 13 15

         # TODO: <modify 'combinations()'> so it compares elems as below
         #  and discontinues creating a kombo, if tupl exhausted the ref
         
      komboList.sort(reverse=True)
      #print(komboList[0]) #TEST
      for kombo in komboList:
         ref_cpy = ref[:]
         out = False
         for tupl in kombo:
            for elem in tupl:
               try:
                  ref_cpy.remove(elem)
                  # rm values from copy of ref, till it's empty
                  # removal attempt after emptied == this combo is impossible
               except (ValueError, IndexError):    # WHY
                  out = True  # bc I gotta..
                  break
            if out:           # ..of these loops SOMEHOW (this is a bad pun)
               break
         if not out:
            arr.append(kombo)
   arr.sort(reverse=True)
   # BONUS: sorting by amount of elements in combination    #??
   
   if not arr:
      print("Optimal combinations available: \n No matches found.\n")
   else:
      # creation of the list to be printed:
      # TODO: append ONLY results w/ the top itemCount
      printout = []
      # print("What sits in printout..?: ")  #TEST
      for tupleCombo in arr:
         itemCount = 0
         for tupl in tupleCombo:
            itemCount += len(tupl)
         printout.append([itemCount, len(tupleCombo), tupleCombo])
      ## itemCounts = [sum( [len(tupl) for tupl in tupleCombo] )
                   ## for tupleCombo in arr]
      ## maxItems = max(itemCounts)
      ## printout = [ [maxItems, len(tupleCombo), tupleCombo]
                   ## for tupleCombo in arr if #len(tupl) = maxItems]
      
      # at this point they're only sorted by the very first item, descending
      printout.sort(reverse=True)
      # NOW they're sorted according to n of items
      ## then n of groups, THEN first item itself
      
      # for testing: 2 4 5 12 43 12 114 14 16 19 0 10 22 3 4 5
      
      # BONUS: get lowerThanTop/n_OfTop by counting..
      # ..how many times 'printout[a][0]' is equal to printout[0][0]
      ## s.count(x)   - total number of occurrences of x in s
      ## adress_of_itemCount  .count(  singleNumber_itemCountObject  )
      ## printout[a][0]       .count(  printout[0][0]                )
      ## hmm, how'd I do 'max(printout[a][0])' ?
      
      # printout[a]     is a single combo
      # printout[a][0]  is the first number == combo itemCount
      
      # DONE: rm all occurences after 'lower n than top' is detected
      ## "cut the tail", shall I say
      ## BUT this requires 'printout' to be reversely SORTED beforehand
      # BONUS: 'cutTail()' maybe? taking also how deeply nested it's gotta be?
      n_items = [combo[0] for combo in printout]
      n_OfTop = n_items.count(max(n_items))
      del printout[n_OfTop:]
     
      # printing sequence:
      # """printout only of the top level, sorted by number of groups"""
      ## (thanks to "len(tupleCombo)")
      
      print("Optimal combinations available: ")
      print("  n [n_items, n_groups, (groups)] ")
      [print("%3d %r" % (printout.index(combo)+1, combo)) for combo in printout]
      print()
      # TODO: groups spaced like in a table, for readability and cleaniness

   # BONUS: print function that """prints only the single top result"""
   ## OR TAKES NUMBER of results to print
   
   return arr

# TODO: 
#  def printBest():
#     list only combos of highest item count
#     ==  ommit entries of kombiOpt of count lower than the highest
#     AND if kombiOpt is empty --> list best from kombi


def checkAgain():
   """
   Returns 'True' if the user wants to check again, else it returns 'False'.
   Asks until user either inputs 'n' or presses 'Enter'.
   """
   while True:
      i = input("Do you want to check again? (Enter / n) ").lower()
      if not i:               return True
      elif i.startswith("n"): return False


# =============================== CODE: ================================
lim = 40
def main():
   while True:
      items = spcInput()
      if sum(items) < lim:
         print(f" You have less than {lim} - you need to loot some more.\n")
      else:
         kombin_arr = kombin(items)
         kombin_arr.print()
         kombiOpt(kombin_arr.arr, items)
      
      if not checkAgain():
         exit()
      print()

   input()


if __name__ == "__main__":
   # execute only if run as a script
   main()

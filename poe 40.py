## return values summing up to exactly 40
# BONUS: window always on top
# BONUS: if compatible file's present --> read data from it w/o asking
# BONUS: reading from file & FURTHER manual reading - and saving the whole afterwards, for later (must be able to subtract from what's already there)
# TODO: shorten loops using list comprehension + so it'd only ever be adding what's =40, at all
# TODO: if 'kombin()' won't find ANY combination --> print this info & cease operation
# TODO: colored commandline - input|output|messages differently

# TODO:switch: 1.allow floats; 2.find all combinations EQUAL OR LESS THAN x; 3.map values to strings;
## thus:    "what combinations of products are available within budget"
## this will most probably require a separate BRANCH 


# BONUS: additional features & things that may become TODOs once current ones are dealt with
# BUG: 
# CASE: 
# TODO: 

# ============================= IMPORTS: ===============================
from itertools import combinations
from re import sub, search
from sys import exit

# ============================ FUNCTIONS: ==============================
def spcInput():
   '''
   Asks for integer input.
   
   Returns list of values (1-19), sorted descending.
   '''
   
   print("Input values separated with spaces or comas and press Enter:")
   while True:
      try:   
         # TEST: str("6 18 14 9 12 10 10 10 9 5 8 2 10")
         # TEST: str(" 43 5 -565-43-78_32+32,65,32  ,456 +_,64")
         tabl = input("> ")
         # tabl = sub("(^[\D]+)|([\D]+$)","",sub("[\D]+",",",tabl))
         tabl = sub("(^\D+)|(\D+$)","",sub("\D+",",",tabl))
         # allows nothing besides digits at beginning/end of input
         #  and changes any other non-digits in-between to comas
         hasDigits = search("\d", tabl)
         # bc: 'only alpha' input flips 'int(a)' over, bc it's an empty string D:
         if not hasDigits:
            print("Input values separated with spaces or comas and press Enter:")
            continue
         tabl = tabl.split(",")
         tabl = [int(a) for a in tabl]
         print("Raw:  %r" % tabl)
      except (NameError, SyntaxError):
         # TODO: test how do these catch now..
         print("Incorrect input: I take only numbers and spaces or comas.")
         continue       # TODO: is it needed? does it go back or forward w/o?
      
      [tabl.remove(n) for n in tabl[:] if n > 19 or n < 1]
      break
   tabl.sort(reverse=True)
   return tabl

def kombin(item_array_, arr=[(40,)]):
   '''
   Returns all combinations summing up to 40, sorted descending, 
   AND prints them in lines.
   '''
   
   # BUG: if there're *possible* TWO IDENTICAL combinations, then it treats one as duplicate!
   ## eg. '10 10 10 10 10 10 10 10' (that's 2x40 combos, and as such should be returned)
   
   # BUG: w/o resetting the 'arr=..' above, the function behaves as if initiated with values it had at its end in the previous loop
   ## I didn't expect Python to do that...
   ## so it's like, variables belonging to a LOOP, merely INITIATED by function?
   ## or rather: belonging/local to the function, BUT retained while in the loop, between function runs
   
   # BONUS: sorted in algorithm itself (is that doable?)
   # BONUS: addition of [optional] simple argument for 'variable 40'
   
   # TODO.META:   
   ## 1. de-duplicate after/while generation
   ## 2. the 'and' from the 'if' below & non-empty initial list --> are not necessary
   ## 3. <here was supposed to BE something, perhabs...>
   
   item_array = item_array_[:]
   item_array.sort(reverse=True)
   
   # arr=[(40,)]    # non-empty, so that in 'if' below it doesn't go 'IndexError'
   # TODO: find another way to check last elem w/o IndexError, even if list is empty

   # if not arr == [whatever]:   arr = []      # if arr isn't already initiated
   
   for x in range(3,len(item_array)):
   # no less than 3 elems, bc only 2*20 == 40
      tupleList = list(combinations(item_array, x))
      tupleList.sort(reverse=True)   # sorting --> duplicates become adjacent
         # TODO: change this to de-dupl. w/o sorting + adjust the 'if' below
         # TODO: change, so that BEFORE THE 'FOR' the list has only unique elems (in the sort itself, already?)
         ##       or below, moving the iterator to the next unrepeating
         ##       (bc it checks pointlessly)
      for tupl in tupleList:
         if sum(tupl) == 40 and tupl != arr[-1]:
            arr.append(tupl)
   
   del arr[0]     # removes first element, eg. "(40,)" or other placeholder
   # NOTE: this elem is only needed so that the arr creation above goes w/o error
   
   arr.sort(reverse=True)
      # so the tuples are sorted: 
      ## by amount of elems in a tuple, descending --> 
      ## --> numerically within given amount, descending
      
      # TODO:?: sorting w/ highest amount on top  # did I do that already?

   if arr == []:  print("Raw combinations: \n No matches found.\n")
   else:
      # creation of a list to be printed:
      printout = []
      maxItems = 0
      # [(maxItems = len(tup)) for tup in arr if len(tup) > maxItems]
      for tup in arr:
         if len(tup) > maxItems:    maxItems = len(tup)
      [printout.append([len(tup), tup]) for tup in arr if len(tup) == maxItems]
      # for tup in arr:
         # if len(tup) == maxItems:   printout.append([len(tup), tup])
      printout.sort(reverse=True)
      
      # TODO:algo: analyze if it NEEDS sorting here, anymore
      ## probably not, since arr's been sorted just before,
      ## and its order is retained here
      
      
      # printing sequence:
      print("Raw combinations: ")
      for tup in printout:
         print("%2d %r" % (printout.index(tup)+1, tup))
      print()
   
   # TODO: simplify printout, so it doesn't duplicate by itself (it's so for sorting by amount)    # ??
   
   return arr

def kombiOpt(list0_, ref):
   '''
   Takes:
      list0_   -  list of tuples (combinations).
      ref      -  a referential list from which they were generated.
   
   Generates:     sums of these combinations and compares them to the list.
   
   Returns:       only sums of combinations that don't require items not present in the list.
   '''
   
   # TODO: turn this f() into a class (for more flexible printing, among others)
   ##       w/ method to printout elements sorted by their amount in "pair"
   
   list0 = list0_[:]
   list0.sort(reverse=True)
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
      #print(komboList[0]) #
      for kombo in komboList:
         ref_cpy = ref[:]
         out = False
         for tupl in kombo:
            for elem in tupl:
               try:
                  ref_cpy.remove(elem)
                  # rm values from copy of ref, till it's empty
                  # removal attempt after emptied == this combo is 
               except (ValueError, IndexError):    # WHY
                  out = True
                  break
            if out:
               break
         if not out:
            arr.append(kombo)
   arr.sort(reverse=True)
   # BONUS: sorting by amount of elements in combination #??
   
   if arr == []:  print("Optimal combinations: \n No matches found.\n")
   else:
      # creation of list to be printed:
      printout = []
      for tupleCombo in arr:
         itemCount = 0
         for tupl in tupleCombo:
            itemCount += len(tupl)
         printout.append([itemCount, len(tupleCombo), tupleCombo])
      printout.sort(reverse=True)
         
      # print sequence:
      # '''printout only of the top level, sorted by number of groups'''
      ## (thanks to "len(b)")       # WHY
      print("Optimal combinations: ")
      # print("   [item_count, group_count, (groups)]")
      # TODO: groups spaced like in a table, for readability and cleaniness
      print("    [n_items, n_groups, (groups)]")
      n_items = printout[0][0]
      # printout[a]     is a single combo
      # printout[a][b]  is the first number == combo itemCount
      for combo in printout:
         if combo[0] >= n_items:        # WHY: print while highest item count
            print("%3d %r" % (printout.index(combo)+1, combo))
         else:
            print()
            break
      # [print("%2d %r" % (printout.index(combo)+1, combo)) while combo[0] >= n_items for combo in printout else: print() break]

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
     while True:
        i = input("< ").lower()
        if        i.startswith("y"):   return True
        elif      i.startswith("n"):   return False

# =============================== CODE: ================================
while True:
   perc = spcInput()
   print("Sorted:\n  %3r %r \n" % (len(perc), perc))
   # TODO: always same indent, regardless of item count
   if sum(perc) < 40:
      print("That's not enough for the recipe, you need to loot some more.")
   else:
      kombiOpt(kombin(perc,[(40,)]), perc)
      # w/o the explicit "[(40,)]" the loop goes awry..
      # this is bc the functions don't seem to start "from zero"
      # the next time they're called (or at least the way I wrote them..?)
   if not checkAgain():
      exit()
   print()
input()

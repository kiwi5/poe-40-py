## return values summing up to exactly 40
# BONUS: window always on top
# BONUS: if compatible file's present --> read data from it w/o asking

# BONUS: additional features & things that may become TODOs once current ones are dealt with
# BUG: 
# CASE:
# TODO: 

# ============================= IMPORTS: ===============================
from itertools import combinations


# ============================ FUNCTIONS: ==============================
def spcInput():
  # input works, but is illegal, bc 'eval()'
  #
  # CASE: restrict to values <1,19>!
   while True:
      try:
         # DEBUG: tabl = eval("[" + input("Input space-separated values: ").replace(" ",",") + "]")
         tabl = eval("[" + str("6 18 14 9 12 10 10 10 9 5 8 2 10").replace(" ",",") + "]")
         # TODO: convert all \s+ \t* to ','      re.sub()
      except (NameError, SyntaxError):
         print("Incorrect values! I take only numbers & spaces.")
         continue
      for n in tabl:
         # BUG: passes floats!
         if "float" in str(type(n)):
            print("Float values were inputted, there might be some errors..")
            n = int(n)      
            # BUG: doesn't change floats, n I dunno Y 
            # BONUS: request to reinput of that which was detected to be a float
            #
            # 'break' here gone immediately under 'for',
            ##  and 'continue' passes 'for' till end, pointlessly
      break
   tabl.sort(reverse=True)
   return tabl

def kombinZ(proc_array_, arr=[(40,)]):
   '''returns all combinations that sum to 40, sorted, and prints them out'''
   # BUG: if there're *possible* TWO IDENTICAL combinations, then it treats one as duplicate!
   ## eg. '10 10 10 10 10 10 10 10' (that's 2x40 combos, and as such should be returned)
   # BONUS: sorted in algorithm itself
   # BONUS: addition of [optional] argument for 'variable 40'
   # TODO.META:   1. de-duplicate after/while generation
   ##             2. the 'and' from the 'if' below & non-empty initial list --> are not necessary
   ##             3. <here was supposed to BE something, perhabs...>
   proc_array = proc_array_[:]
   proc_array.sort(reverse=True)
   #arr=[(40,)]    # non-empty, so in 'if' below it doesn't go 'IndexError'
   for x in range(3,len(proc_array)):      # from 3, bc only 2*20 == 40
      LT = list(combinations(proc_array, x))      # alien code!
      LT.sort(reverse=True)
         # so that dups are adjacent
         # TODO: change this to de-dupl. w/o sorting + adjust the 'if' below
         # TODO: so that BEFORE THE 'FOR' the list was unique (in the sort itself, already?)
         ##          or below, moving the iterator to the next unrepeating
         ##          (bc it checks pointlessly)
      for T in LT:
         if sum(T) == 40 and T != arr[-1]:
            # thanks to this 'and' there're no dups = and no separate f()'s needed!
            arr.append(T)
   arr.sort(reverse=True)
      # so it returns sorted (by): amount of elems in tuple(asc.) --> numerical
      # BONUS: sorting w/ highest amount on top
   
   # printout sequence:
   print("kombinZ: ")
   printout = []
   for a in arr:
      printout.append([len(a), a])
   printout.sort(reverse=True)
   for a in printout:
      print(printout.index(a), a)
   
   return arr

def kombi_opt(list0_, ref):
   # TODO: turn it into a class
   ##       w/ method to printout elements sorted by their amount in "pair"
   list0 = list0_[:]
   list0.sort(reverse=True)
   arr = []
   if len(list0[0]) == 1:
      del list0[0]      # remove lone element, eg. '(40,)'
   for w in range(2,5): 
      # TODO: don't 'i++' anymore, if 'i' had zero results 
      ## = limit to how far it combines them
      LK = list(combinations(list0, w))      # alien code!
      LK.sort(reverse=True)
      #print(LK[0]) #
      for z in LK:      # each specific case is here
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
   arr.sort(reverse=True)  # TODO: sort by nr of elements in combination

   # printout sequence:
   print("\nkombi_opt: ")
   printout = []
   for b in arr:
      lengt = 0
      for a in b:
         lengt += len(a)
      printout.append([lengt, b])
   printout.sort(reverse=True)
   for a in printout:
      print(printout.index(a), a)
   
   return arr

# =============================== CODE: =======================================
# counting:
proc = spcInput()
print("Sorted: %r %r \n" % (len(proc), proc))
if sum(proc) < 40:
   print("Not enough, come back later.")
else:
   #printout2 = kombinZ(proc)
      
##   print("\nkombi_opt: ")
##   printout4 = []
   #printout3 = kombi_opt(printout2, proc)
   kombi_opt(kombinZ(proc), proc)
##   for y in printout3:
##      lengt = 0
##      for x in y:
##         lengt += len(x)
##      printout4.append([lengt, y])
##   printout4.sort(reverse=True)
##   for x in printout4:
##      print(printout4.index(x), x)

##   print("\nPo kombinZ: ")
##   printout5 = []
##   for x in printout2:
##      printout5.append([len(x), x])
##   printout5.sort(reverse=True)
##   for x in printout5:
##      print(printout5.index(x), x)

    
# TODO: cmpr-Times(kombin+uniqL, kombinZ)
#
# TODO: prefer to use the greatest amount of items (== those of the lesser values)
#     : 1. check "inoverflapping" between each other
#          (sorting results: by amount of <instances> --> am. of flasks + am. of elements)
#       2. if overflapping, sort options from the most numerous downwards
#          (this might be a subtype of the above, even)
#
## combinations from "2" till "stop if the whole previous one yielded nothing"
## would have to be each-with-each
## by means of "exhausting d'printout" = when trying to append element already used --> next
## recursion could've worked here on a list one-by-one
## or: generate all combinations and check them one-by-one
##     (though it's a matter of generating them one-by-one, which I know not how to do)

# check all combinations 2-4 timed, and print only these unexhausting (+ number of the used ones)
# still needs to print all solitary ones
# 
input()


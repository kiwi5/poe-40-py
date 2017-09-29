## return values summing up to exactly 40
# BONUS: window always on top
# BONUS: if compatible file's present --> read data from it w/o asking

# BONUS: additional features & things that may become TODOs once current ones are dealt with
# BUG: 
# CASE:
# TODO: 

# ============================= IMPORTS: ===============================
import itertools


# ============================ FUNCTIONS: ==============================
def spcInput():
  # input works, but is illegal, bc 'eval()'
  # CASE: restrict to values <1,19>!
  while True:
    try:
      tabl = eval("[" + input("Input space-separated values: ").replace(" ",",") + "]")
      # DEBUG: tabl = eval("[" + str("6 18 14 9 12 10 10 10 9 5 8").replace(" ",",") + "]")
      # TODO: convert all \s+ \t* to ','    re.sub()
    except (NameError, SyntaxError):
      print("Incorrect values! I take only numbers & spaces.")
      continue
    # BUG: passes floats!
    for n in tabl:
      if "float" in str(type(n)):
        print("Inputted float values, there might be some errors..")
        n = int(n)    
        # BUG: doesn't change floats, n I dunno Y 
        #   (strings it wouldn't change too, actually)
        # BONUS: request to reinput of that which was detected to be a float
        #
        #continue      
        #'break' here went under 'for', and 'continue' passes 'for' till end
    break
  tabl.sort(reverse=True)
  return tabl

def kombin(spis):
  # returns sorted combinations, summing up to 40
  # BONUS: sorted from algorithm itself
  # BONUS: addition of [optional] argument for variable '40'
  arr=[]
  for x in range(3,len(spis)):    # from 3, bc only 2*20 == 40
    LT = list(itertools.combinations(spis, x))    # alien code!
    for T in LT:
      if sum(T) == 40:# and T != arr[-1]:
        arr.append(T)
  arr.sort(reverse=True)
  return arr

def kombinZ(spis):
  # returns sorted combinations, summing up to 40
  # BONUS: sorted from algorithm itself
  # BONUS: addition of [optional] argument for variable '40'
  arr=[(40,)]
  for x in range(3,len(spis)):    # from 3, bc only 2*20 == 40
    LT = list(itertools.combinations(spis, x))    # alien code!
    LT.sort(reverse=True)
    # TODO: sorting w/ highest amount on top
    for T in LT:
      try:
        if sum(T) == 40 and T != arr[-1]:
          arr.append(T)
      except IndexError:
        break
  return arr

def uniq1(seq): 
  # order preserving
  checked = []
  for e in seq:
    if e not in checked:
      checked.append(e)
  return checked

def uniqL(seq):
  # returns a table w/o repeating values, if they are adjacant to each other
  # ?: the table must've got >1 elements!
  # BONUS: changing this into in-place for lists
  for i in range(len(seq)):
    try:
      while seq[i] == seq[i+1]:#?: and i < len(seq)-1:
        del seq[i+1]
        #seq.pop(i+1)
        if i == len(seq)-1:   #?: Y it's UNDER removal?
          break
    except IndexError: break
  return seq


# =============================== CODE: ================================
# counting:
proc = spcInput()
print("Sorted: %r \n" % proc)
if sum(proc) < 40:
  print("Not enough, come back later.")
else:
  printout = uniqL(kombin(proc))
  print("After kombin+uniqL: ")
  for x in printout:
    print(x)
    
  printout2 = kombinZ(proc)
  print("After kombinZ: ")
  for x in printout2:
    print(len(x), x)
    
# TODO: cmpr-Times(kombin+uniqL, kombinZ)
  
# TODO: check if they got such a f() in NumPy!
# TODO: check if search imlementations allow me this easily ##well, they should- that's what they're for##

# TODO: prefer to use the greatest amount of items (== those of the lesser values)
#     : 1. checking "inoverflapping" between each other
#          (sorting results: by amount of <instances> --> am. of flasks)
#       2. if overflapping, sort options from most numerous down (this might be a subtype of the above, even)

input()







# =========================== SCRAPS/OLD: ============================
# = = = = = = = = = = = = = = = = = = = = = =
#python-course.eu

# import numpy
# tabl[] = input()   
# inputting to table a series of 2digit numbers, space-separated, with Enter at he end
#   as string w/ spaces, &then slicing and threat the cells as ints? NOT NEEDED :D

#tabl = array(int, input("Input space-separated values: ").split()) 
# bc I want list of ints instead of just strings
#tabl.sort(key=str.lower)    
# but it isn't sorting ;(

##def old_input():
##  print("Input Enter-separated values.")
##  while True          # inputting data
##    proc.append(int(input("> ")))
##    if proc[-1] == NaN:
##      # and here diffrent acrions dep. on values -->
##      # --> rm last letter (and treat it as) --> End of input
##    else continue

# other testing
##print(tabl)
##tabl = tabl.split()
##for x in tabl:
##  # print(x)
##  print(type(x))
##  x = int(x)
##  print(type(x))
##  print( )
##tabl.sort(reverse=True)     # still sorts as alphanumeric!!
###print("Is integer? %r" % tabl[0].isinteger())
#
##print("After splitting & sorting: ")
##print(tabl)
##print(tabl[0])
###print("Is decimal? %r" % tabl[0].isdecimal())
### print(sum(tabl[]))
# = = = = = = = = = = = = = = = = = = = = = =

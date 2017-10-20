# PoE 40

### "Just take these numbers between 1 & 19, and return best combinations summing up to 40".

This is for the purpose of finding an effective way to combine looted items, needed for [Quality Recipe](https://pathofexile.gamepedia.com/Vendor_recipe_system#Quality_Items) in Path of Exile game.
Saves the time, as counting it in calculator (or mentally, as some are able to) is no longer needed.


### :fork_and_knife: How to use:
 1. Open the script.
 1. Write percent values of all items of a given type you'd like to vendor.
 1. Script outputs what combinations are available to you.

#### :pushpin: Bug note:
There's one significant bug I've found: if the input allows for __two identical__ combinations to be possible, it returns only one of them.
   For example 
   > '10 10 10 10 10 10 10 10' 
   should return 
   > [8, 2, (10, 10, 10, 10),(10, 10, 10, 10)] 
   (that's 8 items in 2 groups/recipes), but it returns only 
   > [4, (10, 10, 10, 10)]. 
   When numbers are more varied it could be much more difficult to notice than in this simple example.

#### NOTE: It needs [Python 3](https://www.python.org/downloads/) installed on your machine to work. Python 2 shouldn't work.
###### Tested on Python 3.6.2 only.

Only after running this script have I gotten to know _how many_ more combinations there could be, that I hadn't even suspected.


====================================

Made for the purpose of learning and automation. 
Maybe someone else will find it useful, too, but I expect there to be better solutions for this already.

This is what I consider my very first complete program, although there have been a few tiny ones before.

##### Todo here:
   - [x] read about Markdown and format this document better
   - [x] note some case-use bugs
   - [x] give example of input and output?

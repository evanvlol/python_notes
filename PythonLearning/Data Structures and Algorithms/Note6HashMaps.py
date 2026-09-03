## A hash map is a way to store data using a key to find a value. (Key-value pair system).

## Think about but instead of indices you use a custom value.

## For example in an array [1,2,3] your indices would be 0, 1, and 2. But lets say you wanted to use Apple, Orange, and Banana,
## This works just fine as well.

## What makes hash maps powerful is how they are able to do what they do with O(1) time complexion.
## For lookup and insert the time complexion is usually O(1).

# Imagine you have a row of mailboxes, each one has a unique number, instead of looking through everyones mailbox for a letter,
# You can run their name through a hash function and it will tell you which mailbox to open.

## Ask, where does the key go? And the function will give you the answer.
## Sometimes two keys might get the same hash (collision), if they do its not something to worry about because most languages
## have mechanisms to handle these collisions for us.

## One big rule for keys for key maps!!! THEY MUST BE HASHABLE. Numbers, Strings, and Tuples are hashable. Lists and Dictionaries
# (which dictionaries are hash maps) are not hashable.

## Hash maps are so common in interviews because they are the go-to structure in interviews when brute forcing is to slow.

## Trying to find a value that already exists requires looping through every value O(n), but with a hashmap you just need to check
# once, O(1).

## When you brute force you ask the same question over and over again, but with a hash map you remember them as you go.
## Once again, No Hash Maps = O(N), Hash Map = O(1).

## Syntax might change between languages but they all do the same things.
## 1. Storing something.
## 2. Looking something up.
## 3. Updating/initializing values.

## ex.

my_map = {}
for item in data:
    if item not in my_map:
        my_map[item] = 1
    else: my_map[item] += 1

## This structure is often referred to as a frequency map, going through items, if it doesnt exist we set it to =1,
# if it does exist we update its count to +=1.

# There are language specific helpers that help clean up the code. Like defaultdict in python or Map.getOrDefault() in Java.

# Hashmaps are often used while you loop, not just after, which allows you to build and use the loop at the same time.
## Initialize a map and use it while looping, it will help you alot.
## Youll use them in anything, ask what you can store to avoid doing extra things later.




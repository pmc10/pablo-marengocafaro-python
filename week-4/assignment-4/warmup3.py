# Two lists of programming languages with some duplicates
list1 = ["Python", "JavaScript", "C++", "Ruby"]
list2 = ["Java", "Python", "JavaScript", "Go"]

# Convert lists to sets
set1 = set(list1)
set2 = set(list2)

# 1. Union: all unique languages from both lists
print("Union:", set1.union(set2))

# 2. Intersection: languages present in both lists
print("Intersection:", set1.intersection(set2))

# 3. Difference: languages only present in the first list
print("Difference:", set1.difference(set2))

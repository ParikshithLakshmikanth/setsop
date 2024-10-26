myset = {1,2,2,3,4,4,4}
print("set:",myset)

myset.add(5)
print("Updated set:",myset)

set1 = myset
set2 = {2,4,4,6}

print("Set 1:",set1)
print("Set 2:",set2)
print("Difference:",set1.difference(set2))
print("Symmetric Difference:",set1.symmetric_difference(set2))
list1=[8,6,7,4,5]
list2=[5,4,3,2,1]
# a.check if the lists have the same length
if len(list1)==len(list2):
    print("a.The lists have the same length.")
else:
    print("a.The lists have the different lengths.")
print(f"sum of the list1:{sum(list1)} & sum of list2:{sum(list2)}")
#b. Check if the lists have the same sum
if sum(list1)==sum(list2):
    print("b.The lists sum to the same value.")
else:
    print("b.The lists do not sum to the same value.")
#c. Check if there are any common values in both the lists
    common_values= set(list1) & set(list2)
if common_values:
    print(f"c. Common values in both lists: {common_values}")
else:
    print("c. There are no common values in both lists.")



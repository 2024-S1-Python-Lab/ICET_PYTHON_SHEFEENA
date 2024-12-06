# sample dictionary
my_dict = {'banana': 3,'apple': 1,'cherry': 2,'date': 4}
print("Original list:", my_dict)
# sort in ascending order based on keys
assorted_dict=dict(sorted(my_dict.items()))
print("Assending order:", assorted_dict)
# sort in descending order based on keys
assorted_dict=dict(sorted(my_dict.items(),reverse=True))
print("Descending order:", assorted_dict)

import sys

def set_stuff(a, b):
    a_union_b = a | b # or us a.union(b)
    a_subset_b = a.issubset(b)
    a_superset_b = a.issuperset(b)

    return a_union_b, a_subset_b, a_superset_b

# # Function to make a set from a string of tokens
# def make_set(line):
#     line = line.strip()
#     tokens = line.split()
#     return set(tokens)
    
# def make_sorted_list(s):
#     lst = list(s)
#     lst.sort()
#     return lst
    
# def main():
#     # Read each set
#     line1 = sys.stdin.readline()
#     a = make_set(line1)
    
#     line2 = sys.stdin.readline()
#     b = make_set(line2)

#     # call the student's function ...
#     union, sub, super = set_stuff(a, b)
    
#     # ... and print the result
#     # First convert to a list and sort to be sure that the order will always be the same
#     print(make_sorted_list(union))
#     print(sub)
#     print(super)

# if __name__ == "__main__":
#     main()
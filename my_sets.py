# Set Creation
set_A = {1, 2, 3, 4}
set_B = {3, 4, 5, 6}

print("Set A:", set_A)
print("Set B:", set_B)

# Add an element to Set A
set_A.add(10)
print("\nAfter adding 10 to Set A:", set_A)

# Update Set B with multiple elements
set_B.update([7, 8])
print("After updating Set B with 7 and 8:", set_B)

# Remove an element from Set A
set_A.remove(2)  # raises error if not found
print("\nAfter removing 2 from Set A:", set_A)

# Discard an element (safe version of remove)
set_B.discard(100)  # does nothing if 100 is not found
print("After discarding 100 from Set B:", set_B)

# Pop an element (randomly removes one)
popped = set_A.pop()
print(f"\nPopped element from Set A: {popped}")
print("Set A after pop:", set_A)

# Copy a set
copy_A = set_A.copy()
print("\nCopy of Set A:", copy_A)

# Clear a set
copy_A.clear()
print("After clearing copy_A:", copy_A)

# Set Operations
print("\n--- Set Operations ---")
print("Union:", set_A | set_B)
print("Intersection:", set_A & set_B)
print("Difference (A - B):", set_A - set_B)
print("Difference (B - A):", set_B - set_A)
print("Symmetric Difference:", set_A ^ set_B)

# Set Relations
print("\n--- Set Relations ---")
print("Is A subset of B?", set_A.issubset(set_B))
print("Is A superset of B?", set_A.issuperset(set_B))
print("Are A and B disjoint?", set_A.isdisjoint(set_B))
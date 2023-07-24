# Creating variables
collection_1 = (1, "text", 4.5, None)
collection_2 = (1, "text", 4.5, None)
collection_3 = (1, "text", 4.5, None)

character_1 = {"Name": "Harry", "Surname": "Potter", "Age": 17}
character_2 = {"Name": "Harry", "Surname": "Potter", "Age": 17}

print(collection_1 == collection_2 == collection_3)
print(collection_1 is collection_2 is collection_3)

print(character_1 == character_2)
print(character_1 is character_2)

# Change types
collection_1 = list(collection_1)
collection_2 = list(collection_2)
collection_3 = list(collection_3)

character_1 = bool(character_1)
character_2 = bool(character_2)

# Print results
print("-" * 50)
print(collection_1 == collection_2 == collection_3)
print((collection_1 is collection_2) or (collection_1 is collection_3) or (collection_2 is collection_3))
print("-" * 50)
print(character_1 == character_2)
print(character_1 is character_2)

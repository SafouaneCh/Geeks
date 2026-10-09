brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

#Change the number of stores to 2.
brand["number_stores"] = 2

#Use the key [type_of_clothes] to print a sentence that explains who Zaras clients are.
print(f"Zara's clients are {', '.join(brand['type_of_clothes'])}.")

#Add a key called country_creation with a value of Spain.
brand["country_creation"] = "Spain"

#Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

#Delete the information about the date of creation.
del brand["creation_date"]

#Print the last international competitor.
print(brand["international_competitors"][-1])

#Print the major clothes colors in the US.
print(f"The major clothes colors in the US are {', '.join(brand['major_color']['US'])}.")

#Print the amount of key value pairs (ie. length of the dictionary).
print(f"The amount of key value pairs in the brand dictionary is {len(brand)}.")

#Print the keys of the dictionary.
print(f"The keys of the brand dictionary are: {', '.join(brand.keys())}.")

#Create another dictionary called more_on_zara
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}

#Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
brand.update(more_on_zara)


#Print the value of the key number_stores. What just happened ?
print(f"The value of the key number_stores is {brand['number_stores']}.")
#number_stores value is updated and not add cuz the key number_stores already exists in the brand dictionary.

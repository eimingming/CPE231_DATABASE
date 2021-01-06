class Product:
    def __init__(self):
        self.dict = {}

    def create(self, code, name, units):
        # Adds the new product record to products object (dictionary) using parameters code, name, units.
        # Returns dictionary {"Is Error":____ , "Error Message": ____}
        # Check product code in products object
        if code in self.dict:
            return {'Is Error': True, 'Error Message': "Product code '{}' already exists. Cannot Create. ".format(code)}
        else:
            self.dict[code] = {"Name" : name,"Units" : units}
        return {'Is Error': False, 'Error Message': ""}
    
    def read(self, code):
        # Finds the product code in products object and returns 1 record in dictionary form.
        # To return (error message, data) as a tuple:  ({"Is Error": ___, "Error Message": _____}, {"Name": ___, "Units": ___})
        #  where the first one is an error message related as a dictionary, and second one is the data as another dictionary.
        if code in self.dict:
            retProduct = self.dict[code]
        else:
            return ({'Is Error': True, 'Error Message': "Product Code '{}' not found. Cannot Read.".format(code)},{})

        return ({'Is Error': False, 'Error Message': ""},retProduct)
    
    def update(self, code, newName, newUnits):
        # Finds the product code in products object and then changes the name and units to the values in newName, and newUnits.
        # Returns dictionary {"Is Error": ___, "Error Message": _____} 
        if code in self.dict:
            self.dict[code]["Name"] = newName
            self.dict[code]["Units"] = newUnits
        else:
            return {'Is Error': True, 'Error Message': "Product Code '{}' not found. Cannot Update.".format(code)}

        return {'Is Error': False, 'Error Message': ""}
    
    def delete(self, code):
        # Finds the product code in products object and deletes by removing it from the dictionary.
        # Returns dictionary {"Is Error": ___, "Error Message": _____} 
        if code in self.dict:
            del self.dict[code]

        else:
            return {'Is Error': True, 'Error Message': "Product Code '{}' not found. Cannot Delete".format(code)}
        return {'Is Error': False, 'Error Message': ""}

    def dump(self):
        # Will dump all products data by returning 1 dictionary as output.
        return (self.dict)
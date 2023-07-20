def add_hash(a: str):
    return "#".join(a)
def add_underscore(a: str):
    return str(a).replace("#", "_")
def remove_underscore(a: str): 
    return str(a).replace("_", "")
print(remove_underscore(add_underscore(add_hash('Python'))))

#EXTRA CHALLENGE

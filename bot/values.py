
# system for storing inter-file values

data = {}

def addsafe(name,value):
    if data.has_key(name) == False:
        data[name] = value
        return True
    return False

def add(name,value):
    data[name] = value
    return True

def get(self,name):
    return data.get(name)

def keys(self):
    return data.keys()




    









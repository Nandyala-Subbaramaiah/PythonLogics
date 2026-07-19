def add_sprinkline(fun):
    def wrapper(*args, **kwargs):
        print("add sprinkline")
        fun(*args, **kwargs)
    return wrapper
    
def add_fudge(fun):
    def wrapper(*args, **kwargs):
        print("add fudges")
        fun(*args, **kwargs)
    return wrapper
        
@add_fudge    
@add_sprinkline
def get_ice_cream(flavour):
    print("here I am having {flavour} icecream")
    
get_ice_cream("vannila")
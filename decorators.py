"""def add_sprinkles(fun):
    def wrapper(*args, **kwargs):
        print("add sprinkles")
        fun(*args, **kwargs)
    return wrapper

def add_fudge(fun):
    def wrapper(*args, **kwargs):
        print("add fudge")
        fun(*args, **kwargs)
    return wrapper

@add_fudge    
@add_sprinkles
def get_ice_cream(flavour):
    print(f"here I am having {flavour} icecream")

get_ice_cream("vanilla")

def add_sprinkles(fun):
    def wrapper(*args, **kwargs):
        try:
            print("add sprinkles")
            fun(*args, **kwargs)
        except Exception as e:
            print(f"Exception in add_sprinkles: {e}")
    return wrapper

def add_fudge(fun):
    def wrapper(*args, **kwargs):
        try:
            print("add fudge") 
            fun(*args, **kwargs)
        except Exception as e:
            print(f"Exception in add_fudge: {e}")
    return wrapper

@add_fudge    
@add_sprinkles
def get_ice_cream(flavour):
    if flavour == "vanilla":
        raise ValueError("Vanilla is out of stock!")
    print(f"here I am having {flavour} icecream")

get_ice_cream("vanilla")


def decorator(func):
    def wrapper(a, b):
        a += 1  # Modify the first value
        b += 1  # Modify the second value
        return func(a, b)
    return wrapper 

@decorator
def add(a, b):
    return a + b

print(add(5, 3))  # Output: 10 (Instead of 8, because we modify values before addition)

def admin_required(func):
    def wrapper(email,role,*args,**kwargs):
        if role.lower()!="admin":
            return f"Unothorized access for user :{email}"
        return func(email,role,*args,**kwargs)
    return wrapper
    
@admin_required
def access_dashboard(email,role):
    return f"Access granted to {email} as {role}"
    
print(access_dashboard("user@example.com","user"))
print(access_dashboard("admin@example.com","admin"))


#another method 
def role_required(allowed_roles):
    def decorator(func):
        def wrapper(email, role, *args, **kwargs):
            if role.lower() not in allowed_roles:
                return f"Unauthorized access for user: {email} with role: {role}"
            return func(email, role, *args, **kwargs)
        return wrapper
    return decorator

@role_required(["admin", "manager"])  # Specify allowed roles here
def dashboard(email, role):
    return f"Access granted to {email} with role: {role}"

@role_required(["editor", "admin"])  # Specify allowed roles here
def edit_content(email, role):
    return f"Edit content access granted to {email} with role: {role}"

# Test cases
print(dashboard("subbu63@gmail.com", "user"))  # Unauthorized
print(dashboard("rama12@gmail.com", "admin"))  # Authorized
print(edit_content("editor@example.com", "editor"))  # Authorized
print(edit_content("viewer@example.com", "viewer"))  # Unauthorized

"""

#its my practiece code
def roles_required(allowed_roles):
    def admin_required(func):
        def wrapper(email,role,*args,**kwargs):
            if role.lower() not in allowed_roles:
                return f"Unothorized access {email}"
            return func(email,role,*args,**kwargs)
        return wrapper
    return admin_required
    
@roles_required (["admin","manager"])
def dashboard(email,role):
    print(f"granted {email} and {role} perimission")
    
@roles_required(["editors","viewers"])
def edit_product(email,role):
    print(f"granted {email} and {role} perimission")
    
print(dashboard("subbu63@gmail.com","user"))
print(dashboard("rama12@gamil.com","admin"))
print(edit_product("sursa123@gmail.com","editors"))


def changing_chars(func):
    def wrapper(sttr, *args, **kwargs):
        sttr = sttr.upper()  # modify argument
        return func(sttr, *args, **kwargs)
    return wrapper

@changing_chars        
def add(sttr):
    print(f"changing {sttr} character")

add("sub")
REGISTERED_CONSTRUCTORS = {}

def register_constructor(name):
    def decorator(cls):
        REGISTERED_CONSTRUCTORS[name] = cls
        return cls
    return decorator
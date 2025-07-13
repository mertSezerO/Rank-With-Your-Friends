# Registered constructor dictionary for dynamic build
REGISTERED_CONSTRUCTORS = {}

# Decorator for dynamicly create corresponding item in builder
def register_constructor(name):
    def decorator(cls):
        REGISTERED_CONSTRUCTORS[name] = cls
        return cls
    return decorator
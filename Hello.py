




def greet(name: str, shout_count: int = 1):
    if shout_count is greet.__defaults__[0]:
       str=f"Hello, {name}{shout_count * '!'}"
       return str    
    else:
      return f"Hello, {name}{shout_count * '!'}"

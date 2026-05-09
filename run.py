# Dunder __builtins__, __init__
message = "PYTHON: Everything is object!"
print(message)

result = type(message)
print("result:", result)

''' In Python, there are builtin tools:
  (1) TYPES > int float srt list dict
  (2) FUNCTION > print(), len(), type(), srt(), int()
  (3) CONSTANTS > True False None
'''
print(__builtins__)
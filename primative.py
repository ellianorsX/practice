print("===============================")
# in JAVA, variable is a name storage lacation!
# in PYTHON, variable is named referance!


count = 100 
count_type = type(count)
print(f"the count: {count} and type: count_type")

result1 = count.bit_count() #method 
result2 = count.numerator #state
print(result1, result2)


print("==========  string  ===========")
# METHODS: upper(), lower(), title(), find(), replace()



course = "AI Python FullStack"
result = type(course)
print(f"the type of course: {result}")


result = course.title()
print(f"the result: {result}")

result = course.upper()
print(f"the result: {result}")

result = course.replace("FullStack", "MasterClass")
print(f"the result (4): {result}")

print("=========  boolean  ============")


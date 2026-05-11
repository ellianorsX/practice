print("======= Iterable  objects & RANGE =======")
# Iterable objects > string dict tuple list range map filter 
#-- barchasi iterable. For-tsikl bilan aylanish mumkin.> for ... in ...
#   Iterablening har bir elementini navbat bilan oladi. String uchun — har bir harf.
#--f-string f"the letter: {letter}" — o'zgaruvchini matnga qo'shish usuli

range_obj = range(3)
print("range_obj:", range_obj) 

for letter in "MIT":
    print(f"the letter: {letter}")
for ele in range_obj:
    print(f"the element: {ele}")
    

# -- range(1, 6) → 1 dan 5 gacha. 
# range(0, 10, 2) → 0, 2, 4, 6, 8 (juft sonlar). Uchinchi argument — qadam (step).


print("======= DICTIONARY =======")

# Dictionary is JSON object!
person = {"name": "Justin", "age": 25, "single": True}
person_obj = dict(name="Justin", age=25, single=True)
print(f"the person: {person}")
print(f"the person_obj: {person_obj}")

# method: get()
# name = person_obj ["name"]
name = person_obj.get("name")
hobby = person_obj.get("hobby")
balance = person_obj.get("balance", 0)
print(f"the name: {name}, hobby: {hobby} and balance: {balance}")

del person_obj ["single"]
for key in person_obj:
    print(f"the key: {key} > value {person_obj.get(key)}")

# key : value
Har bir yozuv kalitdan (nom) va qiymatdan iborat. Kalit noyob bo'lishi shart.

# .get(key, default)
Kalitni qidirib qiymat beradi. Topilmasa — default qiymat. Xato bermaydi.

# del dict[key]
Ko'rsatilgan kalitni lug'atdan o'chirib tashlaydi.

# person["hobby"] → KeyError! Lekin person.get("hobby") → None, xato bermaydi. Har doim .get() ishlatish xavfsizroq.

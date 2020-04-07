# from narrow to wider int -> float -> complex
# can't convert complex to float to get real section

# int - there is no long in python 3
anInt = 2
print(anInt)
print(type(anInt))

# float
aFloat = 2.1
print(aFloat)
print(type(aFloat))
toInt = int(aFloat)
print(toInt)
print(type(toInt))

# complex - i in math but j in programming and j=-1^.5
aComplex = 2 + 0j #also 2-0j + also aFloat+0j
print(aComplex)
print(aComplex.real)
print(aComplex.imag)
print(type(aComplex))
print(type(complex(aFloat)))
#print(float(aComplex)) #in py3 can't convert complex to float
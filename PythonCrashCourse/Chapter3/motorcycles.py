#motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles)

#motorcycles[0] = 'ducati'
#print(motorcycles)

#motorcycles.append('ducati')
#print(motorcycles)

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

last_owned = motorcycles.pop()
print(motorcycles)
print(f"The last motorcycle I owned was a {last_owned.title()}")


#del(motorcycles[0])

#print(motorcycles)

#del motorcycles[1]

#print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}")


motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive='ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\n A {too_expensive.title()} is too expensive for me")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[-1])

motorcycles = []
print(motorcycles[-1])

guest_list = ['José', 'Severo Ochoa', 'Balzac']

print(f"{len(guest_list)} guests")
for guest in guest_list:
    print(f"{guest.title()}, you are invited to the party.")

missing_guest=guest_list.pop(2)
print(f"{len(guest_list)} guests")
print(f"{missing_guest.title()}, cannot make it to the party")

guest_list.append('Lemaitre')
print(f"{len(guest_list)} guests")
for guest in guest_list:
    print(f"{guest.title()}, you are invited to the party.") 

print('We found a bigger dinner table')
guest_list.insert(0, 'Leia')
guest_list.insert(2,'Dexter')
guest_list.append('Monica')

print(f"{len(guest_list)} guests")
for guest in guest_list:
    print(f"{guest.title()}, you are invited to the party.") 

print('We can only invite two people to the party')

for notguest in range(0,4):
    not_invited=guest_list.pop()
    print(f"Sorry, {not_invited.title()} you cannot attend the party")

print(f"{len(guest_list)} guests")
for guest in guest_list:
    print(f"{guest.title()}, you can still attend the party")
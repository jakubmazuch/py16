tydny = int(input("Zadejte počet týdnů: "))

dny = 7*tydny
hodiny = 24*dny
minuty = 60*hodiny
sekundy = 60*minuty

print(f"{tydny} týdnů má {dny} dnů.")
print(f"{tydny} týdnů má {hodiny} hodin.")
print(f"{tydny} týdnů má {minuty} minut.")
print(f"{tydny} týdnů má {sekundy} sekund.")

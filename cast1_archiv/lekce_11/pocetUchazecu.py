with open("jmena.csv", encoding="utf-8") as f:
    radky = f.readlines()

print(f"Počet uchazečů je {len(radky)}.")

inp = int(input("Masukkan nilai bilangan: "))
total = 0
for a in range(inp):
    nilai = int(input("masukkan nilai: "))
    total += nilai

ratarata = total/inp
print("Rata-Ratanya adalah: ", ratarata)

kendaraan = ["civic","roda empat","1500cc","putih","4"]
print (kendaraan)
kendaraan.append("600jt")
kendaraan.append("turbo")
print (kendaraan)
kendaraan.insert(2,"honda")
print (kendaraan)


print()

operasi = input("Menghitung luas bangun datar")
match operasi:
    case "1":
        sisi= int (input("masukan nilai sisi:"))
        luas= sisi*sisi
        print(luas)
    case "2":
        jari_jari= int (input("masukan nilai jari jari:"))
        luas= 3.14*jari_jari*jari_jari
        print(luas)
    case "3":
        alas= int (input("masukan nilai alas:"))
        tinggi= int(input("masukan nilai tinggi:"))
        luas= 0.5*alas*tinggi
        print(luas)  
    case _:
        print("salah pilih")    
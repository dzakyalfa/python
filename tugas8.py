def profil(nama,alamat,gender,umur,hobi):
    print("Nama",nama)
    print("Alamat",alamat)
    print("Gender",gender)
    print("Umur",umur)
    print("Hobi",hobi)
profil ("Dzaky","Leuwiliang","Laki Laki",18,"membaca")  


def cek_kelulusan(nilai):
    if nilai < 60:
        print("Gagal")
    elif 61 <= nilai <= 70:
        print("Baik")
    elif 71 <= nilai <= 80:
        print("Sangat Baik")
    elif 81 <= nilai <= 100:
        print("Istimewa")
    
    else:
        print("Tidak Lulus")
cek_kelulusan(60)

def ganjil(angka):
    for i in range(1, angka + 1, 2):
        print(i)
ganjil(100)
  
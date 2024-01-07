#Sequence
'''''
tup1 = ('Pensil', 1500, 'Buku', 5000, 'Penggaris', 2000)
print(type(tup1))

tup1 = ['Pensil', 1500, 'Buku', 5000, 'Penggaris', 2000]
print(type(tup1))

dict1 = {'Barang' : 'Pensil', 'Harga' : '1500'}
dict2 = {'Barang' : 'Buku', 'Harga' : '5000'}
dict3 = {'Barang' : 'Penggaris', 'Harga' : '2000'}
print(type(dict1))
print(type(dict2))
print(type(dict3))
'''''

#Function
'''''
def is_prima(x, y):
    print x +" " + y

is_prima(13)
'''''

#Pure Function
'''''
total = 10

def tambah_angka(angka):
    total += angka
    return total
'''''

#Lambda
'''''
double = lambda input : input * 2
print (double(2))
'''''

#List Comprehension
'''''
ganjil = [x for x in range(50) if x % 2 != 0]
print(ganjil)
'''''

#Generator Expression
'''''
ganjil = (i for i in range(50) if i % 2 != 0)

for i in ganjil:
    print (i, end=" ")
'''''

#HOF
'''''
def sisagold(a,b):
    return a-b

sisagold = ('-')
print(f"5-2 = {(5-2)}")
'''''

#Closure
'''''
def hitung_pangkat(pangkat):
    def pangkat_dua(x):
        return x ** pangkat
    
    return pangkat_dua

pangkat_dua = hitung_pangkat(2)
pangkat_tiga = hitung_pangkat(3)

print("Pangkat dua dari 5:", pangkat_dua(5))  # Output: 25
print("Pangkat tiga dari 5:", pangkat_tiga(5))  # Output: 125
'''''

#Decorator
'''''
def dekorator_kalimat(fungsi):
    def fungsi_didekorasi(*args, **kwargs):
        
        hasil_asli = fungsi(*args, **kwargs)

        kalimat_hasil = "Hasilnya adalah benar!" if hasil_asli else "Hasilnya adalah salah!"

        return kalimat_hasil

    return fungsi_didekorasi

@dekorator_kalimat
def hitung_pangkat(pangkat, x):
    return x ** pangkat

hasil_pangkat_dua = hitung_pangkat(2, 5)
hasil_pangkat_tiga = hitung_pangkat(3, 5)

print(hasil_pangkat_dua) 
print(hasil_pangkat_tiga) 
'''''
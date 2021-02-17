# Percabangan : Eksekusi Terpiih
ingin_cepat = False
if ingin_cepat:
    print('jalan lurus aja ya!')
else:
    print('Jalan lain')

print('-' * 20)
'''nilai = int(input('Masukan nilai anda : '))
print('Nilai anda adalah', nilai, '\n')
if nilai >= 90:
    print('Grade A')
elif nilai >= 80 < 90:
    print('Grade B')
elif nilai >= 60 < 80:
    print('Grade C')
elif nilai >= 40 < 60:
    print('Grade D')
else:
    print('Grade E')
'''
# OPERATOR KEANGGOTAAN
'''hewan_yang_ada = ['Ayam', 'Bebek', 'Ikan']
hewan_yang_dicari = input('Masukan hewan yang dicari huruf pertama kapital : ')
if (hewan_yang_dicari in hewan_yang_ada):
    print('hewan yang dicari ada')
else:
    print('Hewan tidak ada')
'''
# Percabangan satu baris
'''nilai = int(input("Masukan nilai : "))
status = 'LULUS' if nilai >= 70 else 'Tidak Lulus'
print(status)
'''

# Percabangan Bertingkat
# Algoritma : Jika seseorang memiliki nilai >= 75 maka dia lulus, dan jika usia mereka < 15 kasih selamat dengan sebutan adek, jk > 15 kakak
'''nilai = int(input("Masukan nilai : "))
usia = int(input("masukan usia : "))
if nilai >= 75:
    if usia < 15:
        print('Selamat anda lulus, adek!')
    else:
        print('Selamat anda lulus, kakak!')
else:
    if usia < 15:
        print('Mohon maaf anda tidak lulus, adek!')
    else:
        print('Mohon maaf anda tidak lulus, kakak!')
'''
# PERULANGAN (For)
'''jumlah_anak = 4
for index_anak in range(1, jumlah_anak+1):
    print(f'hai anak ke {index_anak}')
'''
# PERULANGAN For dengan list
'''list_kota = ['Jakarta', 'Bekasi', 'Bogor', 'Depok', 'Tangerang', 'Bandung', 'Yogyakarta', 'Semarang', 'Malang',
            'Surabaya', 'Denpasar'
]
for kota in list_kota:
    print(kota)
'''
# Mengetahui urutan iterasi for dengan list menggunakan enumerate
'''for i, kota in enumerate(list_kota):
    print(i, kota)
'''
# For bilangan ganjil dan genap menggunakan range dari 0 - 11
'''print('-' * 30)
for i in range (2, 12, 2):
    print('Bilangan genap =', i)

print('-' * 30)
for i in range (1, 12, 2):
    print('Bilangan ganjil =', i)
'''
# Continue & Break
print('skip jika nilai == 15')
for i in range(10, 20):
    # skip jika nilai == 15
    if (i == 15):
        continue

    print(i)
print("-" * 50)
print('stop jika nilai == 15')
for i in range(10, 20):
    #     berhenti jika index = 15
    if (i == 15):
        break
    print(i)

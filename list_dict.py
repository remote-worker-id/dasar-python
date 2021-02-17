# Tipe data list/array
'''
anak = ['Dimas', 'Surya', 'Nug', 'Dede']
print(anak)
anak.append('Pangestu')
print(anak)

print('\nsapa anak ke dua')
print(f'hai {anak[1]}!')

print('\nSapa semua anak')
for a in anak:
    print(f'Hai {a}!')

print('\nSapa semua anak jika jumlah anak tidak diketahui scr pasti krn penambahan append dll')
for a in range(0, len(anak)):
    print(f'Hai {anak[a]}')
'''
# DICTIONARY : Menghubungkan Key dan Value
kamus = {'anak': 'son', 'istri': 'wife', 'ayah': 'father', 'ibu': 'mother'}
print(kamus)
print(kamus['ayah'])

print('\nData info driver disekitar user aplikasi gojek')
data_dari_server_gojek = {
    'tanggal': '2021-07-27',
    'driver_list': [{'nama': 'Dede', 'jarak': 10},
                    {'nama': 'Surya', 'jarak': 30},
                    {'nama': 'Nunu', 'jarak': 100},
                    {'nama': 'Pange', 'jarak': 200},
                    ]
}
print(data_dari_server_gojek)
print(f"\nDriver disekitar sini{data_dari_server_gojek['driver_list']}")
print(f"\nDriver #1 {data_dari_server_gojek['driver_list'][0]}")
print(f"\nDriver terdekat berjarak {data_dari_server_gojek['driver_list'][0]['jarak']} meter")

print('\nMengubah item')
print('tanggal awal : ', data_dari_server_gojek.get('tanggal'))
print('driver list awal : ', data_dari_server_gojek.get('driver_list'))
data_dari_server_gojek['tanggal'] = '2021-02-17'
data_dari_server_gojek['driver_list'] = [{'nama': 'Dimas', 'jarak': 5},
                    {'nama': 'Surya', 'jarak': 30},
                    {'nama': 'Nunu', 'jarak': 100},
                    {'nama': 'Pange', 'jarak': 200},
                    ]
print('setelah diubah : ', data_dari_server_gojek.get('tanggal'))
print('setelah diubah : ', data_dari_server_gojek.get('driver_list'))


print('\nMenampilkan semua item menggunakan For')
for key in data_dari_server_gojek:
    print(f"{key} => {data_dari_server_gojek[key]}")


#      For Else (else akan dieksekusi setelah blok for selesai
print('\nPenggunaan for else')
list_buah = ['Jeruk', 'Mangga', 'Apel', 'Durian', 'Anggur', 'Salak', 'Kelengkeng']
for i in list_buah:
    print(i)
else:
    print('Buah sudah tidak tersedia')

#     For Else+Break digunaakan untuk mengecek item ada atau tidak/mencari indeks item pada list ada/tidak
print('\nPenggunaan for else+break')
buahYangDicari = input('masukan buah yang kamu cari : ')
for i, buah in enumerate(list_buah):
    # ubah katanya menjadi lowercase agar jadi incasesencitive
    if buah.lower() == buahYangDicari.lower():
        print('Buah yang kamu cari berada pada indeks ke -', i)
        break
else:
    print('Buah yang kamu cari tidak ada!')





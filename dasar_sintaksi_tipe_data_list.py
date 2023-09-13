"""
Perhatikan detail-detail kecilnya!!!
"""
daftar_buku = ['Seven habits', 'How to influence people','First things first', '4dx']
print('Tampilkan variable daftar_buku')
print(daftar_buku)

print('\nProses dengan FOR IN')
for buku in daftar_buku:
    print(buku)

print('\nTampilkan isi daftar_buku pada indeks/nomor tertentu')
print(daftar_buku[0])
print(daftar_buku[2])

print('\nTampilkan dengan for in range')
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nTampilkan dengan in range, Dimana tipe data tiap elemen berbeda-beda')
daftar_buku = [1, 'Kenji volume 2', -313, 3.12]
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nKembalikan nilai awal daftar_buku')
daftar_buku = ['Seven habits', 'How to influence people','first things first', '4dx']
print('\nTambahkan 1 buku baru')
daftar_buku.append("Dunia matematika kelas 5")
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nClear list atau membersihkan list')
daftar_buku.clear()
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nGanti elemen pertama')
daftar_buku = ['Seven habits', 'How to influence people','first things first', '4dx']
daftar_buku[0] = 'atom habits'
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nAmbil elemen ke-2')
daftar_buku = ['Seven habits', 'How to influence people','first things first', '4dx']
buku = daftar_buku.pop(1)
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nBuku yang diambil tadi')
print(buku)

print('\nPop atau menghilangkan list paling akhir')
daftar_buku = ['Seven habits', 'How to influence people','first things first', '4dx']
daftar_buku.pop()
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPop -1 atau menghilangkan 1 list/variable sesuai perintah')
daftar_buku = ['Seven habits', 'How to influence people','first things first', '4dx']
daftar_buku.pop(-4)
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])


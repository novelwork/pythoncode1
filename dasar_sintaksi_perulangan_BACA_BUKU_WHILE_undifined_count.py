"""
program perulangan baca buku Metode WHILE sampai paham dan punya kata perintah henti
"""

jumlah_buku = 10
print('ibu menyuruh, "baca semua buku"')

total_jumlah_baca = 0

jumlah_buku_yang_dibaca_dan_dipahami = 0
print(f'jumlah buku yang dibaca dan di pahami {jumlah_buku_yang_dibaca_dan_dipahami}')

while total_jumlah_baca < jumlah_buku * 2 :
    total_jumlah_baca = total_jumlah_baca + 1
    if jumlah_buku_yang_dibaca_dan_dipahami == 9:
        print(f'buku yang ke {jumlah_buku_yang_dibaca_dan_dipahami + 1} belum paham')
    else:
        jumlah_buku_yang_dibaca_dan_dipahami = jumlah_buku_yang_dibaca_dan_dipahami + 1
        print(f'buku yang ke {jumlah_buku_yang_dibaca_dan_dipahami} sudah di baca dan dipahami')

print(f'jumlah buku yang sudah di baca {jumlah_buku_yang_dibaca_dan_dipahami}')

if jumlah_buku_yang_dibaca_dan_dipahami == jumlah_buku:
    print('semua buku yang ibu suruh baca dan pahami sudah selesai')
else:
    print(f'ibu budi tidak bisa membaca dan memahami semua buku, '
          f'budi hanya bisa sampai {jumlah_buku_yang_dibaca_dan_dipahami}')
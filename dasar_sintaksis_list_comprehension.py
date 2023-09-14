print('\nPerintah del')
daftar_buku  = ['Seven habits', 'How to influence people','first things first', '4dx']
del daftar_buku[0] #Menghapus elemen tertentu
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah list dengan list comprehension')
daftar_buku  = ['Seven habits', 'How to influence people','first things first', '4dx']
del daftar_buku [:] #Menghapus semua elemen
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah list dengan list comprehension start')
daftar_buku  = ['Seven habits', 'How to influence people','first things first', '4dx']
del daftar_buku [0:3] #Start:end #kalau menggunkan - berarti di barisan tertentu tidak terhapus
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah list dengan list comprehension STEP')
daftar_buku  = ['Seven habits', 'How to influence people','first things first', '4dx']
del daftar_buku [0::3] #START:END:STEP #Perintah menghapus dengan melangkah beberapa baris tertentu
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru')
daftar_buku  = ['Seven habits', 'How to influence people','first things first', '4dx']
daftar_buku_baru = daftar_buku [:]
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru')
del daftar_buku [:]
for i in range (0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension ganjil')
daftar_buku  = ['1 Seven habits', '2 How to influence people','3 first things first', '4 4dx']
daftar_buku_baru = daftar_buku [0::2]
for i in range (0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension genap')
daftar_buku  = ['1 Seven habits', '2 How to influence people','3 first things first', '4 4dx']
daftar_buku_baru = daftar_buku [0::2] #START:STOP:END
for i in range (0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension: BUANG DIUJUNG')
daftar_buku  = ['1 Seven habits', '2 How to influence people','3 first things first', '4 4dx']
daftar_buku_baru = daftar_buku [0:-1:2] #START:STOP:END
for i in range (0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension genap simplfy')
daftar_buku  = ['1 Seven habits', '2 How to influence people','3 first things first', '4 4dx']
print(daftar_buku[0::2])

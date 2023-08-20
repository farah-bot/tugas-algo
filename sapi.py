print('''
Pilihan sapi : 
1. Sapi Warrior : 690 hari
2. Sapi Mage    : 420 hari
3. Sapi Assasin : 530 hari
4. Sapi Nolep   : 330 hari
''')
jumlah = int(input("Masukkan jumlah sapi : "))
sapi = []
print("Masukkan kode sapi yang ingin dipilih : ")
waktu = 0
for i in range(jumlah):
    sapi_input = int(input())
    sapi.append(sapi_input)
    if sapi_input == 1:
        waktu += 690
    if sapi_input == 2:
        waktu += 420
    if sapi_input == 3:
        waktu += 530
    if sapi_input == 4:
        waktu += 330
    tahun = waktu // 356
    sisa = waktu % 356 
    bulan = sisa // 30
    hari = sisa % 30
print("\nJumlah hari yang diperlukan ialah",tahun, "tahun", bulan, "bulan", hari, "hari")

jumlah = int(input("Masukkan jumlah kata : "))
kata = []
for i in range(jumlah):
    kata_input = str(input("Masukkan kata : "))
    kata.append(kata_input)
for k in kata:
    print("Hasil : ")
    for j in range(len(k)-1):
        if ord(k[j]) > ord(k[j+1]):
            selisih = ord(k[j]) - ord(k[j+1])
            print( k[j],"lebih dari", k[j+1], "selisihnya adalah", selisih)
        if ord(k[j]) < ord(k[j+1]):
            selisih = ord(k[j+1]) - ord(k[j])
            print(k[j],"kurang dari", k[j+1], "selisihnya adalah", selisih)

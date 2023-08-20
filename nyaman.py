kiri = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b']
kanan = ['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm']
kata = []
kata_input= input("Masukkan kata : ")
kata.append(kata_input)
for j in kata:
    for i in range(len(j)-1):
        if (j[i] in kiri) & (j[i+1] in kiri) or (j[i] in kanan) & (j[i+1] in kanan):
            print("False\nPenjelasan : ")
            for i in range(len(j)-1):
                if (j[i] in kiri) & (j[i+1] in kiri):
                    print("Karakter yang berdempetan yakni",j[i],"dan",j[i+1],"berada di satu tangan (kiri)")
                if (j[i] in kanan) & (j[i+1] in kanan):
                    print("Karakter yang berdempetan yakni",j[i],"dan",j[i+1],"berada di satu tangan (kanan)")
            break
        else:
            print("True\nPenjelasan : Setiap karakter selalu bergantian tangan")
            break
        
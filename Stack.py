print("""
     Menu Program
=====================
(+) 1. Push
(+) 2. Pop
(+) 3. Cetak
(+) 4. Keluar
=====================
""")

array=[]
atas = -1

while(True):
    pilihan = int(input("Pilihan : "))
    if(pilihan==1):
        if(atas==4):
            print("Array Penuh")
            continue
        atas+=1
        angka=int(input("Angka : "))
        array.append(angka)

    elif(pilihan==2):
        if(atas==-1):
            print("Array Kosong")
            continue
        array.pop(atas)
        atas-=1
        print("Isi ARRAY : ",array)

    elif(pilihan==3):
        print("Isi ARRAY : ",array)

    elif(pilihan==4):
        print("Terima Kasih")
        break
    
    else:
        print("Masukan pilihan yang benar...")

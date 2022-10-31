def kandag():
    bebek = int(input("jumlah bebek :"))
    batas = int(input("batas per kandang : "))
    rak = 1
    if(bebek<=42):
        while (bebek>batas):
            bebek=bebek-batas
            batas = batas-2
            rak = rak+1
        print("Jumlah susunan : ", rak)
    else:
        print("Tidak bisa memasukkan bebek lebih dari 42 ekor!")

kandag()
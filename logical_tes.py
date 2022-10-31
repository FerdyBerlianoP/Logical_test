def kandag():
    bebek = int(input("jumlah bebek :"))
    batas = 12
    rak = 1
    while (bebek>batas):
        bebek=bebek-batas
        batas = batas-2
        rak = rak+1
    print("Jumlah susunan : ", rak)

kandag()
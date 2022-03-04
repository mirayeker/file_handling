with open("dosya_icerigi.txt", "r") as file:
    print(file.tell())
    file.seek(10)
    print(file.tell())
    icerik = file.read(10)
    print(icerik)
    file.seek(0)
    icerik2 = file.read(5)
    print(icerik2)
    # file.tell -> dosya okumak için imlecin nerede olduğunu soyler
    # file.seek(sayı) -> imlecin nereye gideceğini belirtiriz
    # icerik=file.readline(sayı) -> kaç bayt okuyacagını belirtiriz

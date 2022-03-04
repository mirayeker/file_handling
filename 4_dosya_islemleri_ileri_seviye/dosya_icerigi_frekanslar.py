class Dosya():
    def __init__(self):
        with open("metin.txt","r",encoding="utf-8") as file :
            dosya_icerigi =file.read()

            kelimeler=dosya_icerigi.split()

            self.sade_kelimeler=list()

            for i in kelimeler:
                i=i.strip("\n") #boşluklardan böldük
                i=i.strip(" ")
                i=i.strip(".")
                i=i.strip(",")
                self.sade_kelimeler.append(i)

    def tum_kelimeler(self):
        kelimeler_set=set()
        for i in self.sade_kelimeler:
            kelimeler_set.add(i)
        print("Tüm kelimeler ....")
        for i in kelimeler_set:
            print(i)
            print("************************")

    def kelime_frekans(self):
        kelime_sozluk=dict()

        for i in self.sade_kelimeler:
            if ( i in kelime_sozluk):
                kelime_sozluk[i] +=1
            else :
                kelime_sozluk[i] =1
        for kelime,sayi in kelime_sozluk.items():
            print("{} kelimesi {} defa geçiyor".format(kelime,sayi))
            print("----------------------------------")

dosya= Dosya()
dosya.tum_kelimeler()
dosya.kelime_frekans()
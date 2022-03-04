#stringte bulunan harflerin frekansları buluyoruz:

string="ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb".lower()
harfler=list()
for i in string:
    i=i.strip("")
    i=i.strip(".")
    i=i.strip(",")
    i=i.strip("'")

    harfler.append(i)
print(harfler)
harf_sozluk=dict()
for i in harfler:
    if(i in harf_sozluk):
        harf_sozluk[i] +=1
    else:
        harf_sozluk[i]=1

for harf,sayi in harf_sozluk.items():
    print("{} harfi {} kez kullanılmıştır.".format(harf,sayi))
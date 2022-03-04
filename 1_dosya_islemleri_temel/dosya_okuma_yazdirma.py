file=open("Mirisko.txt","w")
file.write("""There's a whole lot of women in me
You're wondering what I mean, I see
Meet the Good, the Bad and the Crazy
I come in many shades and shapes
So don't put up the barricades
I'm not here to make a war\n""")
file.close()
try:
    file=open("Bilgiler.txt","r",encoding ="utf-8")
except FileNotFoundError:
    print("Dosya bulunamadı")
file=open("Mirisko.txt","r")
for i in file:
    print(i,end="")
file.close()
file=open("Mirisko.txt","r")
icerik=file.read() #imlec dosyanın sonuna kadar gittiği için imleç orada kaldı ve içerik2 dosyanın sonunda bir şey bulamadığı için bir şey yazdıramadı
print("Dosyanın icerigi: ********\n")
print(icerik)
icerik2=file.read()
print("dosyanın içeriği2:*********\n")
print(icerik2) #doysnaın geri kalanında bbir şey olmadığı için ekrana bir şey yazdırmadı
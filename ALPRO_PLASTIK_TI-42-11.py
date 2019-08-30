print("welcome to link aja")
db_phone = '000000000000'
db_pin = '111111'
berhasil = 0
saldo=1500000
while(berhasil !=1 ) :
    phone=(input("input your phone number :"))
    pin=(input("input your pin :"))
    if db_phone == phone and db_pin == pin:
        print("login berhasil")
        berhasil=1
    else :
        print("login gagal")
        berhasil=berhasil
def option():
    print("(1)        saldo")
    print("(2)        debit")
    print("(3)        kredit")
    print("(4)        Quit")
if berhasil ==1:
    option()   

Option=int(input("pilih menu: "))

if Option==1:
    print("saldo  Rp. ",saldo)
    option()
    Option=int(input("pilih menu: "))


if Option==2:
    print("saldo  Rp. ",saldo)
    Debit=float(input("masukan jumlah yang akan di setor Rp. "))
    if Debit>0:
        saldo=(saldo+Debit)
        print("saldo akhir  Rp. ",saldo)
    else:
        print("tidak tersedia")
    option()
    Option=int(input("pilih menu: "))

if Option==3:
    print("saldo Rp. ",saldo)
    kredit=float(input("Enter kredit amount Rp. "))
    if kredit>0:
        saldo=(saldo-kredit)
        print("Saldo Akhir  Rp. ",saldo)
    elif kredit>saldo:
        print("saldo anda tidak mencukupi")
    else:
        print("saldo anda tidak mencukupi")
    option()
    Option=int(input("pilih menu: "))


if Option==4:
    exit()

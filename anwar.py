sim = str(input("Jenis operator anda : "))
ipk = float(input("IPK anda : "))

if sim == "Telkomsel" and ipk >= 3 :
    print("Selamat anda mendapatkan IP X")
elif sim == "Telkomsel" and 2.75 <= ipk <= 3 :
    print("Selamat anda mendapatkan PS4")
elif sim == "Telkomsel" and 2.25 <= ipk <= 2.75 :
    print("Selamat anda mendapatkan voucher gratis OYO")
else:
    print("Selamat dan terimakasih")
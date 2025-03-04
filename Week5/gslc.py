# print("\n")







# nama = "rendi fuji wikarta"
# nim = "2802474293"

# for _ in range(4):
#     print("-----------------------------------")
#     print(f"Halo {nama.title()} - {nim}")
#     score = int(input("Input nilai: "))

#     if score >= 90 and score <= 100:
#         predikat = "A"
#     elif score >= 80:
#         predikat = "B"
#     elif score >= 60:
#         predikat = "C"
#     elif score >= 40:
#         predikat = "D"
#     else:
#         predikat = "E"

#     print(f"Predikat {predikat}")
# print("-----------------------------------")    







print("\n")







nama = "rendi fuji wikarta"
buah_favorit = ["Durian", "Mangga", "Jambu", "Papaya", "Jeruk"]

print("-----------------------------------")    
for i in range(2):
    print(f"Hai {nama.title()}")
    buah_input = input("Masukkan nama buah: ").title()
    # pisah input buah menggunakan " dan "
    buah_list = buah_input.split(" Dan ")

    for buah in buah_list:
        buah_available = True
        if buah in buah_favorit:
            continue
        else:
            buah_available = False
            break

    if buah_available:
        print("Buah yang anda cari tersedia!")
    else:
        print("Buah yang anda cari tidak tersedia!")
    print("-----------------------------------")

















print("\n")
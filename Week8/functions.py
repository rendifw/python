# def binusian(year):
#     print("Hai, I'm Binusian", year)

# binusian(2026)
# POINT: 3



# def describe(jurusan, universitas):
#     print("Saya adalah mahasiswa", jurusan)
#     print(f"Jurusan {jurusan} ada di {universitas.upper()}")

# describe("SI", "BINUS")
# POINT: 7



# def x(pertama, kedua, ketiga):
#     full = f"{pertama} {kedua} {ketiga}".title()
#     return full

# saya = x("saya", "jago", "coding")
# print(saya)
# POINT: 7




# def x(universitas, *semua_jurusan):
#     print(f"{universitas} University punya beberapa jurusan yaitu:")
#     for jurusan in semua_jurusan:
#         print(f"- {jurusan}")

# def y(universitas, *semua_kampus):
#     print(f"\nJarak lokasi jurusan {universitas} dari Anggrek ke Syahdan sekitar 1km dan 5km, detail:")
#     for kampus in semua_kampus:
#         print(f"- BINUS {kampus.title()}")
    
# x("BINUS", "SOIS", "SOCS", "BBS")
# y("BINUS", "Anggrek", "Syahdan", "Kijang")
# POINT: 15
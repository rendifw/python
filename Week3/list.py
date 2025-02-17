# 1
x = "Saya adalah mahasiswa"
jurusan = ['SOIS', 'SOCS', 'SOA', 'BBS']
message = f"{x} {jurusan[0]}"
print(message)


# 2
jurusan = ['SOIS', 'SOCS', 'SOA', 'BBS']
jurusan.sort()
print(jurusan)


# 3
jurusan = ['SOIS', 'SOCS', 'SOA', 'BBS']
jurusan.sort(reverse=True)
print(jurusan)


# 4
y = "Saya adalah mahasiswa double degree"
message2 = f"{y} {jurusan[0]} & {jurusan[3]}"
print(message2)


# 5
jurusan = ['SOIS', 'SOCS', 'SOA', 'BBS']
z = "saya adalah mahasiswa"
message3 = f"{z.upper()} {jurusan[0].lower()}"
print(message3)
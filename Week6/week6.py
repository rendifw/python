# x = {}
# x['nilai'] = 65
# x['result'] = "failed"
# print(f"nilai adalah {x['nilai']}; result = {x['result']}")

# x['result'] = "pass"
# print(f"nilai adalah {x['nilai']}; result = {x['result']}")

# del x['result']
# print(x)
# print(f"nilai adalah {x['nilai']}; result {x}")





 
Erik = {"nama": "Erik", "jurusan": "SIS"}
Vincent = {"nama": "Vincent", "jurusan": "SOCS"}
Lisa = {"nama": "Lisa", "jurusan": "BBS"}
Joy = {"nama": "Joy", "jurusan": "DCS"}
students = [Erik, Vincent, Lisa, Joy]

for student in students:
    print(student)
    
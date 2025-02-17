
namaTemen = ['Eric', 'Vincent', 'Brandon', 'Fritz', 'Nicholus', 'Nathaniel', 'Syafiq', 'Agito', 'Ardell', 'Adho']
print(namaTemen)

# namaTemen.extend(['Diko', 'Angel', 'Tracey', 'Kheren', 'Reynaldi'])
namaTemen.append('Diko')
namaTemen.append('Angel')
namaTemen.append('Tracey')
namaTemen.append('Kheren')
namaTemen.append('Reynaldi')
print(namaTemen)

del namaTemen[0:13]
print(namaTemen)
   
namaTemen.sort(reverse = True)
print(namaTemen)
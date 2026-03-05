# NAMA  : Stella Be Lim
# KELAS : 9B
# ---------------------------------------------------------
# LATIHAN: REVIEW LIST PYTHON
#Diberikan sebuah data acak nilai ujian siswa. Buatlah program yang mengurutkan data tersebut 
#dari nilai tertinggi ke terendah. Kemudian, pisahkan 3 nilai tertinggi sebagai penerima beasiswa, 
#dan hapus nilai terendah (nilai di bawah 60) karena dianggap tidak lulus. 
#Gunakan data awal berikut: nilai_ujian = [75, 55, 90, 85, 45, 95, 80] 
# ---------------------------------------------------------

# OUTPUT
#Data nilai asli: [75, 55, 90, 85, 45, 95, 80] 
#Data setelah diurutkan (Descending): [95, 90, 85, 80, 75, 55, 45] 
#Tiga nilai tertinggi (Penerima Beasiswa): [95, 90, 85] 
#Daftar nilai yang lulus: [95, 90, 85, 80, 75]
# ---------------------------------------------------------

# Tulis kodemu di bawah ini:

#Data awal
nilai_ujian = [75, 55, 90, 85, 45, 95, 80]
print(f'Data nilai asli: {nilai_ujian}')
#Data setelah diurutkan
nilai_ujian.sort(reverse=True)
print(f'Data setelah diurutkan (Descending):{nilai_ujian}')
#Tiga nilai tertinggi(penerima beasiswa)
beasiswa = nilai_ujian[:3]
print(f'Tiga nilai tertinggi (Penerima Beasiswa):{beasiswa}')
#Daftar nilai yang lulus
lulus = [nilai for nilai in nilai_ujian if nilai >= 60]
print(f'Daftar nilai yang lulus:{lulus}')
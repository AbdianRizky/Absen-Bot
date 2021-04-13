import os
from lms import LMS
from dotenv import load_dotenv

load_dotenv()
username    = os.getenv('USERNAME_LMS') or input("Username = ")
password    = os.getenv('PASSWORD_LMS') or input("Password = ")
destination = input('Mau kemana kamu? [kelas/dashboard]: ').lower()

def get_kelas(kelas):
  return {
    "1": "animasi",
    "2": "dgp",
    "3": "bk",
    "4": "sunda",
    "5": "pjok",
    "6": "pkwu",
    "7": "inggris",
    "8": "mtk",
    "9": "indo",
  }.get(kelas)

print('Pilihan Kelas:')
print('1. Animasi')
print('2. DGP')
print('3. BK')
print('4. Sunda')
print('5. PJOK')
print('6. PKWU')
print('7. B. Inggris')
print('8. MTK')
print('9. B. Indonesia')
input_kelas = input("Pilih Kelas Sesuai Nomor atau Nama = ")

if input_kelas.isdigit():
  nama_kelas = get_kelas(input_kelas)
else:
  nama_kelas  = input_kelas


lms = LMS(username=username, password=password)
if destination == 'kelas':
  lms.go_to_class(nama_kelas)
elif destination == 'dashboard':
  lms.go_to_dashboard()
else:
  lms.close()
  print('Upss... aku ga tau kamu mau kemana, mungkin kamu typo, pastikan ejaannya benar yaa')
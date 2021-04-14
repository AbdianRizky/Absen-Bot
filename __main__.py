import discord
import os
from lms import LMS
from dotenv import load_dotenv

load_dotenv()
TOKEN       = os.getenv('DISCORD_TOKEN')
username    = os.getenv('USERNAME_LMS') or input("Username = ")
password    = os.getenv('PASSWORD_LMS') or input("Password = ")
destination = input('Mau kemana kamu? [kelas/dashboard/absen]: ').lower()

if destination != 'kelas' and destination != 'dashboard' and destination != 'absen':
  print("ERROR: Pastikan pilihan mu sesuai dengan pilihan diatas!")
  exit()

def get_kelas(kelas):
  return {
    "1": "animasi",
    "2": "dgp",
    "3": "bk",
    "4": "sunda",
    "5": "pjok",
    "6": "pkwu",
    "7": "b. inggris",
    "8": "mtk",
    "9": "b. indonesia",
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


lms = LMS(username, password)
if destination == 'kelas':
  lms.ke_kelas(nama_kelas)
elif destination == 'dashboard':
  lms.ke_dashboard()
elif destination == 'absen':
  lms.absen(nama_kelas)
else:
  lms.close()
  print('Upss... aku ga tau kamu mau kemana, mungkin kamu typo, pastikan ejaannya benar yaa')

class SendReportToDiscord(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  async def on_message(self, message):
    print('Message from {0.author}: {0.content}'.format(message))
    if message.author == self.user:
      return

    if message.content.startswith('$hello'):
      await message.channel.send()

report = SendReportToDiscord()
report.run(TOKEN)



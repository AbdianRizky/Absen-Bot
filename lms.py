from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
driver = "D:\\Programs\\chromedriver.exe"
login_url = "https://learning.smkn1cibinong.sch.id/login/index.php"

class LMS:
  def __init__(self, username=None, password=None):
      self.chrome = webdriver.Chrome(chrome_options = options, executable_path = driver)
      self.username = username
      self.password = password

  def login(self):
    if self.chrome.current_url == login_url:
      input_username = self.chrome.find_element_by_id("username")
      input_username.send_keys(self.username)
      input_password = self.chrome.find_element_by_id("password")
      input_password.send_keys(self.password)
      self.chrome.find_element_by_id("loginbtn").click()

  def close(self):
    self.chrome.close()

  def go_to_dashboard(self):
    self.chrome.get('https://learning.smkn1cibinong.sch.id/my/')
    self.login()
    print("login ke dashboard sukses")

  def go_to_class(self, kelas=None):
    kelas_id = {
      "animasi": "65",
      "dgp": "63",
      "bk": "168",
      "sunda": "253",
      "pjok": "250",
      "pkwu": "245",
      "b. inggris": "244",
      "mtk": "239",
      "b. indonesia": "236",
    }.get(kelas)

    if kelas is not None:
      self.chrome.get(f'https://learning.smkn1cibinong.sch.id/course/view.php?id={kelas_id}')
      self.login()
      print("login ke kelas sukses")
    else:
      self.chrome.get('https://learning.smkn1cibinong.sch.id/my/')
      self.login()
      print("login ke dashboard sukses")


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
driver = "D:\\Programs\\chromedriver.exe"
login_url = "https://learning.smkn1cibinong.sch.id/login/index.php"
dashboard_url = "https://learning.smkn1cibinong.sch.id/my/"
home_url = "https://learning.smkn1cibinong.sch.id"

class LMS:
  def __init__(self, username, password):
    """ 
    Parameters
    ----------
    username: str
          username lms
    password: str
          password lms
    """
    self.chrome = webdriver.Chrome(chrome_options = options, executable_path = driver)
    self.username = username
    self.password = password

  def login(self):
    """ login ke LMS

    jika current_url sama dengan home dan dashboard url, maka anda sudah login.
    jika current_url tidak sama dengan home, dashboard atau login url, maka login gagal.

    Returns
    -------
    string
        mengembalikan status login untuk validasi di login status nanti.
    """
    if self.chrome.current_url == login_url:
      self.chrome.find_element_by_id("username").send_keys(self.username)
      self.chrome.find_element_by_id("password").send_keys(self.password)
      self.chrome.find_element_by_id("loginbtn").click()
      return "sukses"
    elif self.chrome.current_url == home_url or self.chrome.current_url == dashboard_url:
      return "sudah login"
    else:
      return "gagal"
  

  def login_status(self): 
    """ menampilkan status login Anda berdasarkan pengembalian dari method self.login()

    Returns
    -------
    string
        mengembalikan status login
    """
    if self.login() == "sukses":
      return "Login berhasil"
    elif self.login() == "sudah login":
      return "Anda sudah login sebelumnya"
    elif self.login() == "gagal":
      return "Anda gagal login"

  def close(self):
    """ 
    menutup software chrome selenium 
    """
    self.chrome.close()

  def ke_dashboard(self):
    """ menuju dashboard LMS chrome selenium 
    akan login jika belum login

    Returns
    ---------
    string
        mengembalikan status login ke dashboard
    """
    self.chrome.get('https://learning.smkn1cibinong.sch.id/my/')
    self.login()
    return "login ke dashboard sukses"

  def ke_kelas(self, kelas=None):
    """ menuju ke kelas sesuai dengan nama kelas di parameter kelas
    
    jika parameter kelas tidak ada maka akan menuju ke dashboard 

    Parameter
    -----------
    kelas: str, optional
        untuk menandakan kelas mana yang akan dituju (default: None)

    Returns
    -------
    string
        mengembalikan status login ke kelas atau dashboard.
    """
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
      return "login ke kelas sukses"
    else:
      self.chrome.get(dashboard_url)
      self.login()
      return "login ke dashboard sukses"

  def absen(self, kelas=None):
    """ menuju ke kelas sesuai dengan nama kelas di parameter kelas
    
    jika parameter kelas tidak ada maka akan menuju ke dashboard 

    Parameter
    -----------
    kelas: str, optional
        untuk menandakan kelas mana yang akan dituju untuk absen (default: None)

    Returns
    -------
    string
        mengembalikan status.
    """
    kelas_id = {
      "animasi": "1294",
      "dgp": "2268",
      "bk": "3128",
      "sunda": "7106",
      "pjok": "7200",
      "pkwu": "7773",
      "b. inggris": "7145",
      "mtk": "6865",
      "b. indonesia": "6802",
    }.get(kelas)

    if kelas is not None:
      self.chrome.get(f'https://learning.smkn1cibinong.sch.id/mod/attendance/view.php?id={kelas_id}')
      self.login()
      print(self.chrome.find_element_by_css_selector(".statuscol.cell.c2").text)
      print("login ke kelas sukses")
    else:
      self.chrome.close()
      print('error')

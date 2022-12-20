from lib2to3.pgen2 import driver
import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# Variable
url = "https://opensource-demo.orangehrmlive.com/"
username = "Admin"
password = "admin123"


class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    #Test Case 1   
    def test_FPQBS_1(self): 
        # steps
        driver = self.driver # buka web browser
        driver.get(url) # buka situs
        time.sleep(3)

        driver.find_element(By.ID,"txtUsername").send_keys(username) # isi username
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys(password) # isi password
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        current_url = driver.current_url
        self.assertIn(current_url, 'https://opensource-demo.orangehrmlive.com/index.php/dashboard')
    #Test Case 2
    def test_FPQBS_2(self): 
        # steps
        driver = self.driver # buka web browser
        driver.get(url) # buka situs
        time.sleep(3)

        driver.find_element(By.ID,"txtUsername").send_keys("testlogin") # isi wrong username
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys(password) # isi password
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.ID,"spanMessage").text
        self.assertIn('Invalid',response_data) 

    #Test Case 3
    def test_FPQBS_3(self): 
        # steps
        driver = self.driver # buka web browser
        driver.get(url) # buka situs
        time.sleep(3)

        driver.find_element(By.ID,"txtUsername").send_keys(username) # isi username
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("passAdmin") # isi wrong password
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.ID,"spanMessage").text
        self.assertIn('Invalid',response_data) 

    #Test Case 4
    def test_FPQBS_4(self): 
        # steps
        driver = self.driver # buka web browser
        driver.get(url) # buka situs
        time.sleep(3)

        driver.find_element(By.ID,"txtUsername").send_keys(username) # isi username
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("") # kosongkan password
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.ID,"spanMessage").text
        self.assertIn('empty',response_data) 

    #Test Case 5
    def test_FPQBS_5(self): 
        # steps
        driver = self.driver # buka web browser
        driver.get(url) # buka situs
        time.sleep(3)

        driver.find_element(By.ID,"txtUsername").send_keys("") # kosongkan username
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys(password) # isi password
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.ID,"spanMessage").text
        self.assertIn('empty',response_data) 
    
    #Test Case 6
    def test_FPQBS_4(self): 
        # steps
        driver = self.driver # buka web browser
        driver.get(url) # buka situs
        time.sleep(3)

        driver.find_element(By.ID,"txtUsername").send_keys("") # kosongkan username
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("") # kosongkan password
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click() # klik tombol sign in
        time.sleep(1)
    def tearDown(self): 
        self.driver.close() 
if __name__ == "__main__": 
    unittest.main()  
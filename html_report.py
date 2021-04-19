from selenium import webdriver
import unittest
import HtmlTestRunner


class OrangeHRMTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
        cls.driver.maximize_window()

    def testHomePage(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.assertEqual("OrangeHRM", self.driver.title, "Title Not Match")

    def test_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_name("txtUsername").send_keys("Admin")
        self.driver.find_element_by_name("txtPassword").send_keys("admin123")
        self.driver.find_element_by_name("Submit").click()
        self.assertEqual("OrangeHRM", self.driver.title, "Title Not Match")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Quite")


# We need to terminal command for html report .
# command example: python html_report.py

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/HTML Report and POM/report'))

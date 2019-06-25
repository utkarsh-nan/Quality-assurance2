import os
from selenium import webdriver
import unittest
import HtmlTestRunner
import time


class ExoviewerUI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_A_home(self):
        self.driver.get("http://localhost:4000/")
        # self.driver.get("http://192.168.1.17:4000/")
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div/span/button[1]").click()
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div/span/button[2]").click()
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div/span/button[3]").click()
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div/span/button[4]").click()
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/nav/nav/ol/li[1]/a").click()
        self.driver.implicitly_wait(5)
        time.sleep(3)

    def test_B_importchips(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/nav/nav/ol/li[1]/a").click()
        self.driver.find_element_by_xpath("//input[@type=\'file\']").send_keys(os.getcwd()+'./18K1D01.CHIP0172.xml')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/button[2]").click()

    def test_C_prescan(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/nav/nav/ol/li[3]/a").click()
        time.sleep(4)
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[3]/div[1]/div[1]/div/div[1]/div[1]"
                                          "/input").send_keys("TTS")
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[3]/div[1]/div[1]/div/div[2]/div[2]/"
                                          "table/tbody/tr[1]/td[1]/span/span[1]/input").click()
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[3]/div[1]/div[2]/div/div[2]/div[2]/"
                                          "table/tbody/tr[2]/td[1]/span/span[1]/input").click()
        self.driver.find_element_by_id("inputSearch").send_keys("prescan_experiment")
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[3]/div[2]/div[2]/a/button").click()
        # self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[1]/div/span[3]/a").click()
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div[2]/div[4]/button").click()
        self.driver.implicitly_wait(17)
        time.sleep(12)

    def test_D_postscan(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/nav/nav/ol/li[5]/a").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[3]/div/div[1]/div/div[1]/div[1]/"
                                          "input").send_keys("TTS")
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[3]/div/div[1]/div/div[2]/div[2]/"
                                          "table/tbody/tr[3]/td[1]/span/span[1]/input").click()
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[3]/div/div[2]/div/div[2]/div[2]/"
                                          "table/tbody/tr[1]/td[1]/span/span[1]/input").click()
        time.sleep(2)
        self.driver.find_element_by_id("inputSearch").send_keys("postscan_experiment")
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[4]/div[2]/a/button").click()
        self.driver.implicitly_wait(12)
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div[2]/"
                                          "table/tbody/tr[1]/td[1]/span/span[1]/input").click()
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div[2]/"
                                          "table/tbody/tr[1]/td[3]").click()
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div[2]/"
                                          "table/tbody/tr[1]/td[3]/form/input").send_keys("Newsample")
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div[2]/"
                                          "table/tbody/tr[1]/td[4]/div/select").click()
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div[2]/"
                                          "table/tbody/tr[1]/td[4]/div/select").send_keys("Saliva")

        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div[2]/"
                                          "table/tbody/tr[1]/td[5]").click()
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div[2]/"
                                          "table/tbody/tr[1]/td[5]/form/input").clear()
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div[2]/"
                                          "table/tbody/tr[1]/td[5]/form/input").send_keys("18")
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div[2]/"
                                          "table/tbody/tr[1]/td[6]").click()
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div[2]/"
                                          "table/tbody/tr[1]/td[6]/form/input").clear()
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div[2]/"
                                          "table/tbody/tr[1]/td[6]/form/input").send_keys("1:5")
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div[2]/"
                                          "table/tbody/tr[2]/td[1]/span/span[1]/input").click()
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[3]/div[2]/a/button").click()
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div[2]/div[3]/button[2]").click()
        self.driver.implicitly_wait(17)
        time.sleep(12)
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/nav/nav/ol/li[7]/a").click()

    def test_F_ResultsAnalysis(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/nav/nav/ol/li[7]/a").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[3]/div[1]/div/div[1]/input"). \
            send_keys("Postscan")
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[3]/div[1]/div/div[2]/div[4]/table/"
                                          "tbody/tr[1]/th").click()
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[3]/div[2]/div/div[2]/div[2]/table/"
                                          "tbody/tr[1]/th").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[3]/div[3]/div/div[2]/div[2]/table/"
                                          "tbody/tr[1]/td[1]/span/span[1]/input").click()
        self.driver.find_element_by_id("inputSearch").send_keys("Analyze_experiment")
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[4]/div[2]/a/button").click()
        self.driver.find_element_by_id("inputSearch").send_keys("Analyze_Summary")
        # self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[1]/span[3]/a").click()
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[5]/div[2]/a/button").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

"""
suite = unittest.TestLoader().loadTestsFromTestCase(ExoviewerUI)
unittest.TextTestRunner(verbosity=2)
output = open("results.html","w")
runner = HtmlTestRunner.HTMLTestRunner(stream=output)
runner.run(suite)
"""

if __name__ == '__main__':
    unittest.main()









import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self, setup):
         self.logger.info("*********** Test_001_Login **********")
         self.logger.info("*********** Verifying Home Page Title **********")
         self.driver = setup
         self.driver.maximize_window()
         self.driver.get(self.baseURL)
         act_title = self.driver.title
         # validate page title
         if act_title == "Your store. Login":
             self.driver.close()
             assert True
             self.logger.info("*********** Home Page title test is passed **********")
         else:
             self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")     # capture screenshot of failed test case
             self.driver.close()
             assert False
             self.logger.error("*********** Home Page title test is failed **********")


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        # self.logger.info("*********** Verifying Login test **********")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(10)
        self.lp = LoginPage(self.driver)    # create object for LoginPage
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.driver.implicitly_wait(10)

        act_title = self. driver.title
        # validate page title
        if act_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            assert True
            self.logger.info("*********** Login test is passed **********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")     # capture screenshot of failed test case
            self.driver.close()
            assert False
            self.logger.error("*********** Login test is failed **********")




# To run with specific browser:
# pytest -v -s testCases/test_login.py --browser chrome
# pytest -v -s testCases/test_login.py --browser ie

# To run test in parallel:
# pytest -v -s -n=2 testCases/test_login.py --browser chrome

# To run generate html report
# pytest -v -s -n=2 --html=Reports\report.html testCases/test_login.py --browser chrome

# To capture logs in html report, remove -s
# pytest -v -n=2 --html=Reports\report.html testCases/test_login.py --browser chrome

# To run test by group/markers
# pytest -v -m "sanity" --html=Reports/report.html testCases/ --browser chrome
# pytest -v -m "sanity and regression" --html=Reports/report.html testCases/ --browser chrome
# pytest -v -m "sanity or regression" --html=Reports/report.html testCases/ --browser chrome

# for the run.bat file, need to set root directory to project directory then run as admin
# make sure to use different file name for html reports when running with different browsers in run.bat file





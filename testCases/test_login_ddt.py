import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("*********** TEST_002_DDT_Login **********")
        self.logger.info("*********** Verifying Login test **********")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(10)

        self.lp = LoginPage(self.driver)    # create object for LoginPage

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of Rows i a Excel:", self.rows)
        lst_status=[]           # Empty list variable

        for r in range(2,self.rows+1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setEmail(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self. driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("******** Passed ******")
                    self.lp.clickLogout();
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("******** Failed ******")
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("******** Failed ******")
                    self.lp.clickLogout();
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("******** Passed ******")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("********** Login DDT test passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.info("********** Login DDT test failed **********")
            self.driver.close()
            assert False

        self.logger.info("********** End of Login DDT Test **********")
        self.logger.info("********** Completed TEST_002_DDT_Login **********")




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
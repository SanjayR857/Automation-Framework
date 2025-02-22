import time
import pytest
from Pytest_Framewrok_UI_1.pageObjects.HomePage import HomePage
from Pytest_Framewrok_UI_1.pageObjects.LoginPage import LoginPage
from Pytest_Framewrok_UI_1.pageObjects.MyAccountPage import MyAccountPage
from Pytest_Framewrok_UI_1.utilities import XLUtils
from Pytest_Framewrok_UI_1.utilities.readProperties import ReadConfig
from Pytest_Framewrok_UI_1.utilities.customLogger import LogGen
import os

class Test_Login_DDT():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # Logger

    path = os.path.abspath(os.curdir)+"\\testdata\\Opencart_LoginData.xlsx"

    def test_login_ddt(self,setup):
        self.logger.info("**** Starting test_003_login_Datadriven *******")
        self.rows= XLUtils.getRowCount(self.path, 'Sheet1')
        lst_status=[]

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)  # HomePage Page Object Class
        self.lp = LoginPage(self.driver)  # LoginPage Page Object Class
        self.ma = MyAccountPage(self.driver)  # MyAccount Page Object class

        for r in range(2,self.rows+1):
            self.hp.clickMyAccount()
            self.hp.clickLogin()

            self.email= XLUtils.readData(self.path, "Sheet1", r, 1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)
            self.lp.setEmail(self.email)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(3)
            self.targetpage=self.lp.isMyAccountPageExists()

            if self.exp=='Valid':
                if self.targetpage==True:
                    lst_status.append('Pass')
                    self.ma.clickLogout()
                else:
                    lst_status.append('Fail')
            elif self.exp=='Invalid':
                if self.targetpage == True:
                    lst_status.append('Fail')
                    self.ma.clickLogout()
                else:
                    lst_status.append('Pass')
        self.driver.close()
        #final validation
        if "Fail" not in lst_status:
            assert True
        else:
            assert False
        self.logger.info("******* End of test_003_login_Datadriven **********")

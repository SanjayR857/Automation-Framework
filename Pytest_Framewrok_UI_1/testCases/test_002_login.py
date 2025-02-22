import pytest

from Pytest_Framewrok_UI_1.pageObjects.HomePage import HomePage
from Pytest_Framewrok_UI_1.pageObjects.LoginPage import LoginPage
from Pytest_Framewrok_UI_1.utilities.readProperties import ReadConfig
from Pytest_Framewrok_UI_1.utilities.customLogger import LogGen
import os

class Test_Login():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # Logger

    user = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    @pytest.mark.sanity
    def test_login(self,setup):
        self.logger.info("******* Starting test_002_login **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickLogin()

        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.user)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.targetpage=self.lp.isMyAccountPageExists()
        if self.targetpage==True:
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_login")
            self.driver.close()
            assert False

        self.logger.info("******* End of test_002_login **********")

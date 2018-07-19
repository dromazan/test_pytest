from selenium import webdriver
import PageObject.BasePage
from selenium.webdriver.common.by import By
from PageObject.BasePage import BasePage


class GoogleForm(BasePage):

    def fill_email_field(self, value):
        elem = self.driver.find_element(By.XPATH, '//input[@type = "email"]')
        elem.send_keys(value)

    def clear_email_field(self):
        self.driver.find_element(By.XPATH, '//input[@type = "email"]').clear()

    def email_field(self):
        return self.driver.find_element(By.XPATH, '//input[@type = "email"]')

    def email_exception_field(self):
        return self.driver.find_element(By.XPATH, '//div[@role="alert"][1]')

    def date_field_chrome(self):
        return self.driver.find_element(By.XPATH, '//input[@type="date"]')

    def day_field(self):
        # return self.driver.find_element(By.XPATH, '//input[@name="entry.200710398_day"]')
        return self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[2]/div[2]/div/input[3]')

    def month_field(self):
        # return self.driver.find_element(By.XPATH, '//input[@name = "entry.200710398_month"]')
        return self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[2]/div[2]/div/input[2]')

    def year_field(self):
        # return self.driver.find_element(By.XPATH, '//input[@name="entry.200710398_year"]')
        return self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[2]/div[2]/div/input[1]')

    def empty_date_field(self):
        self.day_field().clear()
        self.month_field().clear()
        self.year_field().clear()

    def date_exception_field(self):
        return self.driver.find_element(By.ID, "i.err.1236342938")

    def name_field(self):
        return self.driver.find_element(By.XPATH, '//input[@aria-label = "Name"]')

    def name_exception_field(self):
        return self.driver.find_element(By.ID, 'i.err.1645109785')

    def clear_name_field(self):
        self.name_field().clear()

    def fill_name_field(self, value):
        self.name_field().send_keys(value)

    def sex_listbox(self):
        return self.driver.find_element(By.XPATH, '//div[contains(@class, "quantumWizMenuPaperselectOptionList)]')

    def select_sex_option(self, option):
        self.sex_listbox().click()
        self.driver.find_element(By.XPATH,'//div[contains(@class, "quantumWizMenuPaperselectOption") and (@data-value=%s)]' % option).click()

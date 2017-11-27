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

    def day_field(self):
        return self.driver.find_element(By.XPATH, '//input[@aria-label = "День місяця"]')

    def month_field(self):
        return self.driver.find_element(By.XPATH, '//input[@aria-label = "Місяць"]')

    def year_field(self):
        return self.driver.find_element(By.XPATH, '//input[@aria-label = "Рік"]')

    def empty_date_field(self):
        self.driver.find_element(By.XPATH, '//input[@aria-label = "День місяця"]').clear()
        self.driver.find_element(By.XPATH, '//input[@aria-label = "Місяць"]').clear()
        self.driver.find_element(By.XPATH,'//input[@aria-label = "Рік"]').clear()

    def date_exception_field(self):
        return self.driver.find_element(By.XPATH, '//*[@id="i.err.1236342938"]')

    def name_field(self):
        return self.driver.find_element(By.XPATH, '//input[@aria-label = "Имя"]')

    def name_exception_field(self):
        return self.driver.find_element(By.ID, 'i.err.1645109785')

    def clear_name_field(self):
        self.driver.find_element(By.XPATH, '//input[@aria-label = "Имя"]').clear()

    def fill_name_field(self, value):
        elem = self.driver.find_element(By.XPATH, '//input[@aria-label = "Имя"]')
        elem.send_keys(value)

    def sex_listbox(self):
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div/div[2]/div[2]/div[4]/div[2]/div[1]')

    def select_sex_option(self, option):
        self.sex_listbox().click()
        self.driver.find_element(By.XPATH,'//div[@data-value="%s"]' % option).click()

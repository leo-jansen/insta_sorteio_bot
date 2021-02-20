from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import platform


class InstagramBot:
  def __init__(self, username, password, link):
      self.username = username
      self.password = password
      self.link = link
      self.driver = InstagramBot.escolher_driver()

  @staticmethod
  def escolher_driver():
    if platform.system() == "Windows":
      web_driver = webdriver.Firefox("../driver/geckodriver-v0.29.0-win64/geckodriver.exe")
    elif platform.system() == "Linux":
      web_driver = webdriver.Firefox("../driver/geckodriver-v0.29.0-linux64/geckodriver")
    return web_driver
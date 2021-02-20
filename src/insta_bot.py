from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import platform
import os

class InstagramBot:
  def __init__(self, username, password, link):
      self.username = username
      self.password = password
      self.link = link
      self.driver = InstagramBot.escolher_driver()

  @staticmethod
  def escolher_driver():
    caminho = os.path.dirname(os.path.realpath(__file__))  
    if platform.system() == "Windows":
      web_driver = webdriver.Firefox(executable_path=caminho+"/driver/geckodriver-v0.29.0-win64/geckodriver.exe")
    elif platform.system() == "Linux":
      web_driver = webdriver.Firefox(executable_path=caminho+"/driver/geckodriver-v0.29.0-linux64/geckodriver")
    return web_driver

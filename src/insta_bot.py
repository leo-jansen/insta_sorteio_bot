from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import platform
import os
import time

class InstagramBot:
  def __init__(self, username, password, sorteio, lista_comentario):
      self.username = username
      self.password = password
      self.sorteio = sorteio
      self.lista_comentario = lista_comentario
      self.instagram = "https://www.instagram.com/"
      self.driver = InstagramBot.escolher_driver()

  @staticmethod
  def escolher_driver():
    caminho = os.path.dirname(os.path.realpath(__file__))  
    if platform.system() == "Windows":
      web_driver = webdriver.Firefox(executable_path=caminho+"/driver/geckodriver-v0.29.0-win64/geckodriver.exe")
    elif platform.system() == "Linux":
      web_driver = webdriver.Firefox(executable_path=caminho+"/driver/geckodriver-v0.29.0-linux64/geckodriver")
    return web_driver

  def login(self):
    driver = self.driver
    driver.get(self.instagram)
    time.sleep(2)
    campo_usuario = driver.find_element_by_xpath("//input[@name='username']")
    campo_usuario.click()
    campo_usuario.clear()
    campo_usuario.send_keys(self.username)
    campo_senha = driver.find_element_by_xpath("//input[@name='password']")
    campo_senha.click()
    campo_senha.clear()
    campo_senha.send_keys(self.password)
    campo_senha.send_keys(Keys.RETURN)


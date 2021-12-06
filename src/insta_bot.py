from selenium import webdriver
from selenium.webdriver.firefox.options import Options
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
      options = Options()
      options.binary_location = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
      web_driver = webdriver.Firefox( options=options, executable_path=caminho+"\driver\geckodriver-v0.30.0-win64\geckodriver.exe")
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

  def comentario(self, numero_de_comentario):
    quantidade = 0
    time.sleep(3)
    self.driver.get(self.sorteio)
    time.sleep(2)
    while quantidade < numero_de_comentario:
      campo_comentario = self.driver.find_element_by_xpath("//textarea[@class='Ypffh']")
      campo_comentario.click()
      campo_comentario = self.driver.find_element_by_xpath("//textarea[@class='Ypffh focus-visible']")
      time.sleep(1)
      campo_comentario.clear()
      campo_comentario.send_keys(self.lista_comentario[0])
      time.sleep(1)
      campo_comentario.send_keys(Keys.RETURN)
      quantidade += 1
      time.sleep(60)
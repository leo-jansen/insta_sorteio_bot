from insta_bot import InstagramBot

usuario = input("Digite seu usuario: ")
senha = input("Digite sua senha: ")
sorteio = input("Digite o link do sorteio: ")
numero_de_comentarios = int(input("Quantos comentarios deseja ter? "))
lista_comentario = []
numero = 0
while numero < numero_de_comentarios:
  comentario = input("Digite o seu comentario: ")
  lista_comentario.append(comentario)
  numero += 1

bot = InstagramBot(usuario, senha, sorteio, lista_comentario)
bot.login()

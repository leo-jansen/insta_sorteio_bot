from src.insta_bot import InstagramBot

usuario = input("Digite seu usuario: ")
senha = input("Digite sua senha: ")
sorteio = input("Digite o link do sorteio: ")
numero_de_comentarios = input("Quantos comentarios deseja ter?")
lista_comentario = []
for comentario in numero_de_comentarios:
  comentario = input("Digite o seu comentario")
  lista_comentario.append(comentario)

bot = InstagramBot(usuario, senha, sorteio, lista_comentario)
bot.login()

from insta_bot import InstagramBot

def main():
  usuario = input("Digite seu usuario: ")
  senha = input("Digite sua senha: ")
  sorteio = input("Digite o link do sorteio: ")
  numero_de_comentarios = int(input("Quantos comentarios deja ter? "))
  lista_comentario = []
  comentario = input("Digite o seu comentario: ")
  lista_comentario.append(comentario)
  bot = InstagramBot(usuario, senha, sorteio, lista_comentario)
  bot.login()
  bot.comentario(numero_de_comentarios)

if __name__ == "__main__":
  main()
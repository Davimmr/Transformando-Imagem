##pip install Pillow

from PIL import Image

img = Image.open("teste.png") #imagem
pretobranco = img.convert("L")
pretobranco.save("testepretobranco.png") #nova imagem preto e branco
pretobranco.show()
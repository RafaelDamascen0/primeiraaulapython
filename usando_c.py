#usar o comando de importação para a bibiloteca criada
import ctypes 

lib = ctypes.CDLL("./mensagem.so")
lib.mensagem()

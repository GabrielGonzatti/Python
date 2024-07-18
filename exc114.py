import urllib
import urllib.request
#IMPORTANDO URLLIB PARA FAZER REQUEST

try:
    site = urllib.request.urlopen('https://www.youtube.com/')
except:
    print('O site não está acessivel no momento')
else:
    print('Acessível!')
    print(site.read())
finally:
    print('Fim do programa')

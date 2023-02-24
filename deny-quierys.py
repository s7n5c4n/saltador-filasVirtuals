import requests

url = "https://www.nike.cl/"
solicitud = requests.get(url)
info = solicitud.json
a = dir(solicitud)  #con esto vemos todos los atributos disponibles
ainfo = solicitud.status_code#aqui podemos ver si los atributos de encuentras estan disponible dependiendo de los valores que me den
acokie = solicitud.cookies
#aqueue = solicitud.queue
print(info)
print("*****************************************************************")
print(a)
print(ainfo)
print(acokie)
#print(aqueue)
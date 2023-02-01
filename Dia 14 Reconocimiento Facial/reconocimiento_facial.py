import cv2
import face_recognition as fr
from pathlib import Path

# Cargar imagenes
url_base = Path('C:\programacion\Clases_Python\Dia 14 Reconocimiento Facial')
foto_control = fr.load_image_file(Path(url_base, 'FotoA.jpg'))
foto_prueba = fr.load_image_file(Path(url_base, 'FotoB.jpg'))

# Transformar imagenes en RGB
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)


# Localizar Cara Control
lugar_cara_A = fr.face_locations(foto_control)[0]
cara_codificada_a = fr.face_encodings(foto_control)[0]


# Localizar Cara prueba
lugar_cara_B = fr.face_locations(foto_prueba)[0]
cara_codificada_b = fr.face_encodings(foto_prueba)[0]

# Mostrar Rectangulos
cv2.rectangle(foto_control, (lugar_cara_A[3], lugar_cara_A[0]), (lugar_cara_A[1], lugar_cara_A[2]), (0,255,0), 2)
cv2.rectangle(foto_prueba, (lugar_cara_B[3], lugar_cara_B[0]), (lugar_cara_B[1], lugar_cara_B[2]), (0,255,0), 2)

# Realizar Comparacion True o False
resultado = fr.compare_faces([cara_codificada_a], cara_codificada_b)

# Medida de la distancia de diferencia
distancia = fr.face_distance([cara_codificada_a], cara_codificada_b)

# Mostrar resultado
cv2.putText(foto_prueba, f'{resultado} {distancia.round(2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)

# Mostrar Imagenes
cv2.imshow('Foto Control', foto_control)
cv2.imshow('Foto Prueba', foto_prueba)

# Mantener el Programa abierto
cv2.waitKey(0)

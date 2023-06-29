import io
import os
import requests
import base64
from google.cloud import vision
import openai

# Configurar las credenciales de Google Cloud Vision
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path-to/vision-api-service-account.json"

# Configurar las credenciales de OpenAI
openai.api_key = "sk-<openai-key>"

def obtener_descripcion_imagen(imagen):
    # Pasar la imagen a Google Cloud Vision API
    client = vision.ImageAnnotatorClient()
    
    with io.open(imagen, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.label_detection(image=image)
    labels = response.label_annotations
    
    # Crear una lista de descripciones de las etiquetas
    descripciones = [label.description for label in labels]
    
    return descripciones

def generar_frase_gpt3(descripciones):
    # Concatenar las descripciones en un solo string
    texto = ' '.join(descripciones)
    texto = '******** '+texto+' ********'
    
    # Configurar el modelo y los parámetros de la solicitud a OpenAI
    modelo = "gpt-3.5-turbo"
    parametros = {
        "messages": [{"role": "system", "content": "Translate from `EN` to `ES` each words from above, delimited by ********. And then use the new output to generate a phrase in `ES` "},
                     {"role": "user", "content": texto}],
        "max_tokens": 300,  # Número máximo de tokens en la respuesta
        "temperature": 0.7,  # Controla la aleatoriedad de las respuestas (0.0 a 1.0)
        "n": 1  # Número de respuestas a generar
    }
    
    # Generar la frase utilizando OpenAI GPT-3.5
    respuesta = openai.ChatCompletion.create(model=modelo, **parametros)
    frase_generada = respuesta.choices[0].message.content.strip()
    
    return frase_generada


# Ruta de la imagen que deseas procesar
ruta_imagen = "path-to/demo.jpeg"

# Obtener descripción de la imagen utilizando Google Cloud Vision API
descripciones = obtener_descripcion_imagen(ruta_imagen)

# Generar una frase utilizando OpenAI GPT-3.5
frase_generada = generar_frase_gpt3(descripciones)

# Imprimir la frase generada
print(frase_generada)

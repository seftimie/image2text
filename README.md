[![Image2Text](https://raw.githubusercontent.com/seftimie/image2text/main/image2text.jpg)](#)

# image2text
Combine and use Google Cloud Vision API and the OpenAI GPT-3.5 API to analyze images and generate natural language descriptions

# Setup:
- enable google cloud vision api;
- generate service account;
- generate openai api key;
- replace lines 9, 12 and 53 with your paths & keys;

```
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path-to/vision-api-service-account.json"
openai.api_key = "sk-<openai-key>"
ruta_imagen = "path-to/demo.jpeg"
```

# Dependencies:
``` pip install openai ```

# Test app:
``` python app.py ```

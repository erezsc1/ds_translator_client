
# MarianMT Service CLIENT
Machine Translation RESTful API service. Based on Helsinki-NLP repository, and supports the following languages:
- arb <--> eng
- arb --> fr
- arb <--> heb
- arb <--> rus
- arb <--> spa
- arb <--> tur
- de <--> heb
- ell --> arb
- eng --> heb
- es --> heb
- fi <--> heb
- fr --> heb
- fra --> arb
- heb <--> sv
- ita --> arb
- jpn --> arb

Process finished with exit code 0


All models are stored in /trained_models/
New models can be saved in that directory, and update translator_config.json accordingly.

## Installation
```bash
git clone gitlab.com/miriam_translator_repository.git
$ pip3 wheel --wheel-dir=/tmp/translator_client translator_client
$ pip3 install --no-index --find-links=/tmp/translator_client translator_client
```

## Examples

### Client Class
```python
from translation_cliet import TranslatorClient


if __name__ == '__main__':
    service_url = "http://0.0.0.0:5000"
    tc = TranslatorClient("heb", "arb", service_url)
    query1 = "שלום לכם, ילדים וילדות"
    query2 = [
        "שלום לכם, ילדים וילדות",
        "אני יובל המבולבל"
    ]
    tc.translate(query1)  # [مرحباً أيها الأطفال والبنات]
    tc.translate(query2)  # ['مرحباً أيها الأطفال والبنات', 'أنا يوبيل مشوّش']

```

## Docker
### build: 
```bash
sudo docker build . -t translation_image
```
### run:
with gpu:
```bash
sudo nvidia-docker run -p 5000:80 translation_image
```
without gpu:
```bash
sudo docker run -p 5000:80 translation_image
```
access via ```localhost:5000/docs```

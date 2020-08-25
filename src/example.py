from translator_client import TranslatorClient


if __name__ == '__main__':
    service_url = "http://0.0.0.0:5000"
    tc = TranslatorClient("heb", "arb", service_url)
    query1 = "שלום לכם, ילדים וילדות"
    query2 = [
        "שלום לכם, ילדים וילדות",
        "אני יובל המבולבל"
    ]
    print(tc.translate(query1))  # مرحباً أيها الأطفال والبنات
    print(tc.translate(query2))  # ['مرحباً أيها الأطفال والبنات', '"أنا "يوبيل بوبلاف']

    supported_langs = tc.get_supported_translations()
    [print(lang) for lang in supported_langs]

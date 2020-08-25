import requests


SUCCESS_CODE = 200

SPECIAL_CASE_TGT_MAP = {
    "he": "heb",
    "ara": "arb",
    "ar": "arb",
    "en": "eng"
}


class TranslatorClient():
    def __init__(self, src_lang, tgt_lang, service_url, special_tokens=None):
        self.src_lang = src_lang
        self.tgt_lang = tgt_lang
        self.service_url = service_url
        self.special_tokens = special_tokens

    def get_supported_translations(self):
        request_url = f"{self.service_url}/"
        request = {
            "content-type": "application/json"
        }
        models = requests.get(request_url, params=request).json()["models"]
        supported_translations = []

        lang_mapping_dict = {}

        for model in models:
            src_lang = model.split("_")[-2]
            tgt_lang = model.split("_")[-1]
            src_lang_tok = SPECIAL_CASE_TGT_MAP.get(src_lang, src_lang)
            tgt_lang_tok = SPECIAL_CASE_TGT_MAP.get(tgt_lang, tgt_lang)
            lang_dict_key = f"{src_lang_tok}_{tgt_lang_tok}"
            lang_mapping_dict[lang_dict_key] = True

        for item in lang_mapping_dict:
            lang_1 = item.split("_")[0]
            lang_2 = item.split("_")[1]
            rev_trans = f"{lang_2}_{lang_1}"
            org_trans = f"{lang_1}_{lang_2}"

            if rev_trans in lang_mapping_dict and org_trans in lang_mapping_dict:
                if f"{lang_1} <--> {lang_2}" in supported_translations or f"{lang_2} <--> {lang_1}" in supported_translations:
                    continue
                else:
                    supported_translations.append(f"{lang_1} <--> {lang_2}")
            else:
                supported_translations.append(f"{lang_1} --> {lang_2}")
        return supported_translations

    def translate(self, query):
        '''
        :param query: list[str], str
        :return: returns a list or a string
        '''
        request = {
            "source_lang": self.src_lang,
            "target_lang": self.tgt_lang,
            "content-type": "application/json",
            "special-tokens": self.special_tokens
        }

        request_url = f"{self.service_url}/translate/"
        request["data_list"] = query

        response : requests.Response = requests.get(
            request_url,
            params=request
        )

        if response.status_code == SUCCESS_CODE:
            return response.json()
        return f"error - {response.status_code} code"



import os
from deepl import Translator as deepl_Translator
from translators import translate_text as other_web_Translator
from .translation_languages import translation_lang
from .translation_utils import ctranslate2_weights

import ctranslate2
import transformers

# Translator
class Translator():
    def __init__(self):
        self.deepl_client = None
        self.ctranslate2_translator = None
        self.ctranslate2_tokenizer = None
        self.is_loaded_ctranslate2_model = False

    def authenticationDeepLAuthKey(self, authkey):
        result = True
        try:
            self.deepl_client = deepl_Translator(authkey)
            self.deepl_client.translate_text(" ", target_lang="EN-US")
        except Exception:
            self.deepl_client = None
            result = False
        return result

    def changeCTranslate2Model(self, path, model_type):
        self.is_loaded_ctranslate2_model = False
        directory_name = ctranslate2_weights[model_type]["directory_name"]
        tokenizer = ctranslate2_weights[model_type]["tokenizer"]
        weight_path = os.path.join(path, "weights", "ctranslate2", directory_name)
        tokenizer_path = os.path.join(path, "weights", "ctranslate2", directory_name, "tokenizer")
        self.ctranslate2_translator = ctranslate2.Translator(
            weight_path,
            device="cpu",
            device_index=0,
            compute_type="int8",
            inter_threads=1,
            intra_threads=4
        )
        try:
            self.ctranslate2_tokenizer = transformers.AutoTokenizer.from_pretrained(tokenizer, cache_dir=tokenizer_path)
        except Exception as e:
            print("Error: changeCTranslate2Model()", e)
            tokenizer_path = os.path.join("./weights", "ctranslate2", directory_name, "tokenizer")
            self.ctranslate2_tokenizer = transformers.AutoTokenizer.from_pretrained(tokenizer, cache_dir=tokenizer_path)
        self.is_loaded_ctranslate2_model = True

    def isLoadedCTranslate2Model(self):
        return self.is_loaded_ctranslate2_model

    def translateCTranslate2(self, message, source_language, target_language):
        result = False
        if self.is_loaded_ctranslate2_model is True:
            try:
                self.ctranslate2_tokenizer.src_lang = source_language
                source = self.ctranslate2_tokenizer.convert_ids_to_tokens(self.ctranslate2_tokenizer.encode(message))
                target_prefix = [self.ctranslate2_tokenizer.lang_code_to_token[target_language]]
                results = self.ctranslate2_translator.translate_batch([source], target_prefix=[target_prefix])
                target = results[0].hypotheses[0][1:]
                result = self.ctranslate2_tokenizer.decode(self.ctranslate2_tokenizer.convert_tokens_to_ids(target))
            except Exception:
                pass
        return result

    @staticmethod
    def getLanguageCode(translator_name, target_country, source_language, target_language):
        match translator_name:
            case "DeepL_API":
                if target_language == "English":
                    if target_country in ["United States", "Canada", "Philippines"]:
                        target_language = "English American"
                    else:
                        target_language = "English British"
                elif target_language == "Portuguese":
                    if target_country in ["Portugal"]:
                        target_language = "Portuguese European"
                    else:
                        target_language = "Portuguese Brazilian"
            case _:
                pass
        source_language=translation_lang[translator_name]["source"][source_language]
        target_language=translation_lang[translator_name]["target"][target_language]
        return source_language, target_language

    def translate(self, translator_name, source_language, target_language, target_country, message):
        try:
            result = ""
            source_language, target_language = self.getLanguageCode(translator_name, target_country, source_language, target_language)
            match translator_name:
                case "DeepL":
                    result = other_web_Translator(
                        query_text=message,
                        translator="deepl",
                        from_language=source_language,
                        to_language=target_language,
                        )
                case "DeepL_API":
                    if self.deepl_client is None:
                        result = False
                    else:
                        result = self.deepl_client.translate_text(
                            message,
                            source_lang=source_language,
                            target_lang=target_language,
                            ).text
                case "Google":
                    result = other_web_Translator(
                        query_text=message,
                        translator="google",
                        from_language=source_language,
                        to_language=target_language,
                        )
                case "Bing":
                    result = other_web_Translator(
                        query_text=message,
                        translator="bing",
                        from_language=source_language,
                        to_language=target_language,
                        )
                case "Papago":
                    result = other_web_Translator(
                        query_text=message,
                        translator="papago",
                        from_language=source_language,
                        to_language=target_language,
                        )
                case "CTranslate2":
                    result = self.translateCTranslate2(
                        message=message,
                        source_language=source_language,
                        target_language=target_language,
                        )
        except Exception:
            import traceback
            with open('error.log', 'a') as f:
                traceback.print_exc(file=f)
            result = False
        return result
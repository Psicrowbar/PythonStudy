import json
import requests
from config import keys
class ConvertionException(Exception):
    pass


class CryptoConverter():
    @staticmethod
    def convertcurrency(quote: str, base: str, amount: str, params:int):
        print(params)
        if quote == base:
            raise ConvertionException('Валюта из которой вы переводите и в которую вы переводите должны отличаться.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось получить валюту {quote}.')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось получить валюту {base}.')
        try:
            amount_float = float(amount)
        except ValueError:
            raise ConvertionException('Количество валюты должно быть числом.')
        r = requests.get(f"https://v6.exchangerate-api.com/v6/66a649e9688abcd3128a7a30/pair/{quote_ticker}/{base_ticker}")
        #r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        totalbase = round(json.loads(r.content)['conversion_rate'],3)

        return totalbase

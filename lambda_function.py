import json
import urllib3
from datetime import datetime, timezone
from constants import (
    API_URL, API_KEY, DEFAULT_DIFFERENCE_MINUTES, STATUS_CODE_SUCCESS,
    STATUS_CODE_ERROR, MESSAGE_API_REQUEST_FAILED, MESSAGE_FETCH_API_ERROR,
    HEADER_API_KEY, PROP_AMOUNT, PROP_BASE_CURRENCY, PROP_QUOTE_CURRENCY,
    PROP_EXPIRATION_TS, PROP_SEND_AMOUNT, PROP_PERCENTAGE_FEE, PROP_FIXED_FEE,
    PROP_EXCHANGE_RATE, PROP_BALAM_RATE, PROP_QUOTE_AMOUNT, PROP_RECEIVE_AMOUNT,
    PROP_TIME_UNTIL_EXPIRATION_MINUTES
)

def lambda_handler(event, context):
    try:
        amount = event.get(PROP_AMOUNT)
        base_currency = event.get(PROP_BASE_CURRENCY)
        quote_currency = event.get(PROP_QUOTE_CURRENCY)

        api_data = fetch_api_response(amount, base_currency, quote_currency)

        response_data = map_response_data(api_data, amount, base_currency, quote_currency)

        return {
            "statusCode": STATUS_CODE_SUCCESS,
            "body": response_data
        }
    except Exception as e:
        print(f"Request failed: {e}")
        return {
            "statusCode": STATUS_CODE_ERROR,
            "body": {
                "message": MESSAGE_API_REQUEST_FAILED,
                "error": str(e)
            }
        }

def fetch_api_response(amount, base_currency, quote_currency):
    http = urllib3.PoolManager()
    url = f"{API_URL}?amount={amount}&base_currency={base_currency}&quote_currency={quote_currency}"
    headers = {HEADER_API_KEY: API_KEY}
    try:
        response = http.request('GET', url, headers=headers)
        response_data = json.loads(response.data.decode('utf-8'))
        return response_data.get("data", {})
    except Exception as e:
        print(f"{MESSAGE_FETCH_API_ERROR}: {e}")
        return {}

def map_response_data(data, amount, base_currency, quote_currency):
    expiration_ts = data.get(PROP_EXPIRATION_TS)
    difference_minutes = DEFAULT_DIFFERENCE_MINUTES
    return {
        PROP_SEND_AMOUNT: data.get("base_amount", amount),
        PROP_BASE_CURRENCY: data.get(PROP_BASE_CURRENCY, base_currency),
        PROP_PERCENTAGE_FEE: data.get("pct_fee") * 100 if data.get("pct_fee") else None,
        PROP_FIXED_FEE: data.get("fixed_fee"),
        PROP_EXCHANGE_RATE: data.get("rate"),
        PROP_BALAM_RATE: data.get("balam_rate"),
        PROP_QUOTE_CURRENCY: data.get(PROP_QUOTE_CURRENCY, quote_currency),
        PROP_RECEIVE_AMOUNT: round(data.get(PROP_QUOTE_AMOUNT, 0), 2),
        PROP_EXPIRATION_TS: expiration_ts,
        PROP_TIME_UNTIL_EXPIRATION_MINUTES: difference_minutes
    }

# constants.py

API_URL = "https://api.balampay.com/sandbox/quotes/"  
API_KEY = "rfa3aMb7Rl6TP09jcG6D23E4yZvmp04s9aw9E4vA"  

DEFAULT_DIFFERENCE_MINUTES = 10

STATUS_CODE_SUCCESS = 200
STATUS_CODE_ERROR = 500
MESSAGE_API_REQUEST_FAILED = "API request failed"
MESSAGE_FETCH_API_ERROR = "Error fetching API response"
HEADER_API_KEY = "x-api-key"

PROP_AMOUNT = "amount"
PROP_BASE_CURRENCY = "base_currency"
PROP_QUOTE_CURRENCY = "quote_currency"
PROP_EXPIRATION_TS = "expiration_ts"
PROP_SEND_AMOUNT = "send_amount"
PROP_PERCENTAGE_FEE = "percentage_fee"
PROP_FIXED_FEE = "fixed_fee"
PROP_EXCHANGE_RATE = "exchange_rate"
PROP_BALAM_RATE = "balam_rate"
PROP_QUOTE_AMOUNT = "quote_amount"
PROP_RECEIVE_AMOUNT = "receive_amount"
PROP_TIME_UNTIL_EXPIRATION_MINUTES = "time_until_expiration_minutes"

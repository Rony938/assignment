mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Russia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'UK'},
        {'name': 'Huwei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    "exchange_rate": 107.50
}

for phone_data in mobile_data['data']:
    phone_name = phone_data['name']
    phone_price_usd = float(phone_data['price'].split()[0])  # Extracting the numerical value from 'price'
    phone_made = phone_data['made']

    exchange_rate = mobile_data['exchange_rate']
    phone_price_bdt = phone_price_usd * exchange_rate

    sentence = f"{phone_name} is made in {phone_made}. The price is {phone_price_usd} USD which is almost equal to {phone_price_bdt:.2f} BDT."
    print(sentence)
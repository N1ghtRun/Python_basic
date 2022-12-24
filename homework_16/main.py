import exchange_rate

exchange_object = exchange_rate.ExchangeRate('22', '04', '2020')
exchange_object.set_url()
exchange_object.get_json()
exchange_object.save_data()

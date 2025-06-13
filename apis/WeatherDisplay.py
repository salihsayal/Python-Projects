def displayWeather(response):
    address = response["address"]
    conditions = response["currentConditions"]["conditions"]
    temperature = response["currentConditions"]["temp"]

    return f"Current weather in {address}:\n{conditions}, {temperature} °C"

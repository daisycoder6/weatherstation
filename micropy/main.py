import network
import time
import urequests
import config
import dht
import datetime


def gen_tstamp():
    """
    Generates a current timestamp
    """
    i = datetime.datetime.now()
    tstamp = i.strftime('%Y_%m_%d_%H_%M_%S')
    return(tstamp)

def connect_wifi():
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(False)
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('Connecting to WiFi...')
        sta_if.active(True)
        sta_if.connect(config.WIFI_SSID, config.WIFI_PASSWORD)
        while not sta_if.isconnected():
            time.sleep(1)
    print('Network config:', sta_if.ifconfig())

def get_temperature_and_humidity():
    dht22 = dht.DHT22(machine.Pin(4))
    dht22.measure()
    temperature = dht22.temperature()
    humidity = dht22.humidity()
    # if config.FAHRENHEIT:
    #     temperature = temperature * 9 / 5 + 32
    return temperature, humidity


def deepsleep():
    print('Going into deepsleep for {seconds} seconds...'.format(
        seconds=10))
    rtc = machine.RTC()
    rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)
    rtc.alarm(rtc.ALARM0, 10 * 1000)
    machine.deepsleep()


def log_data(temperature, humidity):

    # http://localhost:8080/?&temp=5&humid=43.4

    # WEBHOOK_URL = 'http://fac4a10c.ngrok.io?&field1={temperature}&field2={humidity}'
    #WEBHOOK_URL = 'http://fac4a10c.ngrok.io/?field1={temperature}&field2={humidity}'
    print('Invoking log webhook')
    url = config.WEBHOOK_URL.format(temperature=temperature,
                                    humidity=humidity)

    print(url)
    response = urequests.get(url=url)
    # response = get(url, payload)
    print(response)
    if response.status_code < 400:
        print('Webhook invoked')
    else:
        print('Webhook failed')
        raise RuntimeError('Webhook failed')
    response.close()


def run():
    connect_wifi()
    temperature, humidity = get_temperature_and_humidity()
    print(temperature)
    print(humidity)
    log_data(temperature, humidity)
    deepsleep()


run()
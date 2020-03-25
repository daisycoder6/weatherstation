import network
import time
import urequests
import config
import dht
import utime

def gen_timestamp():
    """
    Get current time from RTC
    """

    year, month, mday, hour, minute, second, weekday, yearday = utime.localtime()
    component = (str(year), str(month), str(mday), str(hour), str(minute), str(second))

    timestamp = "_".join(component)

    return timestamp

def connect_wifi():
    """
    Connect to WIFI
    Credential supplied fromconfig.py which is copied to device
    """
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
    """
    Invoke measurement and readback of DHT22
    """

    dht22 = dht.DHT22(machine.Pin(4))
    dht22.measure()
    temperature = dht22.temperature()
    humidity = dht22.humidity()

    return temperature, humidity


def deepsleep():
    """
    Sends micro into deepsleep for specified time
    """

    sleeptime = config.SLEEP_TIME

    print('Going into deepsleep for {seconds} seconds...'.format(
        seconds=sleeptime))
    rtc = machine.RTC()
    rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)
    rtc.alarm(rtc.ALARM0, sleeptime * 1000)
    machine.deepsleep()


def log_data(temperature, humidity):
    """
    Send data to web server
    """

    timestamp = gen_timestamp()
    print('Invoking log webhook')
    url = config.WEBHOOK_URL.format(id = config.SENSOR_ID,
                                    tstamp = timestamp,
                                    temperature=temperature,
                                    humidity=humidity)

    response = urequests.get(url=url)
    print(response)
    if response.status_code < 400:
        print('Logging succeeded')
    else:
        print('Logging failed')
        #Want sensor to keep running if it can't connect
        #raise RuntimeError('Webhook failed')
    response.close()


def run():
    connect_wifi()
    temperature, humidity = get_temperature_and_humidity()
    print(temperature)
    print(humidity)
    log_data(temperature, humidity)
    deepsleep()


run()
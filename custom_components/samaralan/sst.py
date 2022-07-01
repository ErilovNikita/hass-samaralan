import requests
import json
import re
import logging
# from homeassistant.core import HomeAssistant

API_URL = "https://cabinet.samaralan.ru/user-services/internet/index.php"

class SST:

    def pull_data(self):
        r = requests.Session().get(API_URL)
        json_device = json.loads('''{}''')

        json_device.update({'ip' : re.findall(r'Вход с IP: (.*)</div>', r.text)[0].replace(' ', '')})
        json_device.update({'rate' : re.findall(r'<b>(.*)</b>', r.text)[2] })
        json_device.update({'upload' : re.findall(r'Отправленно - (.*) МБайт]', r.text)[0].replace('[','')})
        json_device.update({'download' : re.findall(r'Объём трафика: Получено - (.*) МБайт],', r.text)[0].replace('[','')})
        json_device.update({'balance' : re.findall(r'<h3>В вашем распоряжении: (.*) руб. </h3>', r.text)[0]})
        json_device.update({'date' : re.findall(r'Период действия с (.*)</td><td>', r.text)[0].split(' по ')[1]})

        self.devices.append(samaraLan(json.dumps(json_device), self))

class samaraLan:
    def __init__(self, moduleDescription: json, sst: SST):
        self._sst = sst
        config = json.loads(moduleDescription["parsed_configuration"])

        self.ip = config["ip"]
        self.rate = config["rate"]
        self.upload = config["upload"]
        self.download = config["download"]
        self.balance = config["balance"]
        self.date = config["date"]

    @property
    def get_ip(self) -> str:
            return self.ip

    @property
    def get_rate(self) -> str:
            return self.rate

    @property
    def get_upload_data(self) -> int:
            return self.upload

    @property
    def get_download_data(self) -> int:
            return self.download

    @property
    def get_date(self) -> str:
            return self.date
        
    @property
    def get_balance(self) -> int:
            return self.balance
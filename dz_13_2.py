from abc import ABC, abstractmethod


class SmartDevice(ABC):
    def __init__(self, device_name):
        self.device_name = device_name
        self._is_on = False

    def turn_on(self):
        self._is_on = True

    def turn_off(self):
        self._is_on = False

    @property
    @abstractmethod
    def status_report(self):
        pass


class SmartLight(SmartDevice):
    def __init__(self, device_name, brightness=50):
        super().__init__(device_name)
        self.brightness = brightness

    def set_brightness(self, brightness):
        if 0 <= brightness <= 100:
            self.brightness = brightness
        else:
            raise ValueError('Яркость должна быть от 0 до 100')

    @property
    def status_report(self):
        state = 'включена' if self._is_on else 'выключена'
        return f'{self.device_name}: {state}, яркость {self.brightness}%'


class SmartThermostat(SmartDevice):
    def __init__(self, device_name, target_temp=22):
        super().__init__(device_name)
        self.target_temp = target_temp

    @property
    def status_report(self):
        state = 'включен' if self._is_on else 'выключен'
        return f'{self.device_name}: {state}, температура {self.target_temp}°C'


class SmartLock(SmartDevice):
    def turn_on(self):
        self._is_on = True
        print(f'{self.device_name}: дверь заблокирована')

    def turn_off(self):
        self._is_on = False
        print(f'{self.device_name}: дверь разблокирована')

    @property
    def status_report(self):
        state = 'заблокирован' if self._is_on else 'разблокирован'
        return f'{self.device_name}: замок {state}'


class SmartHomeHub:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def turn_all_off(self):
        for device in self.devices:
            device.turn_off()


light = SmartLight('Лампа в зале')
light.turn_on()
light.set_brightness(80)
print(light.status_report)

thermostat = SmartThermostat('Термостат', 24)
thermostat.turn_on()
print(thermostat.status_report)

lock = SmartLock('Входной замок')
lock.turn_on()
print(lock.status_report)

hub = SmartHomeHub()
hub.add_device(light)
hub.add_device(thermostat)
hub.add_device(lock)

hub.turn_all_off()

print(light.status_report)
print(thermostat.status_report)
print(lock.status_report)

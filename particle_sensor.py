import sys
import json
from time import sleep
from sps30 import SPS30
def measureParticle():
    # print(f"Firmware version: {pm_sensor.firmware_version()}")
    # print(f"Product type: {pm_sensor.product_type()}")
    # print(f"Serial number: {pm_sensor.serial_number()}")
    # print(f"Status register: {pm_sensor.read_status_register()}")
    # print(
    #     f"Auto cleaning interval: {pm_sensor.read_auto_cleaning_interval()}s")
    # print(f"Set auto cleaning interval: {pm_sensor.write_auto_cleaning_interval_days(2)}s")
    pm_sensor = SPS30()
    pm_sensor.start_measurement()
    data = pm_sensor.get_measurement()
    while (not data):
        sleep(0.1)
        data = pm_sensor.get_measurement()
    pm25_count = data['sensor_data']['mass_density']['pm2.5']
    pm_sensor.stop_measurement()
    return(pm25_count)
        
if __name__ == "__main__":
    data = measureParticle()
    print(data)
   
    



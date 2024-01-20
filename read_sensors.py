import argparse
import json
# from sense_emu import SenseHat
from sense_hat import SenseHat
import math


sense = SenseHat()

parser = argparse.ArgumentParser(description='SenseHat sensors CLI client.')

# RPY values
parser.add_argument('-r', action='store', type=bool, default=False, help='Roll')
parser.add_argument('-p', action='store', type=bool, default=False, help='Pitch')
parser.add_argument('-y', action='store', type=bool, default=False, help='Yaw')
parser.add_argument('-u', action='store', type=str,choices=['rad', 'deg'], default='deg', help='Unit, either rad or deg')

# Sensors
parser.add_argument('-P', action='store', type=str, choices=['hPa', 'mmHg'], help='Pressure unit, either hPa or mmHg')
parser.add_argument('-T', action='store', type=str, choices=['C', 'F'], help='Temperature unit, either C or F')
parser.add_argument('-H', action='store', type=str, choices=['%', 'num'], help='Humidity unit, either percent or numerical')

args = parser.parse_args()

roll = (int)(args.r)
pitch = (int)(args.p)
yaw = (int)(args.y)
u = (str)(args.u)

P_unit = (str)(args.P)
T_unit = (str)(args.T)
H_unit = (str)(args.H)

results = {}
results['sensors'] = ['LPS25h', 'LSM9DS1', 'HTS221']

if roll:
    roll_value = sense.get_orientation()['roll']
    if u == 'rad': roll_value *= math.pi/180.0
    results['roll'] = roll_value

if pitch:
    pitch_value = sense.get_orientation()['pitch']
    if u == 'rad': pitch_value *= math.pi/180.0
    results['pitch'] = pitch_value

if yaw:
    yaw_value = sense.get_orientation()['yaw']
    if u == 'rad': yaw_value *= math.pi/180.0
    results['yaw'] = yaw_value

if u != 'None':
    results['rpyUnit'] = u

if P_unit != 'None':
    results['pressureUnit'] = P_unit
    pressure = sense.get_pressure()
    if P_unit == 'mmHg': pressure *= 0.75
    results['pressure'] = pressure

if T_unit != 'None':
    results['temperatureUnit'] = T_unit
    temperature = sense.get_temperature()
    if T_unit == 'F': temperature = temperature * 1.8 + 32.0
    results['temperature'] = temperature

if H_unit != 'None':
    results['humidityUnit'] = H_unit
    humidity = sense.get_humidity()
    if H_unit == 'num': humidity /= 100.0
    results['humidity'] = humidity

# mock
# results['roll'] = 40
# results['pitch'] = 90
# results['yaw'] = 20
# results['rpyUnit'] = 'deg'
# results['pressure'] = 1023
# results['temperature'] = 28
# results['humidity'] = 50
# results['pressureUnit'] = "hPa"
# results['temperatureUnit'] = "C"
# results['humidityUnit'] = "%"

print(json.dumps(results))

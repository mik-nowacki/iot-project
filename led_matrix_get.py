import json
from sense_emu import SenseHat

sense = SenseHat()
result = {}
result['ledmatrix'] = sense.get_pixels() 

print(json.dumps(result))
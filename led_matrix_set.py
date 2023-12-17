# @author  Dominik Luczak
import argparse
from json import dumps
from sense_hat import SenseHat

class args:
    this.x = 0
    this.y = 0
    this.R = 0
    this.G = 0
    this.B = 0
    this.C = 0

def main():
    sense = SenseHat()

    parser = argparse.ArgumentParser(description='Set one pixel of the Sense HAT 8x8 LED matrix.')
    parser.add_argument('-x', action='store', type=int, choices=range(0,8), default=0, help='Position x of LED')
    parser.add_argument('-y', action='store', type=int, choices=range(0,8), default=0, help='Position y of LED')
    parser.add_argument('-R', action='store', type=int, default=0, metavar='Red', help='Red channel intensity 0-255')
    parser.add_argument('-G', action='store', type=int, default=0, metavar='Green', help='Green channel intensity 0-255')
    parser.add_argument('-B', action='store', type=int, default=0, metavar='Blue', help='Blue channel intensity 0-255')
    parser.add_argument('-C', action='store_true', help='Clear ledmatrix')

    parse_args = parser.parse_args()
    args = args()
    results = {}
    args.x = int(parse_args.x)
    args.y = int(parse_args.y)
    args.R = int(parse_args.R)
    args.G = int(parse_args.G)
    args.B = int(parse_args.B)
    args.C = int(parse_args.C)

    if C:
        sense.clear()
        results['clear'] = True

    if R>255 or R < 0:
        R=0
    if G>255 or G < 0:
        G=0
    if B>255 or B < 0:
        B=0	
    color = (R,G,B)

    results['position'] = {}
    results['position']['x'] = x
    results['position']['y'] = y
    results['color'] = color

    sense.set_pixel(x, y, color)

    print(dumps(results))

if __name__ == "__main__":
    main()
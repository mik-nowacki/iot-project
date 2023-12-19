# @author  Dominik Luczak
import argparse
from json import dumps
from sense_hat import SenseHat


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
    x = int(parse_args.x)
    y = int(parse_args.y)
    R = int(parse_args.R)
    G = int(parse_args.G)
    B = int(parse_args.B)
    C = int(parse_args.C)

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
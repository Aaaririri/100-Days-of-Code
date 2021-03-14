"""
simple way to calculate how many cans of paint you need to buy
"""
import math
def paint_calc(height, width, cover):
    how_many = math.ceil((height * width)/cover)
    print(f"How many cans of paint you need: {how_many}")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

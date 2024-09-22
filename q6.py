"""
Write a class called Converter. The user will pass a length and 
a unit when declaring an object from the class—for example, 
c = Converter(9,'inches'). The possible units are inches, feet, 
yards, miles, kilometers, meters, centimeters, and millimeters. 
For each of these units there should be a method that returns 
the length converted into those units. 
For example, using the Converter object created above, 
the user could call c.feet() and should get 0.75 as the result.
"""

from typing import Callable, Literal, Union


class Converter:
    units = ["inches", "feet", "yards", "miles", "kilometers", "meters", "centimeters", "millimeters"]
    converter = [2.54, 30.48, 91.44, 160900, 100000, 100, 1, 0.1]
    proper_units = Literal["inches", "feet", "yards", "miles", "kilometers", "meters", "centimeters", "millimeters"]

    def __init__(self, length: int | float, unit: proper_units):
        self.length = length
        self.unit = unit
        self.converted_cm = self.length * Converter.converter[Converter.units.index(self.unit)]

    def __getattr__(self, name: proper_units) -> Callable[..., Union[int, float]]:
        def convert():
            if self.unit == name:
                return self.length
            else:
                divisor = Converter.converter[Converter.units.index(name)]
                return self.converted_cm / divisor
            
        return convert

# Test usage
val = Converter(9, 'inches')
print(val.feet())
print(val.yards())
print(val.millimeters())
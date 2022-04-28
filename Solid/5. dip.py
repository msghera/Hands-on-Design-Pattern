from abc import ABC, abstractmethod

class LightBulb:
    def turn_on(self) -> None:
        print('Lightbulb is on.')        

    def turn_off(self) -> None:
        print('Lightbulb is off.')        


class Switch:
    def __init__(self, light_bulb: LightBulb) -> None:
        self.light_bulb = light_bulb
        self.on = False


    def press(self) -> None:
        if self.on:
            self.on = False
            self.light_bulb.turn_off()
        else:
            self.on = True
            self.light_bulb.turn_on()
    

light_bulb = LightBulb()
switch = Switch(light_bulb)
switch.press()
switch.press()


class Fan:
    def turn_on(self) -> None:
        print('Fan is on.')        

    def turn_off(self) -> None:
        print('Fan is off.')        

fan = Fan()
switch1 = Switch(fan)
switch1.press()
switch1.press()


# class Switchable:
#     def turn_on(self) -> None:
#         pass   

#     def turn_off(self) -> None:
#         pass     


# class LightBulb(Switchable):
#     def turn_on(self) -> None:
#         print('Lightbulb is on.')        

#     def turn_off(self) -> None:
#         print('Lightbulb is off.')        


# class Switch:
#     def __init__(self, item: Switchable) -> None:
#         self.item = item
#         self.on = False


#     def press(self) -> None:
#         if self.on:
#             self.on = False
#             self.item.turn_off()
#         else:
#             self.on = True
#             self.item.turn_on()
    

# light_bulb = LightBulb()
# switch = Switch(light_bulb)
# switch.press()
# switch.press()

# class Fan(Switchable):
#     def turn_on(self) -> None:
#         print('Fan is on.')        

#     def turn_off(self) -> None:
#         print('Fan is off.')        

# fan = Fan()
# switch1 = Switch(fan)
# switch1.press()
# switch1.press()
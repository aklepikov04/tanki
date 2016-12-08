#start'
import turtle
import vehicle

#variables
mic=vehicle.vehicle()
mic.tur.color("red")
mic.set_handlers("w", "s", "a", "d")


# variable2
lol = vehicle.vehicle()
lol.set_handlers("Up", "Down", "Left", "Right")
lol.color("red")

print(lol.color_finder)
if lol.tur.pos() - mic.tur.pos() <= (5,5):
     lol.color_finder += 1
if lol.color_finder % 2 == 1:
     mic.color("red")
     lol.color("black")
print(lol.color_finder)

lol.run
mic.run

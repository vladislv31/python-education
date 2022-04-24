from transport import Transport, Car, Bicycle, QuadBike, Motorcycle


car = Car.black('BMW x5 3.0d', 'BMW', 184, 2926)

car.turn_on()
car.lights_on()
car.play_music()

print(car)
car.print_type()
print('---------')

motorcycle = Motorcycle('Boxer', 'Bajaj', 10, 125, 'gray')
motorcycle.turn_on()
motorcycle.lights_on()

print(motorcycle)
print('---------')

bicycle = Bicycle('Velik', 'Velik marka', 'blue')
bicycle.lights_on()

print(bicycle)
bicycle.print_type()
print('---------')

quadBike = QuadBike('Some quad', 'Quad', 25, 300, 'red')
quadBike.turn_on()

print(quadBike)
print('-------')
print(bicycle <= motorcycle)

print(Transport.get_transports_count())

del bicycle

print(Transport.get_transports_count())

car.turn_off()
car.lights_off()
car.stop_music()

motorcycle.turn_off()
motorcycle.lights_off()

quadBike.turn_off()

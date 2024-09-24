class City:
    def __init__(self, name) -> None:
        self.name = name
        self.routes = {}
    
    def add_route(self, city, price):
        self.routes[city] = price

# Setting up our example cities.
atlanta = City('Atlanta')
boston = City('Boston')
chicago = City('Chicago')
denver = City('Denver')
el_paso = City('El paso')

atlanta.add_route(boston, 100)
atlanta.add_route(boston, 100)
atlanta.add_route(boston, 100)
atlanta.add_route(boston, 100)
atlanta.add_route(boston, 100)
atlanta.add_route(boston, 100)
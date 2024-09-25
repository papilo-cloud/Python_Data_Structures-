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

def dijkstra_shortest_path(starting_city, final_dest):
    cheapest_prices_table = {}
    cheapest_prev_stopover_city_table = {}
    unvisited_cities = [starting_city]
    visited_cities = {}
    
    cheapest_prices_table[starting_city.name] = 0
    current_city = starting_city
    
    while unvisited_cities:
        visited_cities[current_city.name] = 1
        unvisited_cities.remove(current_city)
        
        for (adj_city, price) in current_city.routes.items():
            if not visited_cities.get(adj_city.name) and (
                adj_city not in unvisited_cities):
                unvisited_cities.append(adj_city)
                
                price_through_current_city = \
                    (cheapest_prices_table[current_city.name] + price)
                
                if (not cheapest_prices_table.get(adj_city.name) or 
                        price_through_current_city
                            < cheapest_prices_table[adj_city.name]):
                    
                    cheapest_prices_table[adj_city.name] = \
                        price_through_current_city
                    cheapest_prev_stopover_city_table[adj_city.name] = \
                        current_city.name
        
        cheapest_price = float('inf')
        for city in unvisited_cities:
            if cheapest_prices_table[city.name] < cheapest_price:
                current_city = city
                cheapest_price = cheapest_prices_table[city.name]
                
    shortest_path = []
    current_city_name = final_dest.name
    
    while current_city_name:
        shortest_path.insert(0, current_city_name)
        current_city_name = \
            cheapest_prev_stopover_city_table.get(current_city_name)
            
    return shortest_path
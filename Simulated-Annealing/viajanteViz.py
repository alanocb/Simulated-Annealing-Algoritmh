import random
import math
import matplotlib.pyplot as plt

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def route_length(route, cities):
    length = 0
    for i in range(len(route)):
        current_city = cities[route[i]]
        next_city = cities[route[(i + 1) % len(route)]]
        length += distance(current_city, next_city)
    return length

def generate_neighbor(route):
    a, b = sorted(random.sample(range(len(route)), 2))
    new_route = route.copy()
    new_route[a:b] = reversed(new_route[a:b])
    return new_route

def plot_route_and_cooling(cities, route, temperatures, iteration, image_path, ax_route, ax_cooling, is_final=False):
    route_cities = [cities[i] for i in route]
    route_cities.append(route_cities[0])  # Close the loop
    x, y = zip(*route_cities)

    ax_route.clear()

    # Plot the route
    ax_route.plot(x, y, marker='o', linestyle='-', markersize=8, color='blue')
    for city, (lat, lon) in zip(route, route_cities[:-1]):
        ax_route.text(lat, lon, city, fontsize=8, color='red')
    ax_route.set_title("Best Route" if is_final else f"Iteration {iteration}")
    ax_route.set_xlabel("Latitude")
    ax_route.set_ylabel("Longitude")
    ax_route.grid(True)

    # Display the image in the background with fixed extent
    img = plt.imread(image_path)
    ax_route.imshow(img, extent=[50, 60, 670, 710], aspect='auto')  # Adjust extent as needed

    # Plot the cooling process
    ax_cooling.plot(range(1, iteration + 1), temperatures[:iteration], marker='o', linestyle='-', color='green')
    ax_cooling.set_title("Cooling Process")
    ax_cooling.set_xlabel("Iteration")
    ax_cooling.set_ylabel("Temperature")
    ax_cooling.grid(True)

    plt.tight_layout()
    plt.pause(0.00001)

def simulated_annealing(cities, initial_temp, final_temp, cooling_rate, max_iterations, image_path):
    num_cities = len(cities)
    current_route = list(range(num_cities))
    random.shuffle(current_route)
    best_route = current_route
    current_temp = initial_temp

    temperatures = []  # To store temperature values for plotting

    fig, (ax_route, ax_cooling) = plt.subplots(1, 2, figsize=(12, 5))
    plt.ion()  # Turn on interactive mode for real-time plotting

    for iteration in range(1, max_iterations + 1):
        temperatures.append(current_temp)  # Store the current temperature

        for _ in range(num_cities):
            new_route = generate_neighbor(current_route)
            delta_length = route_length(new_route, cities) - route_length(current_route, cities)

            if delta_length < 0 or random.random() < math.exp(-delta_length / current_temp):
                current_route = new_route

                if route_length(current_route, cities) < route_length(best_route, cities):
                    best_route = current_route

        current_temp *= cooling_rate

        plot_route_and_cooling(cities, current_route, temperatures, iteration, image_path, ax_route, ax_cooling)

    plt.ioff()  # Turn off interactive mode after the loop

    # Plot the final route
    plot_route_and_cooling(cities, best_route, temperatures, max_iterations, image_path, ax_route, ax_cooling, is_final=True)

    plt.show()

    return best_route, route_length(best_route, cities)

# Example usage with an image as a background
cities_coordinates = {
    'Lisboa': (51.29, 683.95),
    'Cascais': (50.67, 683.89),
    'Sintra': (50.87, 684.91),
    'Peniche': (50.86, 688.35),
    'Almada': (51.39, 683.30),
    'Costa': (51.32, 682.87),
    'Setubal': (51.70, 682.44),
    'Sines': (52.32, 678.20),
    'Sagres': (52.03, 671.81),
    'Faro': (55.13, 671.81),
    'Tavira': (55.66, 672.61),
    'Covilha': (55.77, 694.64),
    'Braganca': (58.15, 706.24),
    'Braga': (52.96, 704.36),
    'Guimaraes': (53.15, 703.29),
    'Porto': (52.94, 701.51),
    'Aveiro': (52.76, 697.59),
    'Viseu': (54.70, 697.54),
}

initial_temp = 10000
final_temp = 0.1
cooling_rate = 0.9
max_iterations = 200  
image_path = 'portugal.jpg'  

cities_list = list(cities_coordinates.keys())
cities_positions = [cities_coordinates[city] for city in cities_list]

best_route, length = simulated_annealing(cities_positions, initial_temp, final_temp, cooling_rate, max_iterations, image_path)
print("Best route found:", [cities_list[i] for i in best_route])
print("Length of the best route:", length)

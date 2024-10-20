import sys
import math
import simplekml
from argparse import ArgumentParser

def calculate_radius_from_area(area, sides):
    # Calculate the circumcircle radius for a given area of a regular polygon
    area_m2 = area * 1e6  # Convert km² to m²
    angle = math.pi / sides
    return math.sqrt((2 * area_m2) / (sides * math.sin(2 * angle)))

def calculate_radius_from_perimeter(perimeter, sides):
    # Calculate the circumcircle radius from perimeter of a regular polygon
    side_length = (perimeter * 1000) / sides  # Convert km to m
    angle = math.pi / sides
    return side_length / (2 * math.sin(angle))

def generate_polygon(coords, metric_value, sides, orientation, kml_filename):
    lat, lon = map(float, coords.split(','))

    metric_type = metric_value[0]
    metric = float(metric_value[1:])  # Keep in kilometers

    if metric_type == 'A':
        radius = calculate_radius_from_area(metric, sides)
    elif metric_type == 'P':
        radius = calculate_radius_from_perimeter(metric, sides)
    elif metric_type == 'R':
        radius = metric * 1000  # Convert km to meters
    else:
        raise ValueError("Invalid metric type. Must be 'A' (Area), 'P' (Perimeter), or 'R' (Radius).")

    angle_offset = 2 * math.pi / sides

    # Adjust the starting angle based on orientation
    if orientation == 'NFace':
        start_angle = -math.pi / sides  # Align a face to north
    elif orientation == 'NVertex':
        start_angle = 0  # Align a vertex to north
    else:
        start_angle = 0  # Default if no orientation is given

    kml = simplekml.Kml()
    pol = kml.newpolygon(name=kml_filename)

    coords_list = []
    for i in range(sides):
        angle = start_angle + i * angle_offset
        dx = radius * math.cos(angle) / 111319.9  # Convert meters to degrees for latitude
        dy = radius * math.sin(angle) / (111319.9 * math.cos(math.radians(lat)))  # For longitude correction
        coords_list.append((lon + dy, lat + dx))

    coords_list.append(coords_list[0])  # Close the polygon
    pol.outerboundaryis = coords_list
    pol.style.polystyle.color = '7dff0000'  # Red with partial transparency

    kml.save(kml_filename)

def main():
    parser = ArgumentParser(description='Generate an equilateral polygon in KML format.')
    parser.add_argument('coords', help='Decimal coordinates in the format lat,lon (e.g., "35.6895,139.6917").')
    parser.add_argument('metric_value', help='Metric value prefixed by type (e.g., "A46" for area in km², "P46" for perimeter in km, "R46" for radius in km).')
    parser.add_argument('sides', type=int, choices=range(3, 17), help='Number of sides of the polygon (3 to 16).')
    parser.add_argument('orientation', nargs='?', choices=['NFace', 'NVertex'], default=None, help='Optional orientation: NFace to align a face north, NVertex to align a vertex north.')

    args = parser.parse_args()

    kml_filename = f"polygon_{args.coords.replace(',', '_')}_{args.sides}_sides.kml"
    generate_polygon(args.coords, args.metric_value, args.sides, args.orientation, kml_filename)

if __name__ == '__main__':
    main()

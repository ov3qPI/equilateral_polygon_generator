# equilateral_polygon_generator
Generate an equilateral polygon (with between 3 and 16 sides) centered at a specified latitude and longitude.

## Features
- Generate polygons with **3 to 16 sides**.
- Specify the size of the polygon using **Area (km²)**, **Perimeter (km)**, or **Radius (km)**.
- Choose the orientation of the polygon, aligning a **face** or **vertex** to true north.

## Prerequisites
- Python 3.x
- `simplekml` library

To install `simplekml`, run:
```sh
pip install simplekml
```

## Usage
The script is executed from the command line with the following arguments:

```sh
python equilateral_polygon_generator.py <coords> <metric_value> <sides> [orientation]
```

### Arguments
1. **`coords`**: Decimal coordinates representing latitude and longitude of the center of the polygon.
   - Format: `lat,lon` (e.g., `36.472300,-110.795540`)

2. **`metric_value`**: A value that determines the size of the polygon. It must be prefixed by a letter indicating the type:
   - `A##` - Area in square kilometers (e.g., `A46` for 46 km²).
   - `P##` - Perimeter in kilometers (e.g., `P10` for a perimeter of 10 km).
   - `R##` - Radius in kilometers (e.g., `R5` for a radius of 5 km).

3. **`sides`**: The number of sides of the polygon. Must be between **3 and 16**.

4. **`orientation`** (Optional): Align the polygon to true north.
   - `NFace` - Align a **face** of the polygon north.
   - `NVertex` - Align a **vertex** of the polygon north.

### Example Commands
- Generate a pentagon with an area of 46 km², with a vertex aligned north:
  ```sh
  python equilateral_polygon_generator.py "36.472300,-110.795540" A46 5 NVertex
  ```

- Generate a hexagon with a perimeter of 20 km, with a face aligned north:
  ```sh
  python equilateral_polygon_generator.py "36.472300,-110.795540" P20 6 NFace
  ```

- Generate a square with a radius of 3 km, without specifying orientation:
  ```sh
  python equilateral_polygon_generator.py "36.472300,-110.795540" R3 4
  ```

## Output
The script generates a KML file named based on the coordinates and the number of sides of the polygon. For example:
```
polygon_36.472300_-110.795540_5_sides.kml
```
This file can be opened in Google Earth or other geographic visualization tools to view the generated polygon.

## Notes
- The script uses **kilometers** as the default unit for all inputs.
- Ensure that you provide valid values for each argument, as incorrect formats or unsupported values will result in an error.

# Point Cloud to Video
Converts a 3d point cloud to a video, using three.js and `ffmpeg`. 
Load Javascript data, render using three.js, and save the canvas to a 
png. Additionally supplies a utility for converting a specific `.npy` 
format to Javascript.

> Note that this repository isn't general at all. You'll probably need to hack it for your own purposes. I've done the heavy lifting (i.e., mixed and matched from the relevant Three.js docs) to render the point cloud though. 

# Usage

1. Clone the repository recursively (replace with HTTP below if you don't have keys setup)

```
git clone --recursive git@github.com:alvinwan/pc2vid.git
```
2. Create a new `js/output.js` file with the structure described in `Point Cloud Format` below. This should match the format described at [antsy3d](https://github.com/alvinwan/antsy3d#point-cloud-format). The latter takes precedence.
3. Open `js_to_png.html` in your browser. The app will begin saving frames as PNGs every half-second. The PNG filename will match the key provided in the original data dictionary. The example from `Point Cloud Format`, for example, would output `frog.png`.
4. Run the `png_to_mp4.sh` bash script. (`ffmpeg`)

## Point Cloud Format

`js/output.js` defines a global variable `data`, a dictionary mapping unique point cloud names to point cloud data; point clouds have a `vertices` property, a list of vertices, each with `.x`, `.y` and `.z` properties.

e.g., To access the `x` position of the first point in the point cloud named `frog`, you would access `data.frog.vertices[0].x`. Simple example of `output.js`:

```
var data = {
   'frog': {
      'vertices': [
          {'x': 3.5, 'y': 3.5, 'z': 5.6},
          {'x': 1.0, 'y': 1.2, 'z': 3.4}
      ]
   }
}
```

# `.npy` Conversion Tool

Note this tool is extremely specific to our own data format. It may be
wortwhile to code your own from scratch. To use it, install `numpy`

```
pip install numpy
```

Then, run

```
python to_json.py 
```

> **Why not build a Python utility?** I tried looking around, but visualizations
I explored used a backend I didn't have (and didn't want to bother installing).
However, this utility just uses the browser, which every computer has.
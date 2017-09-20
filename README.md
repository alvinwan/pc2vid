# Point Cloud to Video
Converts a 3d point cloud to a video, using three.js and `ffmpeg`. 
Load Javascript data, render using three.js, and save the canvas to a 
png. Additionally supplies a utility for converting a specific `.npy` 
format to Javascript.

![2011_09_26_0001](https://user-images.githubusercontent.com/2068077/30610372-cbb0fe3a-9d32-11e7-8dd5-6902e25258dc.gif)
*LiDAR data and images belong to the KITTI dataset's copyright holders.*

> Note that this repository isn't general at all. You'll probably need to hack it for your own purposes. I've done the heavy lifting (i.e., mixed and matched from the relevant Three.js docs) to render the point cloud though. 

# Usage

1. Clone the repository recursively (replace with HTTP below if you don't have keys setup)

```
git clone --recursive git@github.com:alvinwan/pc2vid.git
```

## General Usage 
2. Create a new `js/output.js` file with the structure described in `Point Cloud Format` below. This should match the format described at [antsy3d](https://github.com/alvinwan/antsy3d#point-cloud-format). The latter takes precedence.
3. Open `js_to_png.html` in your browser. The app will begin saving frames as PNGs every half-second. The PNG filename will match the key provided in the original data dictionary. The example from `Point Cloud Format`, for example, would output `frog.png`.
4. Run the `png_to_mp4.sh` bash script. (`ffmpeg`)

## Pallas-Specific Usage

2. Download `.npy` files to `data/<dataset>`. (For example, you could have `data/0001_pred/{000000000,0000000001...}.npy`) Make sure all files match `%10d.npy`.
3. Run `python to_json.py <dataset> <start> <end>`. There's too much data to load at once, so we have to split up, say, 159 images, into chunks of ~40. (e.g., run `python to_json.py 0001_pred 0 40`. Do next step, then `python to_json.py 0001_pred 40 80`...)
4. Open `js_to_png.html` in your browser. This will render and download each image.

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

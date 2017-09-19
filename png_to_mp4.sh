# For scaling below, see discussion at https://stackoverflow.com/q/20847674/4855984
ffmpeg -r 4 -f image2 -i output/%010d.png -crf 25 -vcodec libx264 -pix_fmt yuv420p -vf scale=1280:-2 2011_09_26_0001.mp4

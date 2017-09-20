# For scaling below, see discussion at https://stackoverflow.com/q/20847674/4855984
ffmpeg -r 10 -f image2 -i output/0005_pred/2011_09_26_0005_%010d.png -crf 25 -vcodec libx264 -pix_fmt yuv420p -vf scale=2200:-2 2011_09_26_0005_pred.mp4

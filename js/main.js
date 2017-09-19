start = 51; // index of point cloud to start at
N = 108 // number of point clouds

window.onload = function() {
    function draw(i) {
        obj_name = i.toString().padStart(10, '0');
        display(obj_name);
        setTimeout(function() { download(i); }, 500);
    }
    function download(i) {
        save_image();
        if (i < N) {
            draw(i+1);
        }
    }
    draw(start);
}

start = 0; // index of point cloud to start at
N = 160 // number of point clouds

window.onload = function() {
    function draw(i) {
        obj_name =  i.toString().padStart(10, '0');
        if (obj_name in data) {
            display(obj_name);
            setTimeout(function() { download(i); }, 500);
        } else {
            if (i < N) {
                draw(i+1);
            }
        }
    }
    function download(i) {
        save_image();
        if (i < N) {
            draw(i+1);
        }
    }
    draw(start);
}

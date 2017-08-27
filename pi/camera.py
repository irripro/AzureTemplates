from picamera import PiCamera
from time import sleep
import time, sys, os

def cleanup(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for file_ in files:
            full_path = os.path.join(root, file_)
            os.remove(full_path)

def camera_still():
    camera = PiCamera()
    camera.rotation = 270
    camera.resolution = (2592, 1944)
    camera.start_preview()

    # Wait for light to adjust
    sleep(3)

    # Set a timestamp
    timestamp = int(time.time())

    # Add a filename with a timestamp
    filename = "./stills/img_{}.jpg".format(str(timestamp))
    camera.capture(filename)
    camera.stop_preview()
    print('File has been stored as: {}'.format(filename))

def camera_video():
    camera = PiCamera()
    camera.rotation = 270

    camera.start_preview()

    # Add a filename with a timestamp
    timestamp = int(time.time())
    filename = "./videos/video_{}.h264".format(str(timestamp))
    camera.start_recording(filename)
    sleep(10)
    camera.stop_recording()
    camera.stop_preview()

    print('File has been stored as: {}'.format(filename))


def main():
    try:
        if ('still' in sys.argv[1]):
            camera_still()
        elif ('video' in sys.argv[1].lower()):
            camera_video()
    except:
        print("The way to use this is: 'python [video/still]'")

if __name__== "__main__":
    cleanup("/home/pi/camera/stills")
    cleanup("/home/pi/camera/videos")
    main()

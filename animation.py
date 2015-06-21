import matplotlib
matplotlib.use('GTKAgg')
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy


class Recorder:

    def __init__(self):
        self.frames = []

    def record_frame(self, frame):
        self.frames.append(numpy.array(frame))

    def record_still_frame(self, frame, count):
        for i in range(0, count):
            self.record_frame(frame)

    def finish(self):
        self.fig = plt.figure()
        im = plt.imshow(self.frames[0], interpolation='nearest')

        def updatefig(frame):
            im.set_array(frame)
            return im,

        self.ani = animation.FuncAnimation(self.fig, updatefig, frames=self.frames, interval=5, blit=True)

    def show(self):
        plt.show()

    def save(self, name, fps=90):
        filename = name + '.mp4'
        self.ani.save(filename, codec='libx264', writer='ffmpeg', fps=fps)


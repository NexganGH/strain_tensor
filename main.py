import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


tensor = np.zeros((3, 3), dtype=float)

points = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0], [1, 1, 0]])


def get_modified_coordinate(x, tensor_row, point_):
    new_x = x
    for j in range(3):
        new_x += tensor_row[j] * point_[j]
    return new_x


def get_modified_point(point_, tensor_):
    new_point = [0, 0, 0]
    for i in range(3):
        new_point[i] = get_modified_coordinate(point_[i], tensor_[i], point_)
    return new_point


fig: plt.Figure = plt.figure()

ax = fig.add_subplot(111, projection='3d')


def draw_points():
    new_points = []

    for point in points:
        new_points.append(get_modified_point(point, tensor))

    new_points = np.array(new_points)

    ax.clear()
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], c='b')

    ax.scatter(new_points[:, 0], new_points[:, 1], new_points[:, 2], c='r')
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_zlim(-5, 5)


ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.ion()

draw_points()

fig2 = plt.figure()


ax_1 = plt.axes([0.2, 0.01, 0.65, 0.03])
ax_2 = plt.axes([0.2, 0.05, 0.65, 0.03])
ax_3 = plt.axes([0.2, 0.10, 0.65, 0.03])
ax_4 = plt.axes([0.2, 0.15, 0.65, 0.03])
ax_5 = plt.axes([0.2, 0.20, 0.65, 0.03])
ax_6 = plt.axes([0.2, 0.25, 0.65, 0.03])

xx_s = Slider(ax_1, 'Strain xx', -10, 10, valinit=0)
yy_s = Slider(ax_2, 'Strain yy', -10, 10, valinit=0)
zz_s = Slider(ax_3, 'Strain zz', - 10, 10, valinit=0)
xy_s = Slider(ax_4, 'Strain xy', - 10, 10, valinit=0)
xz_s = Slider(ax_5, 'Strain xz', - 10, 10, valinit=0)
yz_s = Slider(ax_6, 'Strain yz', - 10, 10, valinit=0)


def update_plot(value):
    tensor[0][0] = xx_s.val
    tensor[1][1] = yy_s.val
    tensor[2][2] = zz_s.val

    tensor[0][1] = xy_s.val
    tensor[1][0] = xy_s.val

    tensor[0][2] = xz_s.val
    tensor[2][0] = xz_s.val

    tensor[1][2] = yz_s.val
    tensor[2][1] = yz_s.val

    draw_points()


xx_s.on_changed(update_plot)
yy_s.on_changed(update_plot)
zz_s.on_changed(update_plot)
xy_s.on_changed(update_plot)
xz_s.on_changed(update_plot)
yz_s.on_changed(update_plot)


plt.show(block=True)

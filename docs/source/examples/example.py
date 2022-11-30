import os
import k3d
import numpy as np

def func():
    data = np.load('streamlines_data.npz')
    v = data['v']
    lines = data['lines']
    vertices = data['vertices']
    indices = data['indices']

    plt_streamlines = k3d.line(lines,
        width=0.00007, attribute=v,
        color_map=k3d.colormaps.matplotlib_color_maps.Inferno,
        color_range=[0, 0.5], shader='mesh')

    plt_mesh = k3d.mesh(vertices, indices,
        opacity=0.25, wireframe=True, color=0x0002)

    plot = k3d.plot(grid_visible=False, screenshot_scale=1.0, axes_helper=0)

    plot += plt_streamlines
    plot += plt_mesh
    return plot

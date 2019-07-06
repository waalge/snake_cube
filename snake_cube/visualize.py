#!/usr/bin/env python3

"""
Create a visualization of solution.
Feeds the absolute coordinates of a solution into vtk.

Code adapted from one of the examples on vtk wiki.
"""

import numpy as np
import vtk
from vtk.util.colors import tomato

import cube_data

def basic_cyclinder():
    """
    Basic attributes of a cylinder used by segment
    """
    cylinder = vtk.vtkCylinderSource()
    cylinder.SetResolution(15)
    cylinder.SetHeight(1)
    cylinder.SetRadius(0.03)
    return cylinder

def path_segment(center, rot, length):
    """
    Orient cylinder to be path segment.
    """
    cylinder = basic_cyclinder()
    cylinder.SetHeight(length)
    cylinderMapper = vtk.vtkPolyDataMapper()
    cylinderMapper.SetInputConnection(cylinder.GetOutputPort())

    cylinderActor = vtk.vtkActor()
    cylinderActor.SetMapper(cylinderMapper)
    cylinderActor.GetProperty().SetColor(tomato)
    cylinderActor.SetPosition(center)

    cylinderActor.RotateX(rot[0])
    cylinderActor.RotateY(rot[1])
    cylinderActor.RotateZ(rot[2])
    return cylinderActor

def path(coords):
    """
    Concatenate a list of path segments.
    """
    coords = [np.array(c) for c in coords]
    segments = []
    for cnt, coord in enumerate(coords[:-1]):
        center = (coord + coords[cnt+1])/2
        orientaion = (coords[cnt+1] - coord)
        rots = (0, 0, 0)
        if orientaion[0] != 0:
            rots = (0, 0, -90)
            length = abs(orientaion[0])
        if orientaion[1] != 0:
            length = abs(orientaion[1])
        if orientaion[2] != 0:
            length = abs(orientaion[2])
            rots = (90, 0, 0)
        segments.append(path_segment(center, rots, length))
    return segments

if __name__ == '__main__':
    ren = vtk.vtkRenderer()
    renWin = vtk.vtkRenderWindow()
    renWin.AddRenderer(ren)
    iren = vtk.vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    # Add the actors to the renderer, set the background and size
    solutions = cube_data.CUBES[2]["abs_solutions"]
    path_coords = [(0, 0, 0)] + solutions[0]
    print("Sols", len(solutions))
    P = path(path_coords)
    for segment in P:
        ren.AddActor(segment)
    ren.SetBackground(0.1, 0.2, 0.4)
    renWin.SetSize(200, 200)

    # This allows the interactor to initalize itself. It has to be
    # called before an event loop.
    iren.Initialize()

    # We'll zoom in a little by accessing the camera and invoking a "Zoom"
    # method on it.
    ren.ResetCamera()
    ren.GetActiveCamera().Zoom(1.5)
    renWin.Render()

    # Start the event loop.
    iren.Start()

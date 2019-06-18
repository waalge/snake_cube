#!/usr/bin/env python3

# This simple example shows how to do basic rendering and pipeline
# creation.

import numpy as np
import vtk
import solutions

# The colors module defines various useful colors.
from vtk.util.colors import tomato

def basic_cyclinder():
    # This creates a polygonal cylinder model with eight circumferential
    # facets.
    cylinder = vtk.vtkCylinderSource()
    cylinder.SetResolution(15)
    cylinder.SetHeight(1)
    cylinder.SetRadius(0.03)
    return cylinder

def path_segment(center, rot,length):
    cylinder = basic_cyclinder() 
    cylinder.SetHeight(length)
    # The mapper is responsible for pushing the geometry into the graphics
    # library. It may also do color mapping, if scalars or other
    # attributes are defined.
    cylinderMapper = vtk.vtkPolyDataMapper()
    cylinderMapper.SetInputConnection(cylinder.GetOutputPort())

    # The actor is a grouping mechanism: besides the geometry (mapper), it
    # also has a property, transformation matrix, and/or texture map.
    # Here we set its color and rotate it -22.5 degrees.
    cylinderActor = vtk.vtkActor()
    cylinderActor.SetMapper(cylinderMapper)
    cylinderActor.GetProperty().SetColor(tomato)
    cylinderActor.SetPosition(center)
    #print("Orient", cylinderActor.GetOrientation())
    #cylinderActor.SetOrientation(orientation)
    #cylinder_methods = [method_name for method_name in dir(cylinderActor) if callable(getattr(cylinderActor, method_name))]
    #print(cylinder_methods)

    cylinderActor.RotateX(rot[0])
    cylinderActor.RotateY(rot[1])
    cylinderActor.RotateZ(rot[2])
    return cylinderActor

def path(coords):
    coords = [np.array(c) for c in coords] 
    segments = []
    for ii, coord in enumerate(coords[:-1]):
        center = (coord + coords[ii+1])/2 
        orientaion = (coords[ii+1] - coord)
        rots = (0,0,0)
        if orientaion[0] != 0:
            rots = (0,0,-90) 
            length = abs(orientaion[0]) 
        if orientaion[1] != 0:
            length = abs(orientaion[1]) 
        if orientaion[2] != 0:
            length = abs(orientaion[2]) 
            rots = (90,0,0) 
        segments.append(path_segment(center,rots,length))
    return segments 

# Create the graphics structure. The renderer renders into the render
# window. The render window interactor captures mouse events and will
# perform appropriate camera or actor manipulation depending on the
# nature of the events.
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

# Add the actors to the renderer, set the background and size
path_coords = [(0,0,0)] + solutions.solutions[0]
print("Sols", len(solutions.solutions))
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

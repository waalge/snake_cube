from setuptools import setup

setup(
   name='snake_cube',
   version='0.0',
   description='Solve any snake cube',
   author='waalge',
   author_email='waalgy@gmail.com',
   packages=['snake_cube'],  #same as name
   install_requires=['vtk'], #external packages as dependencies
)

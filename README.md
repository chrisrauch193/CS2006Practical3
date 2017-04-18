# CS2006Practical3: Python 2

The following dependencies are required:

  - python=3.6
  - numpy
  - matplotlib
  - pandas
  - ipywidgets
  - ipykernel
  - basemap

The project can be run in one of three environments:


1. Standard Python.

Using a standard Python installation, install the dependencies using pip.

After installing ipywidgets, you will need to enable the ipywidgets extension using the command:

  jupyter nbextension enable --py widgetsnbextension --sys-prefix

Installing basemap through pip will also require geos and proj4, which must be downloaded from their respective websites and built
from source files.  This will not work without administrator privileges on lab machines.


2. Anaconda

If using Anaconda, install the dependencies using conda.  The ipywidgets extension should already be enabled.

Installing basemap through conda also installs geos and proj4, and so this is the preferred method for enabling basemap functionality.  If you are unable to install anaconda, all other sections of the notebook will work apart from the BaseMap plot of the regions by population.


3. Binder

The Binder virtual environment has also been provided to run the project without access to any of the dependencies.  An environment.yml file is included in the project which describes the dependencies required to run, and an environment has been pre-built which can be accessed at the following link:

...

The first attempt at launching may result in failure, but refreshing will fix this problem.

# CS2006Practical3: Python 2

The following dependencies are required to run the analysis locally:

  - python
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

Installing basemap through pip requires geos and proj4 to be installed separately.  These tools must be downloaded from their respective websites and built
from source.  This will not work without administrator privileges on lab machines, but the instructions to set up this environment where these privileges are available are available at matplotlib.org/basemap/users/installing.html.

If you are unable to install basemap, all other sections of the notebook will work apart from the BaseMap plot of the regions by population.

2. Anaconda

If using Anaconda, install the dependencies using the conda tool.  The ipywidgets extension should be automatically enabled using this method.

Installing basemap through conda also installs geos and proj4, and so this is the preferred method for enabling basemap functionality.


3. Binder

The Binder virtual environment has also been provided to run the project without access to any of the dependencies.  An environment.yml file is included in the project which describes the dependencies required to run.  The environment itself has been pre-built, and can be accessed at the following link:

  mybinder.org/repo/chrisrauch193/cs2006practical3

The first attempt at launching may result in failure, but refreshing will fix this problem.


4. Docker

A Dockerfile was made to allow use of Docker distribution. It was created to use the repo when the repo was private. It worked and was built successfully, but now that the repo is the public and is using the binder it may not work. We have included screenshots to show proof of successful builds.

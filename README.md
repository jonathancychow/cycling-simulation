[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jonathancychow/cycling-simulation/main?filepath=notebooks%2Fcycling_simulation.ipynb)
![Heroku](https://heroku-badge.herokuapp.com/?app=cycling-sim)

# cycling.model
Model to simulate performance for cycling time trial

# Deployment
The dashboard is hosted at [Heroku](https://cycling-sim.herokuapp.com/) and [AWS](http://cycle.us-east-2.elasticbeanstalk.com/).

The jupyter notebook is hosted at Binder, please see this [link](https://mybinder.org/v2/gh/jonathancychow/cycling-simulation/main?filepath=notebooks%2Fcycling_simulation.ipynb).

# Getting started

The `tox` package is used for development, test and build. Tox is a build tool for python. It allowes us to define a set of standards and configure a set of commands
to make sure the project is maintainable by others. See also:

- [tox](https://tox.readthedocs.io/en/latest/)
- [flask](http://flask.pocoo.org/)
- [virtualenv](https://virtualenv.pypa.io/en/stable/)

For an introduction to python directory structures, see [here.](https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure)


### Create a development environment - develop

This step makes sure we create an isolated python environment from the rest of the system.
Current this python environment exists under the newly created directory ".venv" under the project root folder.

### Make sure tox is installed
If your OS is MacOS
```
pip install tox
```
If your OS is Window, do the following instead as there is a [bug](https://github.com/tox-dev/tox/issues/1550) still unresolved.
```
pip install tox==3.8.3
```
### Create develop environment
```
tox -e develop
```

You can verify the python versions by running the following if your OS is Mac
```
./.venv/bin/python -V
```
If your OS is Window
```
.\.venv\Scripts\python -V
```
Start the web server
```
tox -e serve
```

### Start Jupyter Notebook
```
source .venv/bin/activate
jupyter notebook
```

If you want to quickly interact with a pre-built Jupyter Notebook, you can click [here](https://mybinder.org/v2/gh/jonathancychow/cycling-simulation/main?filepath=notebooks%2Fcycling_simulation.ipynb), I have set it all up in MyBinder.

A trim down notebook is set up for youngster to learn more about Python and simulation, see this [link](https://mybinder.org/v2/gh/jonathancychow/cycling-simulation/main?filepath=notebooks%2Fcycling_simulation_edu.ipynb).

# Test
### Static code analysis - lint

This step verifies the code style of the project and makes sure that common inconsistencies are avoided. You can
easily check for common bugs and also improve the readability of the code.

```
tox -e lint
```

### Unit and functional testing - test

Testing verifies the functional requirements of the application. We use pytest but this is configurable by the developer
in case a different framework is needed.

```
tox -e test
```



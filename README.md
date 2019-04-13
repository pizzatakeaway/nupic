# Numenta Platform for Intelligent Computing

The Numenta Platform for Intelligent Computing (NuPIC) is a machine intelligence platform that implements the HTM learning algorithms. HTM is a detailed computational theory of the neocortex. At the core of HTM are time-based continuous learning algorithms that store and recall spatial and temporal patterns. NuPIC is suited to a variety of problems, particularly anomaly detection and prediction of streaming data sources. For more information, see numenta.org or the NuPIC Forum.

For usage guides, quick starts, and API documentation, see http://nupic.docs.numenta.org/.


# This Project
This project aims to investigate HTM performances for **multivariate Anomaly Detection tasks**.  
We will investigate both the performances of *dependent* and *independent* HTM-models.  
In this repo we will work using dasets presented in [NAB](https://github.com/numenta/NAB)


### Dependencies
The following dependencies are required to install NuPIC on all operating systems.

- [Python 2.7](https://www.python.org/)
- [pip](https://pip.pypa.io/en/stable/installing/)>=8.1.2
- [setuptools](https://setuptools.readthedocs.io)>=25.2.0
- [wheel](http://pythonwheels.com)>=0.29.0
- [numpy](http://www.numpy.org/)
- C++ 11 compiler like [gcc](https://gcc.gnu.org/) (4.8+) or [clang](http://clang.llvm.org/)
- MySQL `$ sudo apt install mysql-server` and then follow the [instructions](https://www.digitalocean.com/community/tutorials/how-to-install-the-latest-mysql-on-ubuntu-18-04) starting from *Step 2*.


# Install
1. Git clone: (https://github.com/pizzatakeaway/nupic)[https://github.com/pizzatakeaway/nupic]
1. Install the environment, type `$ pipenv --two` when in `~/Anomaly_Detection/nupic`.  
The environment is installed in `~/.local/share/virtualenvs/nupic-yn_sXeWq/lib/python2.7/site-packages/nupic`.
1. Activate environment `$ pipenv shell`
1. Install requirements `$ pip install -r requirements`.  
For the list of dependencies: [nupic](https://github.com/numenta/nupic).
1. Install *nupic* `$ pip install nupic`
1. Test *nupic* running `$ py.test tests/unit`
1. To perform swarming:
    - Install MySQL, `$ sudo apt install mysql-server` and then follow the [instructions](sudo apt install mysql-server) starting from *Step 2*.
    - Since `root` has a password, create in `$ /nupic/src/nupic/support` the file `nupic-site.xml` that looks like this

    ```
    <?xml version="1.0"?>
    <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

    <configuration>

    <!-- database credentials, used for swarming -->

    <property>
    <name>nupic.cluster.database.host</name>
    <value>localhost</value>
    <description>Name of the machine running the MySQL database server</description>
    </property>

    <property>
    <name>nupic.cluster.database.user</name>
    <value>root</value>
    <description>Username for the MySQL database server </description>
    </property>

    <property>
    <name>nupic.cluster.database.passwd</name>
    <value>yourpassword</value>
    <description>Password for the MySQL database server </description>
    </property>

    </configuration>
    ```

    and enter the password in #22.  
    Finally copy `nupic-site.xml` in `~/.local/share/virtualenvs/nupic-yn_sXeWq/lib/python2.7/site-packages/nupic`.  
    - Always make sure `PyMySQL = 0.9.3` is installed.
    - Test *swarm* with `$ python examples/swarm/test_db.py`

1. Install `$ python -m pip install jupyter`

**NOTE:**
- Always perform installations and work inside the environment


### Notebooks
1. `Notebooks/Walkthrough_HTM Univariate.ipynb`: example with *1 Field* of how `Encoders`, `Spatial Pooler` and `Temporal Memory` are built upon each other, and how to perform a *walk* along the alogorithm from input to output and vice versa.
1. `Notebooks/Walkthrough_HTM Multivariate.ipynb`: example with *multiple Fields (2)* of how `Encoders`, `Spatial Pooler` and `Temporal Memory` are built upon each other, and how to perform a *walk* along the alogorithm from input to output and vice versa.

### Input Data
The input data need to be formatted as described in: [link](http://nupic.docs.numenta.org/stable/quick-start/example-data.html).

### Hyperparameters
To find the right hyperparameters we decided to adopt the *swarming algorithm*, implemented in [nupic](https://github.com/numenta/nupic).

### Swarm

1. create/edit `search_def.json`:
    1. **Error Metric**: by default, your model’s accuracy will be evaluated using a MAPE (Mean Average Percent Error) error metric over the last 1000 records seen by the model.
    1. **Custom Error Metric**: [link](http://nupic.docs.numenta.org/stable/guides/swarming/running.html#using-custom-error-metrics)
1. run `run_swarm.py --maxWorkers=4`
1. The parameters models returned by `swarm.py` performed very poorly. See `~ab_experiments/notebooks/Univariate_SwarmParam.ipynb`. 

The paramaters returned by `from nupic.frameworks.opf.common_models.cluster_params import getScalarMetricWithTimeOfDayAnomalyParams` perform way better.
This has then been used in all other experiments.

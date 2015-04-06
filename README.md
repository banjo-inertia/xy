datac - Utility for managing 2D data
************************************

Scope
=====
Thinking of (and plotting) data in terms of an independent and dependent variable is ubiquitous. Oftentimes additional constants need to be included with such data. Despite the ubiquity of this kind of data, everyone seems to reinvent their own methods for handling it. This package provides utilities for managing two-dimensional data sets and associated constants.


Installation
============

Dependencies
------------

* [matplotlib](http://matplotlib.org)
* [astropy](http://www.astropy.org)

The datac module currently only works with python 2.7.


Building from source
--------------------
This module is currently only available by building from source via github. First, clone the [git repo](https://github.com/jrsmith3/datac) or uncompress a tarball of the source. Second, execute the following command:

```
conda build path/to/datac/conda.recipe
```

Finally, install the built package with:

```
conda install datac --use-local
```


License
-------
The code is licensed under the [MIT license](http://opensource.org/licenses/MIT). You can use this code in your project without telling me, but it would be great to hear about who's using the code. You can reach me at <joshua.r.smith@gmail.com>.

Contributing
------------
The repository is hosted on [github](https://github.com/jrsmith3/datac) . Feel free to fork this project and/or submit a pull request. Please notify me of any issues using the [issue tracker](https://github.com/jrsmith3/datac/issues). In the unlikely event that a community forms around this project, please adhere to the [Python Community code of conduct](https://www.python.org/psf/codeofconduct/).

Version numbers follow [PEP 440](https://www.python.org/dev/peps/pep-0440/). The first three segments (major.minor.patch) should be interpreted according to the [semver](http://semver.org) rubric.

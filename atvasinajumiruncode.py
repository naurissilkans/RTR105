Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 
================= RESTART: /home/user/RTR105/Atvasinajums.py =================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/Atvasinajums.py'}
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/Atvasinajums.py', 'sys': <module 'sys' (built-in)>}
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/Atvasinajums.py', 'sys': <module 'sys' (built-in)>, 'sin': <ufunc 'sin'>, 'linspace': <function linspace at 0x7fd4980d4e18>}
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/Atvasinajums.py', 'sys': <module 'sys' (built-in)>, 'sin': <ufunc 'sin'>, 'linspace': <function linspace at 0x7fd4980d4e18>, 'x': array([0. , 0.4, 0.8, 1.2, 1.6, 2. , 2.4, 2.8, 3.2, 3.6, 4. ])}
>>> x
array([0. , 0.4, 0.8, 1.2, 1.6, 2. , 2.4, 2.8, 3.2, 3.6, 4. ])
>>> sin(x)
array([ 0.        ,  0.38941834,  0.71735609,  0.93203909,  0.9995736 ,
        0.90929743,  0.67546318,  0.33498815, -0.05837414, -0.44252044,
       -0.7568025 ])
>>> 
================= RESTART: /home/user/RTR105/Atvasinajums.py =================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/Atvasinajums.py'}
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/Atvasinajums.py', 'sys': <module 'sys' (built-in)>}
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/Atvasinajums.py', 'sys': <module 'sys' (built-in)>, 'sin': <ufunc 'sin'>, 'linspace': <function linspace at 0x7fc894cfae18>}
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/Atvasinajums.py', 'sys': <module 'sys' (built-in)>, 'sin': <ufunc 'sin'>, 'linspace': <function linspace at 0x7fc894cfae18>, 'x': array([0. , 0.4, 0.8, 1.2, 1.6, 2. , 2.4, 2.8, 3.2, 3.6, 4. ])}
>>> type(x)
<class 'numpy.ndarray'>
>>> x
array([0. , 0.4, 0.8, 1.2, 1.6, 2. , 2.4, 2.8, 3.2, 3.6, 4. ])
>>> x[0]
0.0
>>> x[1]
0.4
>>> x[2]
0.8
>>> x[10]
4.0
>>> x[11]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    x[11]
IndexError: index 11 is out of bounds for axis 0 with size 11
>>> 
================= RESTART: /home/user/RTR105/Atvasinajums.py =================
>>> x
array([0. , 0.4, 0.8, 1.2, 1.6, 2. , 2.4, 2.8, 3.2, 3.6, 4. ])
>>> y
array([ 0.        ,  0.38941834,  0.71735609,  0.93203909,  0.9995736 ,
        0.90929743,  0.67546318,  0.33498815, -0.05837414, -0.44252044,
       -0.7568025 ])
>>> 
================= RESTART: /home/user/RTR105/Atvasinajums.py =================
Traceback (most recent call last):
  File "/home/user/RTR105/Atvasinajums.py", line 16, in <module>
    from mathplotlib import pyplot as plt
ModuleNotFoundError: No module named 'mathplotlib'
>>> 
================= RESTART: /home/user/RTR105/Atvasinajums.py =================

Warning (from warnings module):
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/font_manager.py", line 281
    'Matplotlib is building the font cache using fc-list. '
UserWarning: Matplotlib is building the font cache using fc-list. This may take a moment.

================= RESTART: /home/user/RTR105/Atvasinajums.py =================

================= RESTART: /home/user/RTR105/Atvasinajums.py =================
Traceback (most recent call last):
  File "/home/user/RTR105/Atvasinajums.py", line 22, in <module>
    legend.append("$sin(x)$ - default - viss savienots ar taisnaam liinijaam")
NameError: name 'legend' is not defined
>>> 
================= RESTART: /home/user/RTR105/Atvasinajums.py =================
Traceback (most recent call last):
  File "/home/user/RTR105/Atvasinajums.py", line 22, in <module>
    legend.append("$sin(x)$ - default - viss savienots ar taisnaam liinijaam")
NameError: name 'legend' is not defined
>>> 
================= RESTART: /home/user/RTR105/Atvasinajums.py =================
[]
['$sin(x)$ - default - viss savienots ar taisnaam liinijaam']
['$sin(x)$ - default - viss savienots ar taisnaam liinijaam', '$sin(x)$ - tikai dazi punktim']

================= RESTART: /home/user/RTR105/Atvasinajums.py =================
Traceback (most recent call last):
  File "/home/user/RTR105/Atvasinajums.py", line 29, in <module>
    print(plt.legend._doc_)
AttributeError: 'function' object has no attribute '_doc_'
>>> 
>>> 
>>> print(plt._doc_)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print(plt._doc_)
AttributeError: module 'matplotlib.pyplot' has no attribute '_doc_'
>>> print(plt.__doc__)

`matplotlib.pyplot` is a state-based interface to matplotlib. It provides
a MATLAB-like way of plotting.

pyplot is mainly intended for interactive plots and simple cases of programmatic
plot generation::

    import numpy as np
    import matplotlib.pyplot as plt

    x = np.arange(0, 5, 0.1)
    y = np.sin(x)
    plt.plot(x, y)

The object-oriented API is recommended for more complex plots.

>>> 
================= RESTART: /home/user/RTR105/Atvasinajums.py =================
Traceback (most recent call last):
  File "/home/user/RTR105/Atvasinajums.py", line 30, in <module>
    print(plt.legend._doc_)
AttributeError: 'function' object has no attribute '_doc_'
>>> 
================= RESTART: /home/user/RTR105/Atvasinajums.py =================
Traceback (most recent call last):
  File "/home/user/RTR105/Atvasinajums.py", line 30, in <module>
    print(plt.legend._doc_)
AttributeError: 'function' object has no attribute '_doc_'
>>> 
================= RESTART: /home/user/RTR105/Atvasinajums.py =================

================= RESTART: /home/user/RTR105/Atvasinajums.py =================

================= RESTART: /home/user/RTR105/Atvasinajums.py =================

================= RESTART: /home/user/RTR105/Atvasinajums.py =================

================= RESTART: /home/user/RTR105/Atvasinajums.py =================
Traceback (most recent call last):
  File "/home/user/RTR105/Atvasinajums.py", line 40, in <module>
    plt.plot(x,derivative,"y")
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/pyplot.py", line 3261, in plot
    ret = ax.plot(*args, **kwargs)
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/__init__.py", line 1717, in inner
    return func(ax, *args, **kwargs)
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/axes/_axes.py", line 1372, in plot
    for line in self._get_lines(*args, **kwargs):
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/axes/_base.py", line 404, in _grab_next_args
    for seg in self._plot_args(this, kwargs):
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/axes/_base.py", line 384, in _plot_args
    x, y = self._xy_from_xy(x, y)
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/axes/_base.py", line 243, in _xy_from_xy
    "have shapes {} and {}".format(x.shape, y.shape))
ValueError: x and y must have same first dimension, but have shapes (11,) and (1,)
>>> 
================= RESTART: /home/user/RTR105/Atvasinajums.py =================
Traceback (most recent call last):
  File "/home/user/RTR105/Atvasinajums.py", line 41, in <module>
    plt.plot(x,derivative,"y")
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/pyplot.py", line 3261, in plot
    ret = ax.plot(*args, **kwargs)
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/__init__.py", line 1717, in inner
    return func(ax, *args, **kwargs)
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/axes/_axes.py", line 1372, in plot
    for line in self._get_lines(*args, **kwargs):
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/axes/_base.py", line 404, in _grab_next_args
    for seg in self._plot_args(this, kwargs):
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/axes/_base.py", line 384, in _plot_args
    x, y = self._xy_from_xy(x, y)
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/axes/_base.py", line 243, in _xy_from_xy
    "have shapes {} and {}".format(x.shape, y.shape))
ValueError: x and y must have same first dimension, but have shapes (11,) and (1,)
>>> 
================= RESTART: /home/user/RTR105/Atvasinajums.py =================

================= RESTART: /home/user/RTR105/Atvasinajums.py =================

================= RESTART: /home/user/RTR105/Atvasinajums.py =================

================= RESTART: /home/user/RTR105/Atvasinajums.py =================

================= RESTART: /home/user/RTR105/Atvasinajums.py =================

================= RESTART: /home/user/RTR105/Atvasinajums.py =================
>>> 

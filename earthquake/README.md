
I really like the python language.
There are many powerful features of
the language that I didn't touch in this program.
However, I tried to demonstrate some of
the language features in this exercise:

- doc strings
- different ways of importing
- Object Oriented Programming
- exception handling
- packaging
- usage of private attributes
- temporary filename generation
- context manager protocol
- list comprehension
- reading json data from a website
- processing json data


1. sudo pip install geopy # install python package 'geopy'
2. mkdir /tmp/earthquake
3. copy the following files into /tmp/earthquake
   __init__.py
   earthquakes.py

4. chmod 755 /tmp/earthquake/__init__.py
   chmod 755 /tmp/earthquake/earthquakes.py

5. example interactive session (output is deleted for brevity)
   Note: cd /tmp
         or
         export PYTHONPATH=${PYTHONPATH}:/tmp

$ python
>>> import earthquake
>>> help(earthquake)
>>> dir(earthquake)
>>> help(earthquake.EarthQuakes)
>>> 
>>> address = 'San Francisco, CA 94128, USA'
>>> x = earthquake.EarthQuakes(address) # defaults: days = 7, distance = 100 miles
>>> x.max_magnitude()
>>> 
>>> x = earthquake.EarthQuakes(address, 3, 50) # days = 3, distance = 50 miles
>>> x.max_magnitude()


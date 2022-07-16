# numpy-redis

## Descrition

## Getting Started

### Installing

To install numpy-redis use:
```pip install numpy-redis```

### Storing a Numpy array in a Redis database

To store a Numpy array in a Redis database be sure to connect to the database with:
```r = redis.StrictRedis(host='localhost', port=12000, db=0)```

Then once you have a valid connection to a Redis instance, you can use:
```Array.create("array_name", array_value)```

### Deleting an array from the database

To delete a Numpy array from a redis database, use the following code:
```Array.delete("array_name")```

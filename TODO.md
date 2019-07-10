This is a pretty bare-bones distribution. I would want to add some stuff
before making it a real functioning package.

## 1. Error Handling

There is no exception handling right now. I would like to add try/except 
structures to each of the functions.

## 2. Testing

The `test.py` file is really more for showing how to use the functions
rather than really testing them. I would want to add some sort of unit test
structure to the package like nose.

## 3. Config keys

Right now the method of access/secret keys to AWS is pretty limitied. To run
the test file a `config.yml` file must be created in the root directory. I would
want to have some sort of command line script that saved the keys in enviorment
variables, or maybe just use the `aws configure` structure and read from those.

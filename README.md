# Technical test MDM

## Technical Test with Python

The goal of the exercise is to resolve the following problem:
https://www.hackerrank.com/challenges/sparse-
arrays/problem

### Environment

- Python
- Pytest library
- Docker

### Description of the code

The code is comprised of the following classes:

```
├── Dockerfile
├── main.py
├── README.md
├── test.py
└── util
    ├── RandomArrayGenerator.py
    └── SparseArray.py
```
- main.py: main programme (see below section to know how to run it)
- test.py: test class (see the **Tests** section below for more details on how to run it)
- util/RandomArrayGenerator.py: Class that generates a random string array (used to generate the `strings` array)
- util/SparseArray.py: Class containing the function that determines the number of query occurences 
(from the `queries` array) in the `strings` array

### Run the program

First, you have to be in the project folder:

```bash
cd technical-test-mdm
```

In order to run the code, run the following command:

```bash
python -m main QUERY_VALUES
```

Where QUERY_VALUES represent all the values of the `query` array.  
For instance, `QUERY_VALUES`= a bc de f  (Hence `query` = ['a', 'bc', 'de', 'f'])

Python command with the above example

```bash
python -m a bc de f
```

As indicated in the above section, the `strings` array is randomly generated. 
The result will be displayed in a dictionnary as shown in the below example:

```
{a: 2, bc: 1, de: 0, f: 0}
```

#### Run the program with Docker

Make sure you have docker installed: https://docs.docker.com/

Then run below commands to build the Docker image from the Dockerfile and run it:

```bash
docker build . -t test_mdm
docker run -t test_mdm a b c d e f g h
```

Note: You may have to run the command using `sudo` if you are not the user root 
or if your user doesn't belong to the `docker` group.

### Tests

#### Description

If you wish to see the existing tests, or to add more tests got to the `test.py` class.
We are using the `unittest` library.

To add a test, create a function test_[PURPOSE_OF_THE_TEST] where `PURPOSE_OF_THE_TEST` describes the type of test you realise. 

#### Run the tests

To run the tests using the ``pytest module, launch below command:

```bash
python -m pytest test.py
```
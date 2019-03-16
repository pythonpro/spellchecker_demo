# Simple spellchecker demo project 

Only Russian texts supported. Includes pipenv environment and Docker image creation instructions as well as pytest tests.

### Prerequisites for local (without Docker) installation

Requires `enchant` package to be installed on linux. Something like this:

```
# apt-get install enchant
```
and `pipenv` for python virtual environment creation:
```
# pip install pipenv
```

### Installing

```
$ pipenv install
```

### Activating python virtual environment

```
$ pipenv shell
```

### Running

```
$ python spellchecker.py
```

### Testing

```
$ pytest
```
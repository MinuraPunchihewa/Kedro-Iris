# Kedro Spaceflights Tutorial

This is an enhanced implementation of the Kedro Iris Starter project.

This implementation includes several extended features including,
* New nodes and pipelines
* Custom datasets
* Dataset injection
* Dataset versioning

## Run Locally

Clone the project,

```
git clone https://github.com/MinuraPunchihewa/kedro-iris.git
```

Go to the project directory,

```
cd kedro-iris
```

Install dependencies,

```
kedro install
```

Run the default pipeline,

```
kedro run
```

To run a pipeline of choice,
```
kedro run --pipeline <pipeline_name>
```

## Testing

Have a look at the file `src/tests/test_run.py` for instructions on how to write your tests. You can run your tests as follows:

```
kedro test
```

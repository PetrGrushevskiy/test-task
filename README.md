## Test task

###### Before running tests, you need to install the necessary packages:
>pip install -r requirements.txt

###### Than you can use the following commands to run tests:
- To run all API tests:

> pytest -m "api"

- To run all UI tests:

> pytest -m "ui"

- To run the specific test:

> pytest file_name::test_class_name::test_func_name
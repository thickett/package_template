This is a generic starting point for creating python packages.

**NOTE**: This template is designed to enable you to quickly create packages for your code, i.e if you have lots of functionality that you find your self copying around to different projects, or re-writing. Do not use this for larger projects where there are many contributors and is to be used by external consumers; we have no type checking, we do not check for duplication, we do not inspect the code or any other such actions as part of ci/cd.

### How to use

1. There are a number of variables that need changing, first go to `setup.py` in the root directory
    * at a minimum you should change the name, descriptions, and url. This is the information used by pypi, so if it is for a small personal package you could forgo this..
    * you should include all high-level package requirements that the **user** will need. i.e you dont need to include dev specific packages. i.e ruff, pytest etc
    * additonal downloadables can be added by adding `include_package_data=True` and `package_data={'file_to_include':'directory_to_file'}`
2.  The next thing to do is check if the github actions that are pre-defined meet your needs. currently there are just 2 (they can be seen at .github/workflows/):
    * **lint** This simply does ruff checks and fixes anything it finds. the changes, if there are any are automatically commited with a default commit message.
      * **NOTE**: I more or less always use ubuntu, if you are developing for a specific OS it would make sense to reflect that throughout these workflows.
      *  **NOTE**: I have the default python-version as 3.11 throughout the workflows, of course change this as is needed...
    * **publish**: This runs any tests you have in .tests/ using unittest. of course change this if you are using a different testing framework. This also includes the workflow for creating the binary and pushing it through to pypi, we use bump to auto itterate on versioning, remove this if you prefer to do it manually.
      * **NOTE** you must have set a `PYPI_TOKEN` secret in your repo secrets for this to work.

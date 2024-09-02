from setuptools import setup, find_packages

setup(
    name='INSERT NAME HERE', #
    version='0.1.0',
    packages=find_packages(),
    description='INSERT DESCRIPTION HERE', #
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Callum Thickett',
    author_email='callum.thickett@stepstone.com',
    url='INSERT REPO LINK HERE', #
    # include_package_data=True,
    # package_data={
    #     'ctgenerics':['config/sample_config.ini']
    # },
    install_requires=[
        'pandas~=2.2.2',
        'pydantic',
        'pyyaml'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

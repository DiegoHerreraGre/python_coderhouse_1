from setuptools import setup, find_packages

setup(
    name='Package',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django==4.2.11',
        'pytz==2021.3',
        'sqlparse==0.4.2',
    ],
    entry_points={
        'console_scripts': [
            'TareaPy = TareaPy.__main__:main'
        ]
    },
)
from setuptools import setup

setup(
    name='xkcd',
    version='0.1',
    py_modules=['xkcd'],
    install_requires=[
        'Click',
        'Pillow',
        'requests',
        'sh',
    ],
    entry_points='''
        [console_scripts]
        xkcd=xkcd:cli
    ''',
)

from os import path
from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='repldiscordpy',
    version='0.1.0',    
    long_description=long_description,
    long_description_content_type='text/markdown',
    description='This tool makes it easier for you to host your Discord.py bot for free using Repl.it and UptimeRobot!',
    url='https://github.com/nsde/repldiscordpy',
    author='onlix',
    author_email='neostyxde@gmail.com',
    license='MIT',
    packages=['repldiscordpy']   ,
    install_requires=['flask',
                      'requests',
                      ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',        
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
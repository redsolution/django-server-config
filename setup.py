# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

# Utility function to read the README file.  
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

setup(
    name="redsolutioncms.django-server-config",
    version=__import__('config').__version__,
    description=read('DESCRIPTION'),
    license="LGPL",
    keywords="django config lighttpd apache monit",

    author="Alexander Ivanov",
    author_email="alexander.ivanov@redsolution.ru",

    maintainer='Ivan Gromov',
    maintainer_email='ivan.gromov@redsolution.ru',

#    url="http://packages.python.org/django-server-config",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Framework :: Django',
        'Environment :: Web Environment',
        'Natural Language :: Russian',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],
    packages=find_packages(),
    install_requires=[],
    include_package_data=True,
    zip_safe=False,
    long_description=read('README'),
    entry_points={
        'redsolutioncms': ['config = config.redsolution_setup', ],
    }
)

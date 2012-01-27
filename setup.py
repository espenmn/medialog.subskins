from setuptools import setup, find_packages
import os

version = '4.2b14'
setup(name='medialog.subskins',
      version=version,
      description="An installable theme and theming tool for Plone 4",                
      long_description=open("README").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='web zope plone theme theming tool',
      author='Espen Moe-Nilssen',
      author_email='espen@medialog.no',       
      url='http://svn.plone.org/svn/collective/medialog.subskins',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['medialog'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plonetheme.classic',
          'Products.PloneSubSkins',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )

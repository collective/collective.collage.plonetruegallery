from setuptools import setup, find_packages
import os

version = '1.0-SNAPSHOT'

setup(name='collective.collage.plonetruegallery',
      version=version,
      description="Show a PloneTrueGallery slideshow in a Collage",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Kees Hink',
      author_email='hink@gw20e.com',
      url='http://plone.org/products/collective.collage.plonetruegallery',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.collage'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'collective.plonetruegallery',
          'Products.Collage',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )

from setuptools import setup, find_packages

version = '1.4'

setup(name='lazy',
      version=version,
      description='Lazy attributes for Python objects',
      long_description=open('README.rst').read() + '\n' +
                       open('CHANGES.rst').read(),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
      ],
      keywords='decorator lazy attribute property',
      author='Stefan H. Holek',
      author_email='stefan@epy.co.at',
      url='https://github.com/stefanholek/lazy',
      license='BSD-2-Clause',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=True,
      test_suite='lazy.tests',
)

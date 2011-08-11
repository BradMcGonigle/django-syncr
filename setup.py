from setuptools import setup, find_packages
 
setup(
    name='django-syncr',
    version='0.50',
    description='Synchronize Django with the web',
    author='Jesse Legg',
    author_email='jesse.legg@gmail.com',
    url='http://code.google.com/p/django-syncr',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
)

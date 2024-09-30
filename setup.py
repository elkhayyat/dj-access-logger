from setuptools import setup, find_packages

setup(
    name='dj-access-logger',
    version='1.0.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='A Django middleware for logging HTTP requests and responses.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/elkhayyat/dj-access-logger',
    author='AHMED ELKHAYYAT',
    author_email='elkhayyat.me@gmail.com',
    install_requires=[
        'Django>=3.0',
        'pymongo',
        'djongo',
        'mysqlclient',
        'psycopg2',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)

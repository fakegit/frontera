from os.path import dirname, join
from setuptools import setup


with open(join(dirname(__file__), 'crawlfrontier/VERSION'), 'rb') as f:
    version = f.read().decode('ascii').strip()


setup(
    name='crawl-frontier',
    packages=['crawlfrontier'],
    version=version,
    url='https://github.com/scrapinghub/crawl-frontier',
    description='A flexible frontier for web crawlers',
    long_description=open('README.md').read(),
    author='Scrapy developers',
    maintainer='Javier Casas',
    maintainer_email='javier@scrapinghub.com',
    license='BSD',
    include_package_data=True,
    zip_safe=False,
    keywords=['crawler', 'frontier', 'scrapy', 'web', 'requests'],
    classifiers=[
        'Framework :: Crawl Frontier',
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'SQLAlchemy>=0.9.8',
        'six>=1.8.0',
        'w3lib>=1.10.0',
        'tldextract>=1.5.1',
        'colorlog>=2.4.0',
        'pyparsing==1.5.7',
        'pydot==1.0.28',
    ],
)

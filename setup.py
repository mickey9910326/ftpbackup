from setuptools import setup, find_packages

REQUIREMENTS = [
    'pathspec',
]

setup(
    name='ftpbackup',
    version='0.1.0',
    description = 'Backup the folder to FTP!',
    long_description='',
    author = 'mickey9910326',
    author_email = 'mickey9910326@gmail.com',
    url='https://pypi.org/py_ASA_loader',
    license = 'MIT',
    packages=find_packages(),
    zip_safe=False,
    entry_points = {
        'console_scripts': [
            'ftpbk = ftpbackup.__main__:run',
        ],
    },
    install_requires=REQUIREMENTS
)

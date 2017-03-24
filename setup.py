import os
from distutils.core import setup

CLASSIFIERS = [
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Topic :: Software Development',
]

packages, data_files, install_requires = [], [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)
for dirpath, dirnames, filenames in os.walk('python_vlookup'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'):
            del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        prefix = dirpath[12:]  # Strip "python_vlookup/" or "python_vlookup\"
        for f in filenames:
            data_files.append(os.path.join(prefix, f))

setup(
    name='python_vlookup',
    packages=['python_vlookup'],
    version='2.0',
    description='A replica of VLOOKUP from Microsoft Excel, for Python',
    author='Christopher Scanlin',
    author_email='cscanlin@gmail.com',
    url='https://github.com/cscanlin/Super-Simple-VLOOKUP-in-Python',
    download_url='https://github.com/cscanlin/Super-Simple-VLOOKUP-in-Python/tarball/1.2',
    keywords=['python', 'excel', 'vlookup', 'string', 'search'],
    package_data={'python_vlookup': data_files},
    include_package_data=True,
    install_requires=install_requires,
    classifiers=CLASSIFIERS,
)

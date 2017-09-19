import setuptools
from gantt import __version__

setuptools.setup(
    name="minimal-gantt",
    author="Olav Vahtras",
    author_email="olav.vahtras@gmail.com",
    description="A minimal Gantt chart generator",
    license="MIT",
    version=__version__,
    py_modules=["gantt"],
    scripts=["csv2gantt"],
    install_requires=["pandas", "seaborn"],
    )
    

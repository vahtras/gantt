import setuptools

setuptools.setup(
    name="minimal-gantt",
    author="Olav Vahtras",
    author_email="olav.vahtras@gmail.com",
    description="A minimal Gantt chart generator",
    license="MIT",
    version="0.1",
    py_modules="gantt",
    install_requires=["pandas", "seaborn"],
    )
    

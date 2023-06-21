from setuptools import setup

setup(
    name='everylog_python_client',
    version='0.0.1',
    description='EveryLog provides a simple way to receive notifications for important application events that you choose.',
    install_requires=['requests'],
    author='Gasana Manzi David',
    author_email='david.gasana@devinterface.com'
    package_dir={'.': '/src/everylog_python_client'},
    py_modules=['everylog_python_client'],
    python_require=">=2.7",
    keywords=['everylog', 'log python', 'logging'],
    author_email='gasana.david@devinterface.com',
    license='MIT',
    )
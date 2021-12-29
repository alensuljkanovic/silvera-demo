from setuptools import setup

setup(
    name='pygen',
    version="0.0.1",
    description='Python code gen for Silvera tool',

    author='Alen Suljkanovic',
    author_email='alienized91@gmail.com',
    license='MIT',
    include_package_data=True,
    tests_require=[
        'pytest',
    ],
    keywords="microservices dsl generator compiler",
    entry_points={
        'silvera_generators': [
            # Java generator is built-in
            'python = pygen.generator:python',
        ],

        'silvera_evaluators': [
            # Java generator is built-in
            'myeval = pygen.evaluator:myeval',
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Interpreters',
        'Topic :: Software Development :: Compilers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        ]

)
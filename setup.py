# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
#                                                           #
#   This file was created by: Alberto Palomo Alonso         #
# Universidad de Alcalá - Escuela Politécnica Superior      #
#                                                           #
# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

REQUIREMENTS = ['numpy>=1.23.4',
                ]


setuptools.setup(
    name='pokrl',
    version='0.1.0',
    author='Palomo-Alonso, Alberto',
    author_email='a.palomo@edu.uah',
    description='PokRl: Your AI professor for playing Poker!',
    keywords='deeplearning, ml, poker',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/iTzAlver/pokrl.git',
    project_urls={
        'Documentation': 'https://htmlpreview.github.io/?https://github.com/iTzAlver/pokrl/blob/'
                         'main/doc/pokrl.html',
        'Bug Reports': 'https://github.com/iTzAlver/pokrl/issues',
        'Source Code': 'https://github.com/iTzAlver/pokrl.git',
        # 'Funding': '',
        # 'Say Thanks!': '',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        # see https://pypi.org/classifiers/
        'Development Status :: 5 - Production/Stable',

        'Topic :: Software Development :: Build Tools',

        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License'
    ],
    python_requires='>=3.11',
    # install_requires=['Pillow'],
    extras_require={
        'dev': ['check-manifest'],
    },
    include_package_data=True,
    install_requires=REQUIREMENTS
)
# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
#                        END OF FILE                        #
# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #

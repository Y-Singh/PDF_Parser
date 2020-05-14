
import setuptools

setuptools.setup(name='psp',
        version='1',
        description="Parses packing slips'n' stuff",
        author='Ellis Wright',
        author_email='ellisw@mastodondesign.com',
        packages=['psp'],
        zip_safe=False,
        install_requires=['pdfminer.six'])

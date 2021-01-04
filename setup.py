from setuptools import setup, find_packages


def readme():
    with open(r'README.md') as f:
        README = f.read()
    return README


def requirements():
    with open('requirements.txt', 'r') as f:
        req = f.read()
    return req

    setup(name='pygita',
          packages=find_packages(),
          version='1.0.0',
          license='MIT',
          description='''pygita is a wrapper
          of bhagavadgita.io api for Python 3''',
          author='Shubhendra Kushwaha',
          author_email='shubhendrakushwaha94@gmail.com',
          url='https://github.com/TheShubhendra/pygita',
          keywords=[
             'auth',
             'auth_token',
             'get_chapter',
             'get_verse',
          ],
          install_requires=requirements(),
          include_package_data=True,
          long_description=readme(),
          long_description_content_type="text/markdown",
          classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Build Tools',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
          ],
          python_requires='>=3.0',
          )

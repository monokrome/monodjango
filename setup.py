try:
    from setuptools import setup, find_packages
    from setuptools.command.test import test
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages
    from setuptools.command.test import test

setup(name = 'monodjango',
      description = 'A collection of django tools that I have created, which don't make sense as full projects.',
      author = 'Brandon R. Stoner',
      author_email = 'monokrome@monokro.me',
      version = '0.01',

      zip_safe = False,
      include_package_data = True,
      packages = ('monodjango',),
      url = 'http://github.com/monokrome/django-news/',

      classifiers = [
          "Development Status :: 4 - Beta",
          "Environment :: Web Environment",
          "Intended Audience :: Developers",
          "Operating System :: OS Independant",
          "Programming Language :: Python",
          "Framework :: Django",
          "Topic :: Internet :: WWW/HTTP / :: Site Management",
      ],
)


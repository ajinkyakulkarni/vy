#! /usr/bin/env python

from distutils.core import setup
from os.path import join

setup(name="vy",
      version="0.0.1",
      description="A vim-like in python made from scratch.",
      packages=["vyapp", 
                "vyapp.plugins",
                "vyapp.plugins.syntax",
                "vyapp.plugins.syntax.styles",
                "vyapp.plugins.omen",             
                "vyapp.plugins.jdb",
                "vyapp.plugins.pdb"],
      # package_dir={'vyapp':'vyapp'},
      scripts=['vy'],
      package_data={'vyapp': ['vyrc', join('vyapp', 'vyrc')]},
      author="Iury O. G. Figueiredo",
      author_email="ioliveira@id.uff.br",
      url='https://github.com/iogf/vy',
      download_url='https://github.com/iogf/vy/releases',
      keywords=['vy', 'vi', 'vim', 'emacs', 'sublime', 'atom', 'nano', 'vim-like'],
      classifiers=[])
 































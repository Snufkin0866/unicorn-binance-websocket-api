#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: setup.py
#
# Part of ‘UNICORN Binance WebSocket API’
# Project website: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api
# Documentation: https://oliver-zehentleitner.github.io/unicorn-binance-websocket-api
# PyPI: https://pypi.org/project/unicorn-binance-websocket-api/
#
# Author: Oliver Zehentleitner
#         https://about.me/oliver-zehentleitner
#
# Copyright (c) 2019, Oliver Zehentleitner
# All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='unicorn-binance-websocket-api',
     version='1.9.0.dev',
     author="Oliver Zehentleitner",
     url="https://about.me/oliver-zehentleitner/",
     scripts=['unicorn_binance_websocket_api.py'],
     description="A python API to use the Binance Websocket API's (com, com-margin, com-futures, jersey, us,"
                 " dex/chain+testnet) in a easy, fast, flexible, robust and fully-featured way.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     license='MIT License',
     install_requires=['colorama', 'pathlib', 'requests', 'websocket-client', 'websockets==7.0', 'flask_restful',
                       'cheroot', 'flask', 'simplejson'],
     keywords='binance, asyncio, async, asynchronous, concurrent, websocket-api, webstream-api, '
              'binance-websocket, binance-webstream, webstream, websocket, api, binance-jersey, binance-dex, '
              'binance-futures, binance-margin',
     project_urls={
        'Howto': 'https://www.technopathy.club/2019/11/02/howto-unicorn-binance-websocket-api/',
        'Documentation': 'https://oliver-zehentleitner.github.io/unicorn-binance-websocket-api/',
        'Wiki': 'https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/wiki',
        'Source': 'https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api',
     },
     python_requires='>=3.5.3',
     packages=setuptools.find_packages(),
     classifiers=[
         "Development Status :: 5 - Production/Stable",
         "Programming Language :: Python :: 3.5",
         "Programming Language :: Python :: 3.6",
         "Programming Language :: Python :: 3.7",
         "Programming Language :: Python :: 3.8",
         "License :: OSI Approved :: MIT License",
         'Intended Audience :: Developers',
         "Intended Audience :: Financial and Insurance Industry",
         "Intended Audience :: Information Technology",
         "Intended Audience :: Science/Research",
         "Operating System :: OS Independent",
         "Topic :: Office/Business :: Financial :: Investment",
         'Topic :: Software Development :: Libraries :: Python Modules',
         "Framework :: AsyncIO",
     ],
)

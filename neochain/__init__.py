#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This package helps to detect communities in blockchain transaction data
by using well known community detection algorithms and also can observe
evolution in blockchain network by observing changes in communities in
blockchain

To install: python setup.py install
To use: import neochain as nc
"""


# Source code meta data
__author__ = 'Dalwar Hossain'
__email__ = 'dalwar.hossain@protonmail.com'


# Handle imports
from nc_community_handler import find_communities, find_top_n_communities
from nc_graph_handler import generate_merged_graph


# Version
__version__ = 1.0

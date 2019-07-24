# straight_line_dist.py
# Implementation of straight line distance algorithm using balltree
# Author: Adam Munawar Rahman

from .csv_utils import *
from .nn_utils import *
import sys
import os


def straight_line_distance(src_tagged_points, tgt_tagged_points, tgt_properties=[]):
    """
    Given a set of source coordinates and a set of tagged target coordinates, 
    and an optional list of target properties:

    Determines the nearest target site for each source site, and outputs
    a list of tuples indexed to the source sites, where for each source site,
    the corresponding tuple:
    (straight line distance to nearest target site, 
     target site identifier,
     <additional properties of target site specified by tgt_properties>)
    """

    src_points = [(float(tagged_vector[0][0]), float(tagged_vector[0][1]))
                  for tagged_vector in src_tagged_points]
    tgt_points = [(float(tagged_vector[0][0]), float(tagged_vector[0][1]))
                  for tagged_vector in tgt_tagged_points]
    # Uses balltree implementation to return distances to neighbors in meters, calculated with haversine
    nn_indices_and_dists = get_nearest_neighbors(src_points, tgt_points, 1)
    straight_line_dist_data = []
    for ix_and_dist in nn_indices_and_dists:
        ix, dist = ix_and_dist[0]
        tgt_info = tgt_tagged_points[ix]
        info_tuple = (dist, )
        for property in tgt_info[1:]:
            info_tuple += (property, )
        straight_line_dist_data.append(info_tuple)

    print("Completed nearest site calculation for {0} source sites!".format(
        len(src_points)))

    return(straight_line_dist_data)

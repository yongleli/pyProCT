'''
Created on 09/01/2013

@author: victor
'''
import numpy

class CohesionAndSeparationCalculator(object):
    
    def __init__(self):
        pass
    
    def cluster_cohesion(self, cluster, clusterization, clustering_cohesion, condensed_distance_matrix):
        """
        Returns the cohesion plus separation value of a cluster. The condensed matrix 
        given as parameter stores the distances of the elements of the dataset used to 
        extract the cluster.
        """
        if clustering_cohesion > 0:
            weight = 1./clustering_cohesion
            sep_and_cohe = 0.0
            ## I'm inside?
            where_am_i = clusterization.cluster_index(cluster)
            
            for i in range(len(clusterization.clusters)):    
                if i != where_am_i :
                    c_j = clusterization.clusters[i]
                    sep_and_cohe = sep_and_cohe + self.__clusters_mixed_cohesion(cluster,c_j,condensed_distance_matrix)
            return weight*sep_and_cohe
        else:
            return numpy.finfo(numpy.float32).max
    
    def __clusters_mixed_cohesion(self,cluster_1,cluster_2,condensed_distance_matrix):
        """
        Calculates the 'cohesion' of one cluster vs other.
        Precondition: Clusters don't have shared elements.
        """
        mixed_cohesion = 0
        for c_i in cluster_1.all_elements:
            for c_j in cluster_2.all_elements:
                mixed_cohesion = mixed_cohesion + condensed_distance_matrix[c_i,c_j]
        return mixed_cohesion
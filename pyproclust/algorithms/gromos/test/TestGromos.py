'''
Created on 15/02/2012

@author: victor
'''
import unittest
import pyproclust.algorithms.gromos.gromosAlgorithmTools as grt
from pyproclust.matrix.condensedMatrix import CondensedDistanceMatrix
from pyproclust.clustering.cluster import cluster_from_tuple, Cluster
from pyproclust.algorithms.gromos.gromosAlgorithm import GromosAlgorithm

class Test(unittest.TestCase):

    def test_intermediate_iteration_1(self):
        """
        Replication of an intermediate result from an actual run.
        """
        condensed_matrix = CondensedDistanceMatrix([2.2360679774997898, 2.2360679774997898, 3.6055512754639891, 31.144823004794873, 4.2426406871192848, 33.241540277189323, 4.0, 28.442925306655784, 6.4031242374328485, 34.525353003264136, 6.7082039324993694, 6.0827625302982193, 32.756678708318397, 29.832867780352597, 23.086792761230392, 17.464249196572979, 35.902646142032481, 29.732137494637012, 33.837848631377263, 31.016124838541646, 20.124611797498108, 25.0, 21.095023109728988, 23.086792761230392, 22.360679774997898, 29.832867780352597, 24.186773244895647, 25.709920264364882, 28.792360097775937, 32.649655434629018, 32.140317359976393, 36.055512754639892, 34.713109915419565, 35.227829907617071, 36.013886210738214, 36.013886210738214, 3.1622776601683795, 5.0990195135927845, 29.068883707497267, 2.2360679774997898, 31.144823004794873, 3.6055512754639891, 26.305892875931811, 7.2111025509279782, 32.388269481403292, 5.0990195135927845, 5.8309518948453007, 30.594117081556711, 27.658633371878661, 20.880613017821101, 15.231546211727817, 33.734255586865999, 27.513632984395208, 31.622776601683793, 28.792360097775937, 18.384776310850235, 23.021728866442675, 20.0, 21.587033144922902, 21.095023109728988, 27.802877548915689, 23.021728866442675, 24.331050121192877, 27.202941017470888, 30.870698080866262, 31.016124838541646, 34.481879299133332, 33.376638536557273, 34.058772731852805, 35.014282800023196, 35.128336140500593, 2.0, 32.015621187164243, 4.1231056256176606, 34.058772731852805, 2.2360679774997898, 29.154759474226502, 4.2426406871192848, 35.227829907617071, 5.6568542494923806, 4.0, 33.376638536557273, 30.413812651491099, 23.53720459187964, 17.720045146669349, 36.496575181789318, 30.083217912982647, 34.205262752974143, 31.32091952673165, 18.867962264113206, 24.083189157584592, 19.235384061671343, 21.540659228538015, 20.615528128088304, 29.0, 22.360679774997898, 24.041630560342615, 27.313000567495326, 31.384709652950431, 30.265491900843113, 34.539832078341085, 32.984845004941285, 33.376638536557273, 34.058772731852805, 34.0, 34.014702703389901, 6.0827625302982193, 36.055512754639892, 3.6055512754639891, 31.144823004794873, 3.1622776601683795, 37.215588131856791, 7.2111025509279782, 4.4721359549995796, 35.355339059327378, 32.388269481403292, 25.495097567963924, 19.646882704388499, 38.470768123342687, 32.015621187164243, 36.138621999185304, 33.241540277189323, 20.0, 25.45584412271571, 19.646882704388499, 22.360679774997898, 21.189620100417091, 30.413812651491099, 22.803508501982758, 24.698178070456937, 28.178005607210743, 32.449961479175904, 30.594117081556711, 35.341194094144583, 33.526109228480422, 33.734255586865999, 34.23448553724738, 34.058772731852805, 28.0, 2.2360679774997898, 31.016124838541646, 3.6055512754639891, 35.057096285916209, 4.2426406871192848, 28.160255680657446, 32.140317359976393, 4.1231056256176606, 4.4721359549995796, 9.8488578017961039, 15.524174696260024, 6.4031242374328485, 7.6157731058639087, 8.0622577482985491, 8.2462112512353212, 26.627053911388696, 23.345235059857504, 34.132096331752024, 30.610455730027933, 33.015148038438355, 23.323807579381203, 35.0, 33.301651610693426, 31.89043743820395, 30.528675044947494, 40.311288741492746, 36.359317925395686, 39.204591567825318, 41.868842830916641, 44.598206241955516, 45.967379738244816, 30.016662039607269, 3.1622776601683795, 25.079872407968907, 7.2801098892805181, 31.144823004794873, 3.0, 5.0, 29.274562336608895, 26.305892875931811, 19.416487838947599, 13.601470508735444, 32.388269481403292, 25.96150997149434, 30.083217912982647, 27.202941017470888, 16.15549442140351, 20.808652046684813, 18.027756377319946, 19.416487838947599, 19.026297590440446, 25.612496949731394, 21.0, 22.203603311174518, 25.0, 28.635642126552707, 29.0, 32.280024783137947, 31.256999216175569, 32.015621187164243, 33.060550509633082, 33.241540277189323, 33.0, 5.0990195135927845, 37.013511046643494, 2.2360679774997898, 30.066592756745816, 34.058772731852805, 3.1622776601683795, 5.0, 11.401754250991379, 17.262676501632068, 4.4721359549995796, 7.810249675906654, 7.0710678118654755, 8.0622577482985491, 27.784887978899608, 24.083189157584592, 35.355339059327378, 31.622776601683793, 34.132096331752024, 23.600847442411894, 36.055512754639892, 34.205262752974143, 32.526911934581186, 30.805843601498726, 41.036569057366385, 36.61966684720111, 39.698866482558415, 42.449970553582247, 45.254833995939045, 46.690470119715009, 28.0178514522438, 4.1231056256176606, 34.058772731852805, 3.6055512754639891, 2.2360679774997898, 32.140317359976393, 29.154759474226502, 22.203603311174518, 16.278820596099706, 35.227829907617071, 28.635642126552707, 32.756678708318397, 29.832867780352597, 16.643316977093239, 21.931712199461309, 17.11724276862369, 19.313207915827967, 18.439088914585774, 26.870057685088806, 20.223748416156685, 21.840329667841555, 25.079872407968907, 29.154759474226502, 28.160255680657446, 32.310988842807021, 30.805843601498726, 31.256999216175569, 32.015621187164243, 32.015621187164243, 32.0, 6.0827625302982193, 25.019992006393608, 29.017236257093817, 4.4721359549995796, 2.2360679774997898, 6.324555320336759, 12.165525060596439, 7.6157731058639087, 5.0, 7.2111025509279782, 6.0827625302982193, 23.021728866442675, 19.849433241279208, 30.528675044947494, 27.018512172212592, 29.410882339705484, 20.124611797498108, 31.400636936215164, 29.732137494637012, 28.42534080710379, 27.294688127912362, 36.796738985948195, 33.120990323358392, 35.805027579936315, 38.418745424597091, 41.109609582188931, 42.449970553582247, 38.013155617496423, 7.0710678118654755, 3.1622776601683795, 36.055512754639892, 33.060550509633082, 26.076809620810597, 20.09975124224178, 39.11521443121589, 32.388269481403292, 36.496575181789318, 33.541019662496844, 18.384776310850235, 24.207436873820409, 17.088007490635061, 20.248456731316587, 18.788294228055936, 29.206163733020468, 20.248456731316587, 22.360679774997898, 26.076809620810597, 30.610455730027933, 27.892651361962706, 33.120990323358392, 31.016124838541646, 31.048349392520048, 31.400636936215164, 31.144823004794873, 31.0, 35.0, 2.2360679774997898, 5.0990195135927845, 12.041594578792296, 18.027756377319946, 2.2360679774997898, 7.2111025509279782, 5.3851648071345037, 7.0710678118654755, 27.730849247724095, 23.600847442411894, 35.341194094144583, 31.384709652950431, 34.0, 22.671568097509269, 35.846896657869841, 33.837848631377263, 31.89043743820395, 29.832867780352597, 40.459856648287818, 35.608987629529715, 38.897300677553446, 41.725292090050132, 44.598206241955516, 46.097722286464439, 4.0, 29.017236257093817, 26.019223662515376, 19.026297590440446, 13.038404810405298, 32.062439083762797, 25.317977802344327, 29.427877939124322, 26.476404589747453, 13.416407864998739, 18.439088914585774, 15.033296378372908, 16.492422502470642, 16.031219541881399, 23.345235059857504, 18.0, 19.235384061671343, 22.135943621178654, 25.942243542145693, 26.0, 29.410882339705484, 28.284271247461902, 29.017236257093817, 30.066592756745816, 30.265491900843113, 33.015148038438355, 30.016662039607269, 23.021728866442675, 17.029386365926403, 36.055512754639892, 29.274562336608895, 33.376638536557273, 30.413812651491099, 15.620499351813308, 21.2602916254693, 15.297058540778355, 17.888543819998318, 16.763054614240211, 26.248809496813376, 18.439088914585774, 20.248456731316587, 23.706539182259394, 28.0178514522438, 26.305892875931811, 30.870698080866262, 29.120439557122072, 29.427877939124322, 30.066592756745816, 30.0, 3.0, 10.0, 16.0, 3.1622776601683795, 5.0, 4.0, 5.0, 25.495097567963924, 21.400934559032695, 33.105890714493697, 29.154759474226502, 31.76476034853718, 20.615528128088304, 33.61547262794322, 31.622776601683793, 29.732137494637012, 27.802877548915689, 38.288379438153292, 33.600595232822883, 36.796738985948195, 39.597979746446661, 42.449970553582247, 43.931765272977593, 7.0, 13.0, 6.0827625302982193, 3.1622776601683795, 5.0, 4.0, 22.825424421026653, 19.104973174542799, 30.413812651491099, 26.627053911388696, 29.154759474226502, 18.867962264113206, 31.064449134018133, 29.206163733020468, 27.586228448267445, 26.076809620810597, 36.069377593742864, 31.906112267087632, 34.828149534535996, 37.536648758246919, 40.311288741492746, 41.725292090050132, 6.0, 13.038404810405298, 6.7082039324993694, 10.770329614269007, 8.0622577482985491, 17.029386365926403, 14.7648230602334, 24.413111231467404, 21.213203435596427, 23.430749027719962, 16.278820596099706, 25.495097567963924, 24.083189157584592, 23.323807579381203, 23.086792761230392, 31.400636936215164, 28.792360097775937, 30.886890422961002, 33.286633954186478, 35.805027579936315, 37.013511046643494, 19.026297590440446, 12.369316876852981, 16.492422502470642, 13.601470508735444, 13.038404810405298, 13.038404810405298, 19.798989873223331, 17.4928556845359, 19.209372712298546, 16.278820596099706, 21.400934559032695, 20.591260281974002, 20.880613017821101, 22.022715545545239, 28.178005607210743, 27.294688127912362, 28.460498941515414, 30.463092423455635, 32.649655434629018, 33.61547262794322, 7.2801098892805181, 4.2426406871192848, 6.7082039324993694, 27.856776554368238, 23.323807579381203, 35.468295701936398, 31.304951684997057, 34.014702703389901, 21.931712199461309, 35.777087639996637, 33.61547262794322, 31.400636936215164, 29.0, 40.0, 34.713109915419565, 38.209946349085598, 41.109609582188931, 44.045431091090478, 45.607017003965517, 4.1231056256176606, 1.4142135623730951, 20.615528128088304, 16.401219466856727, 28.231188426986208, 24.186773244895647, 26.832815729997478, 15.811388300841896, 28.653097563788805, 26.627053911388696, 24.758836806279895, 23.021728866442675, 33.301651610693426, 28.844410203711913, 31.89043743820395, 34.655446902326915, 37.483329627982627, 38.948684188300895, 3.0, 24.041630560342615, 19.235384061671343, 31.622776601683793, 27.313000567495326, 30.083217912982647, 17.691806012954132, 31.780497164141408, 29.529646120466801, 27.202941017470888, 24.758836806279895, 35.805027579936315, 30.479501308256342, 33.97057550292606, 36.878177829171548, 39.824615503479755, 41.400483088968905, 21.189620100417091, 16.643316977093239, 28.792360097775937, 24.596747752497688, 27.313000567495326, 15.620499351813308, 29.068883707497267, 26.92582403567252, 24.839484696748443, 22.803508501982758, 33.421549934136806, 28.600699292150182, 31.827660925679098, 34.655446902326915, 37.536648758246919, 39.05124837953327, 6.324555320336759, 7.6157731058639087, 4.4721359549995796, 6.4031242374328485, 11.180339887498949, 8.4852813742385695, 7.6157731058639087, 9.0553851381374173, 12.529964086141668, 15.231546211727817, 16.278820596099706, 16.124515496597098, 17.720045146669349, 19.697715603592208, 20.591260281974002, 13.038404810405298, 8.2462112512353212, 11.180339887498949, 5.0, 12.649110640673518, 10.295630140987001, 8.6023252670426267, 9.0, 16.970562748477139, 14.317821063276353, 16.124515496597098, 18.601075237738275, 21.2602916254693, 22.627416997969522, 5.0990195135927845, 2.2360679774997898, 17.11724276862369, 3.1622776601683795, 5.6568542494923806, 10.0, 15.264337522473747, 11.045361017187261, 16.401219466856727, 13.928388277184119, 14.142135623730951, 15.033296378372908, 15.297058540778355, 3.0, 12.041594578792296, 4.4721359549995796, 3.1622776601683795, 5.8309518948453007, 10.63014581273465, 10.770329614269007, 13.0, 12.0, 13.341664064126334, 15.231546211727817, 16.124515496597098, 15.033296378372908, 2.2360679774997898, 3.6055512754639891, 7.810249675906654, 13.038404810405298, 10.04987562112089, 14.422205101855956, 12.369316876852981, 13.0, 14.317821063276353, 14.866068747318506, 16.031219541881399, 13.152946437965905, 9.8488578017961039, 7.2111025509279782, 18.357559750685819, 13.038404810405298, 16.278820596099706, 19.209372712298546, 22.203603311174518, 23.853720883753127, 3.1622776601683795, 7.6157731058639087, 13.0, 8.0, 13.45362404707371, 10.770329614269007, 11.045361017187261, 12.165525060596439, 12.649110640673518, 4.4721359549995796, 9.8488578017961039, 7.6157731058639087, 10.816653826391969, 9.0553851381374173, 10.198039027185569, 12.083045973594572, 13.038404810405298, 5.3851648071345037, 8.6023252670426267, 7.2801098892805181, 7.6157731058639087, 10.0, 12.727922061357855, 14.212670403551895, 12.369316876852981, 5.8309518948453007, 9.4339811320566032, 12.529964086141668, 15.652475842498529, 17.464249196572979, 9.2195444572928871, 4.4721359549995796, 3.1622776601683795, 4.4721359549995796, 5.6568542494923806, 5.0, 8.0622577482985491, 11.180339887498949, 13.152946437965905, 3.1622776601683795, 6.324555320336759, 8.2462112512353212, 3.1622776601683795, 5.0990195135927845, 2.0])
        remaining_nodes = [4, 8, 9, 15, 16, 18, 20, 21, 22, 26, 29, 30, 32, 36]
        clustered_nodes = [7, 0, 1, 2, 3, 5, 11, 12, 13, 6, 10, 14, 17, 19, 25, 23, 24, 27, 28, 34, 31, 33, 35]
        (node, len_neig) = grt.choose_node_with_higher_cardinality(condensed_matrix,remaining_nodes,4.0)
        self.assertEqual(len_neig,1)
        self.assertNotIn(node, clustered_nodes)
        neigbours = grt.get_neighbors_for_node(condensed_matrix,node,remaining_nodes,4.0)
        self.assertEqual(len(neigbours),len_neig)
        expected_neightbours = [8]
        for i in range(len(neigbours)):
            self.assertEqual(neigbours[i],expected_neightbours[i])
        
        
    def test_intermediate_iteration_2(self):
        """
        One iteration of the algorithm
        """
        remaining_nodes = [4, 8, 9, 15, 16, 18, 20, 21, 22, 26, 29, 30, 32, 36]
        condensed_matrix = CondensedDistanceMatrix([2.2360679774997898, 2.2360679774997898, 3.6055512754639891, 31.144823004794873, 4.2426406871192848, 33.241540277189323, 4.0, 28.442925306655784, 6.4031242374328485, 34.525353003264136, 6.7082039324993694, 6.0827625302982193, 32.756678708318397, 29.832867780352597, 23.086792761230392, 17.464249196572979, 35.902646142032481, 29.732137494637012, 33.837848631377263, 31.016124838541646, 20.124611797498108, 25.0, 21.095023109728988, 23.086792761230392, 22.360679774997898, 29.832867780352597, 24.186773244895647, 25.709920264364882, 28.792360097775937, 32.649655434629018, 32.140317359976393, 36.055512754639892, 34.713109915419565, 35.227829907617071, 36.013886210738214, 36.013886210738214, 3.1622776601683795, 5.0990195135927845, 29.068883707497267, 2.2360679774997898, 31.144823004794873, 3.6055512754639891, 26.305892875931811, 7.2111025509279782, 32.388269481403292, 5.0990195135927845, 5.8309518948453007, 30.594117081556711, 27.658633371878661, 20.880613017821101, 15.231546211727817, 33.734255586865999, 27.513632984395208, 31.622776601683793, 28.792360097775937, 18.384776310850235, 23.021728866442675, 20.0, 21.587033144922902, 21.095023109728988, 27.802877548915689, 23.021728866442675, 24.331050121192877, 27.202941017470888, 30.870698080866262, 31.016124838541646, 34.481879299133332, 33.376638536557273, 34.058772731852805, 35.014282800023196, 35.128336140500593, 2.0, 32.015621187164243, 4.1231056256176606, 34.058772731852805, 2.2360679774997898, 29.154759474226502, 4.2426406871192848, 35.227829907617071, 5.6568542494923806, 4.0, 33.376638536557273, 30.413812651491099, 23.53720459187964, 17.720045146669349, 36.496575181789318, 30.083217912982647, 34.205262752974143, 31.32091952673165, 18.867962264113206, 24.083189157584592, 19.235384061671343, 21.540659228538015, 20.615528128088304, 29.0, 22.360679774997898, 24.041630560342615, 27.313000567495326, 31.384709652950431, 30.265491900843113, 34.539832078341085, 32.984845004941285, 33.376638536557273, 34.058772731852805, 34.0, 34.014702703389901, 6.0827625302982193, 36.055512754639892, 3.6055512754639891, 31.144823004794873, 3.1622776601683795, 37.215588131856791, 7.2111025509279782, 4.4721359549995796, 35.355339059327378, 32.388269481403292, 25.495097567963924, 19.646882704388499, 38.470768123342687, 32.015621187164243, 36.138621999185304, 33.241540277189323, 20.0, 25.45584412271571, 19.646882704388499, 22.360679774997898, 21.189620100417091, 30.413812651491099, 22.803508501982758, 24.698178070456937, 28.178005607210743, 32.449961479175904, 30.594117081556711, 35.341194094144583, 33.526109228480422, 33.734255586865999, 34.23448553724738, 34.058772731852805, 28.0, 2.2360679774997898, 31.016124838541646, 3.6055512754639891, 35.057096285916209, 4.2426406871192848, 28.160255680657446, 32.140317359976393, 4.1231056256176606, 4.4721359549995796, 9.8488578017961039, 15.524174696260024, 6.4031242374328485, 7.6157731058639087, 8.0622577482985491, 8.2462112512353212, 26.627053911388696, 23.345235059857504, 34.132096331752024, 30.610455730027933, 33.015148038438355, 23.323807579381203, 35.0, 33.301651610693426, 31.89043743820395, 30.528675044947494, 40.311288741492746, 36.359317925395686, 39.204591567825318, 41.868842830916641, 44.598206241955516, 45.967379738244816, 30.016662039607269, 3.1622776601683795, 25.079872407968907, 7.2801098892805181, 31.144823004794873, 3.0, 5.0, 29.274562336608895, 26.305892875931811, 19.416487838947599, 13.601470508735444, 32.388269481403292, 25.96150997149434, 30.083217912982647, 27.202941017470888, 16.15549442140351, 20.808652046684813, 18.027756377319946, 19.416487838947599, 19.026297590440446, 25.612496949731394, 21.0, 22.203603311174518, 25.0, 28.635642126552707, 29.0, 32.280024783137947, 31.256999216175569, 32.015621187164243, 33.060550509633082, 33.241540277189323, 33.0, 5.0990195135927845, 37.013511046643494, 2.2360679774997898, 30.066592756745816, 34.058772731852805, 3.1622776601683795, 5.0, 11.401754250991379, 17.262676501632068, 4.4721359549995796, 7.810249675906654, 7.0710678118654755, 8.0622577482985491, 27.784887978899608, 24.083189157584592, 35.355339059327378, 31.622776601683793, 34.132096331752024, 23.600847442411894, 36.055512754639892, 34.205262752974143, 32.526911934581186, 30.805843601498726, 41.036569057366385, 36.61966684720111, 39.698866482558415, 42.449970553582247, 45.254833995939045, 46.690470119715009, 28.0178514522438, 4.1231056256176606, 34.058772731852805, 3.6055512754639891, 2.2360679774997898, 32.140317359976393, 29.154759474226502, 22.203603311174518, 16.278820596099706, 35.227829907617071, 28.635642126552707, 32.756678708318397, 29.832867780352597, 16.643316977093239, 21.931712199461309, 17.11724276862369, 19.313207915827967, 18.439088914585774, 26.870057685088806, 20.223748416156685, 21.840329667841555, 25.079872407968907, 29.154759474226502, 28.160255680657446, 32.310988842807021, 30.805843601498726, 31.256999216175569, 32.015621187164243, 32.015621187164243, 32.0, 6.0827625302982193, 25.019992006393608, 29.017236257093817, 4.4721359549995796, 2.2360679774997898, 6.324555320336759, 12.165525060596439, 7.6157731058639087, 5.0, 7.2111025509279782, 6.0827625302982193, 23.021728866442675, 19.849433241279208, 30.528675044947494, 27.018512172212592, 29.410882339705484, 20.124611797498108, 31.400636936215164, 29.732137494637012, 28.42534080710379, 27.294688127912362, 36.796738985948195, 33.120990323358392, 35.805027579936315, 38.418745424597091, 41.109609582188931, 42.449970553582247, 38.013155617496423, 7.0710678118654755, 3.1622776601683795, 36.055512754639892, 33.060550509633082, 26.076809620810597, 20.09975124224178, 39.11521443121589, 32.388269481403292, 36.496575181789318, 33.541019662496844, 18.384776310850235, 24.207436873820409, 17.088007490635061, 20.248456731316587, 18.788294228055936, 29.206163733020468, 20.248456731316587, 22.360679774997898, 26.076809620810597, 30.610455730027933, 27.892651361962706, 33.120990323358392, 31.016124838541646, 31.048349392520048, 31.400636936215164, 31.144823004794873, 31.0, 35.0, 2.2360679774997898, 5.0990195135927845, 12.041594578792296, 18.027756377319946, 2.2360679774997898, 7.2111025509279782, 5.3851648071345037, 7.0710678118654755, 27.730849247724095, 23.600847442411894, 35.341194094144583, 31.384709652950431, 34.0, 22.671568097509269, 35.846896657869841, 33.837848631377263, 31.89043743820395, 29.832867780352597, 40.459856648287818, 35.608987629529715, 38.897300677553446, 41.725292090050132, 44.598206241955516, 46.097722286464439, 4.0, 29.017236257093817, 26.019223662515376, 19.026297590440446, 13.038404810405298, 32.062439083762797, 25.317977802344327, 29.427877939124322, 26.476404589747453, 13.416407864998739, 18.439088914585774, 15.033296378372908, 16.492422502470642, 16.031219541881399, 23.345235059857504, 18.0, 19.235384061671343, 22.135943621178654, 25.942243542145693, 26.0, 29.410882339705484, 28.284271247461902, 29.017236257093817, 30.066592756745816, 30.265491900843113, 33.015148038438355, 30.016662039607269, 23.021728866442675, 17.029386365926403, 36.055512754639892, 29.274562336608895, 33.376638536557273, 30.413812651491099, 15.620499351813308, 21.2602916254693, 15.297058540778355, 17.888543819998318, 16.763054614240211, 26.248809496813376, 18.439088914585774, 20.248456731316587, 23.706539182259394, 28.0178514522438, 26.305892875931811, 30.870698080866262, 29.120439557122072, 29.427877939124322, 30.066592756745816, 30.0, 3.0, 10.0, 16.0, 3.1622776601683795, 5.0, 4.0, 5.0, 25.495097567963924, 21.400934559032695, 33.105890714493697, 29.154759474226502, 31.76476034853718, 20.615528128088304, 33.61547262794322, 31.622776601683793, 29.732137494637012, 27.802877548915689, 38.288379438153292, 33.600595232822883, 36.796738985948195, 39.597979746446661, 42.449970553582247, 43.931765272977593, 7.0, 13.0, 6.0827625302982193, 3.1622776601683795, 5.0, 4.0, 22.825424421026653, 19.104973174542799, 30.413812651491099, 26.627053911388696, 29.154759474226502, 18.867962264113206, 31.064449134018133, 29.206163733020468, 27.586228448267445, 26.076809620810597, 36.069377593742864, 31.906112267087632, 34.828149534535996, 37.536648758246919, 40.311288741492746, 41.725292090050132, 6.0, 13.038404810405298, 6.7082039324993694, 10.770329614269007, 8.0622577482985491, 17.029386365926403, 14.7648230602334, 24.413111231467404, 21.213203435596427, 23.430749027719962, 16.278820596099706, 25.495097567963924, 24.083189157584592, 23.323807579381203, 23.086792761230392, 31.400636936215164, 28.792360097775937, 30.886890422961002, 33.286633954186478, 35.805027579936315, 37.013511046643494, 19.026297590440446, 12.369316876852981, 16.492422502470642, 13.601470508735444, 13.038404810405298, 13.038404810405298, 19.798989873223331, 17.4928556845359, 19.209372712298546, 16.278820596099706, 21.400934559032695, 20.591260281974002, 20.880613017821101, 22.022715545545239, 28.178005607210743, 27.294688127912362, 28.460498941515414, 30.463092423455635, 32.649655434629018, 33.61547262794322, 7.2801098892805181, 4.2426406871192848, 6.7082039324993694, 27.856776554368238, 23.323807579381203, 35.468295701936398, 31.304951684997057, 34.014702703389901, 21.931712199461309, 35.777087639996637, 33.61547262794322, 31.400636936215164, 29.0, 40.0, 34.713109915419565, 38.209946349085598, 41.109609582188931, 44.045431091090478, 45.607017003965517, 4.1231056256176606, 1.4142135623730951, 20.615528128088304, 16.401219466856727, 28.231188426986208, 24.186773244895647, 26.832815729997478, 15.811388300841896, 28.653097563788805, 26.627053911388696, 24.758836806279895, 23.021728866442675, 33.301651610693426, 28.844410203711913, 31.89043743820395, 34.655446902326915, 37.483329627982627, 38.948684188300895, 3.0, 24.041630560342615, 19.235384061671343, 31.622776601683793, 27.313000567495326, 30.083217912982647, 17.691806012954132, 31.780497164141408, 29.529646120466801, 27.202941017470888, 24.758836806279895, 35.805027579936315, 30.479501308256342, 33.97057550292606, 36.878177829171548, 39.824615503479755, 41.400483088968905, 21.189620100417091, 16.643316977093239, 28.792360097775937, 24.596747752497688, 27.313000567495326, 15.620499351813308, 29.068883707497267, 26.92582403567252, 24.839484696748443, 22.803508501982758, 33.421549934136806, 28.600699292150182, 31.827660925679098, 34.655446902326915, 37.536648758246919, 39.05124837953327, 6.324555320336759, 7.6157731058639087, 4.4721359549995796, 6.4031242374328485, 11.180339887498949, 8.4852813742385695, 7.6157731058639087, 9.0553851381374173, 12.529964086141668, 15.231546211727817, 16.278820596099706, 16.124515496597098, 17.720045146669349, 19.697715603592208, 20.591260281974002, 13.038404810405298, 8.2462112512353212, 11.180339887498949, 5.0, 12.649110640673518, 10.295630140987001, 8.6023252670426267, 9.0, 16.970562748477139, 14.317821063276353, 16.124515496597098, 18.601075237738275, 21.2602916254693, 22.627416997969522, 5.0990195135927845, 2.2360679774997898, 17.11724276862369, 3.1622776601683795, 5.6568542494923806, 10.0, 15.264337522473747, 11.045361017187261, 16.401219466856727, 13.928388277184119, 14.142135623730951, 15.033296378372908, 15.297058540778355, 3.0, 12.041594578792296, 4.4721359549995796, 3.1622776601683795, 5.8309518948453007, 10.63014581273465, 10.770329614269007, 13.0, 12.0, 13.341664064126334, 15.231546211727817, 16.124515496597098, 15.033296378372908, 2.2360679774997898, 3.6055512754639891, 7.810249675906654, 13.038404810405298, 10.04987562112089, 14.422205101855956, 12.369316876852981, 13.0, 14.317821063276353, 14.866068747318506, 16.031219541881399, 13.152946437965905, 9.8488578017961039, 7.2111025509279782, 18.357559750685819, 13.038404810405298, 16.278820596099706, 19.209372712298546, 22.203603311174518, 23.853720883753127, 3.1622776601683795, 7.6157731058639087, 13.0, 8.0, 13.45362404707371, 10.770329614269007, 11.045361017187261, 12.165525060596439, 12.649110640673518, 4.4721359549995796, 9.8488578017961039, 7.6157731058639087, 10.816653826391969, 9.0553851381374173, 10.198039027185569, 12.083045973594572, 13.038404810405298, 5.3851648071345037, 8.6023252670426267, 7.2801098892805181, 7.6157731058639087, 10.0, 12.727922061357855, 14.212670403551895, 12.369316876852981, 5.8309518948453007, 9.4339811320566032, 12.529964086141668, 15.652475842498529, 17.464249196572979, 9.2195444572928871, 4.4721359549995796, 3.1622776601683795, 4.4721359549995796, 5.6568542494923806, 5.0, 8.0622577482985491, 11.180339887498949, 13.152946437965905, 3.1622776601683795, 6.324555320336759, 8.2462112512353212, 3.1622776601683795, 5.0990195135927845, 2.0])
        gromos_algorithm = GromosAlgorithm(condensed_matrix)
        cluster = gromos_algorithm._GromosAlgorithm__do_one_iteration(remaining_nodes,4.0)
        expected_cluster = Cluster(4,[4,8])
        self.assertEqual(cluster, expected_cluster)
    
    def test_get_neighbors_for_node(self):
        
        condensed_matrix = CondensedDistanceMatrix([0.2,  1.,  0.3,  .0, 
                                                        0.5,  0.6, 0.7,
                                                              0.9, 0.8,
                                                                   0.4])
        self.assertItemsEqual([0,2],grt.get_neighbors_for_node(condensed_matrix,1,range(5),0.5))

    def test_gromos(self):
        """
        Based in results of hierarchical clustering. the dataset is so simple that may be similar.
        cutoff 4:      {0,1}  {2,3,4}
        cutoff 2.2:    {0,1}  {2}  {3,4}
        cutoff 1.2:    {0,1}  {2}  {3}  {4}
        """
        
        condensed_matrix = CondensedDistanceMatrix([1., 4.5, 8.5, 7.2,\
                                                        4.5, 7.8, 6.7,\
                                                             3.6, 2.2,\
                                                                  2.0])
        gromos_alg = GromosAlgorithm(condensed_matrix)
        
        cutoff_4 = [Cluster(2, [2,3, 4]), Cluster(0, [0,1])]
        cutoff_2 = [Cluster(4, [4,2, 3]), Cluster(0, [0,1])]
        cutoff_1 = [Cluster(0, [0,1]), Cluster(2, [2]), Cluster(3, [3]), Cluster(4, [4])]
        
        clusters =  gromos_alg.perform_clustering(kwargs={"cutoff":4}).clusters
        for i in range(len(clusters)):
            self.assertEqual(cutoff_4[i], clusters[i])
        
        clusters =   gromos_alg.perform_clustering(kwargs={"cutoff":2.2}).clusters
        for i in range(len(clusters)):
            self.assertEqual(cutoff_2[i], clusters[i])
        
        clusters =   gromos_alg.perform_clustering(kwargs={"cutoff":1.2}).clusters
        for i in range(len(clusters)):
            self.assertEqual(cutoff_1[i], clusters[i])

    def test_choose_node_with_higher_cardinality(self):
        condensed_matrix = CondensedDistanceMatrix([1., 4.5, 8.5, 7.2, 
                                                        4.5, 7.8, 6.7, 
                                                             3.6, 2.2, 
                                                                  2.0])
        nodes = range(5)
        self.assertEqual( grt.choose_node_with_higher_cardinality(condensed_matrix, nodes, 4.),\
                          (2,2))
        
        nodes = range(1,5)
        self.assertEqual( grt.choose_node_with_higher_cardinality(condensed_matrix,  nodes, 4.),\
                          (2,2))
        
        nodes = [2,0,3]
        self.assertEqual( grt.choose_node_with_higher_cardinality(condensed_matrix,  nodes, 4.),\
                         (2,1))
        
        nodes = range(5)
        self.assertEqual( grt.choose_node_with_higher_cardinality(condensed_matrix,  nodes, 7.),\
                          (2,4))
         
        nodes = [2,0,3]
        self.assertEqual( grt.choose_node_with_higher_cardinality(condensed_matrix,  nodes, 7.),\
                         (2,2))
        
    def test_get_cluster_for_node(self):
        condensed_matrix = CondensedDistanceMatrix([1., 4.5, 8.5, 7.2, 
                                                        4.5, 7.8, 6.7, 
                                                             3.6, 2.2, 
                                                                  2.0])
        row_len = 5
        nodes_left = range(row_len)
        
        self.assertEqual(len(grt.get_neighbors_for_node(condensed_matrix,  0, nodes_left, 4.)),1)
        self.assertEqual(len(grt.get_neighbors_for_node(condensed_matrix,  1, nodes_left, 4.)),1)
        self.assertEqual(len(grt.get_neighbors_for_node(condensed_matrix,  2, nodes_left, 4.)),2)
        self.assertEqual(len(grt.get_neighbors_for_node(condensed_matrix,  3, nodes_left, 4.)),2)
        self.assertEqual(len(grt.get_neighbors_for_node(condensed_matrix,  4, nodes_left, 4.)),2)
        
        self.assertEqual(len(grt.get_neighbors_for_node(condensed_matrix,  0, nodes_left, 7.)),2)
        self.assertEqual(len(grt.get_neighbors_for_node(condensed_matrix,  1, nodes_left, 7.)),3)
        self.assertEqual(len(grt.get_neighbors_for_node(condensed_matrix,  2, nodes_left, 7.)),4)
        self.assertEqual(len(grt.get_neighbors_for_node(condensed_matrix,  3, nodes_left, 7.)),2)
        self.assertEqual(len(grt.get_neighbors_for_node(condensed_matrix,  4, nodes_left, 7.)),3)
        
        neig_4_3 = [2,4]
        neig = grt.get_neighbors_for_node(condensed_matrix,  3, nodes_left, 4.)
        for i in range(len(neig_4_3)):
            self.assertEqual(neig[i],neig_4_3[i])
        
        neig_7_2 = [0,1,3,4]
        neig = grt.get_neighbors_for_node(condensed_matrix,  2, nodes_left, 7.)
        for i in range(len(neig_7_2)):
            self.assertEqual(neig[i],neig_7_2[i])
            
    def test_eliminate_cluster(self):
        cluster = cluster_from_tuple((4,[2,3,5,7,9]))
        nodes = range(15)
        nodes_left = [0,1,6,8,10,11,12,13,14]
        grt.eliminate_cluster_from_node_list(nodes, cluster)
        nodes_left.sort()
        for i in range(len(nodes)):
            self.assertEqual(nodes[i],nodes_left[i])

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
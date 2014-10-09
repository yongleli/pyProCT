"""
Created on 13/02/2013

@author: victor
"""
from pyRMSD.RMSDCalculator import RMSDCalculator
from pyRMSD.condensedMatrix import CondensedMatrix

class RMSDMatrixBuilder(object):

    def __init__(self):
        pass

    @classmethod
    def build(cls, data_handler, matrix_creation_parameters):
        """
        Generates a matrix with the method used in the handler creation.

        @param trajectory_handler:
        @param matrix_creation_parameters:

        @return: The created matrix.
        """
        calculator_type = matrix_creation_parameters.get_value("calculator_type", 
                                                               default_value = "QTRFIT_OMP_CALCULATOR")
        
        structure = data_handler.get_data()
        fit_selection_coordsets = structure.getFittingCoordinates()
        calc_selection_coordsets = structure.getCalculationCoordinates()
        
        if calc_selection_coordsets is None:
            calculator = RMSDCalculator(calculatorType = calculator_type,
                                        fittingCoordsets  = fit_selection_coordsets)
        else:
            symm_groups = []
            if "symmetries" in matrix_creation_parameters:
                # Then prepare it to handle calculation symmetries
                # Description of equivalences must have the same number of atoms
                symm_groups = cls.process_symm_groups(matrix_creation_parameters,
                                                      structure,
                                                      calc_selection_coordsets)
                print "Using symmetries",symm_groups
                
            calculator = RMSDCalculator(calculatorType = calculator_type,
                                        fittingCoordsets  = fit_selection_coordsets,
                                        calculationCoordsets = calc_selection_coordsets,
                                        calcSymmetryGroups = symm_groups)
            
        rmsds = calculator.pairwiseRMSDMatrix()

        return CondensedMatrix(rmsds)

    @classmethod
    def process_symm_groups(cls, matrix_parameters, structure, calc_selection_coordsets):
        symm_groups = []
        for equivalence_id in matrix_parameters["symmetries"]:
            # Example: [["name C10", "name C30"],["name O7", "name O20"]]
            symm_group = cls.process_group(equivalence_id,
                                           matrix_parameters,
                                           structure,
                                           calc_selection_coordsets)

            symm_groups.append(symm_group)
        return symm_groups

    @classmethod
    def process_group(cls, equivalence_id, matrix_parameters, structure, calc_selection_coordsets):

        common_selection = matrix_parameters["symmetries"][equivalence_id]["common"]
        atom_selections = matrix_parameters["symmetries"][equivalence_id]["equivalences"]

        symm_group = []
        for atom_selection in atom_selections:
            atom1_coords = cls.select_one_atom( structure,
                                                "%s and %s"%(common_selection,atom_selection[0]))

            atom1_index = cls.locate_index(atom1_coords, calc_selection_coordsets)

            atom2_coords = cls.select_one_atom( structure,
                                                "%s and %s"%(common_selection,atom_selection[1]))

            atom2_index = cls.locate_index(atom2_coords, calc_selection_coordsets)

            symm_group.append((atom1_index, atom2_index))
        return tuple(symm_group)
    
    @classmethod
    def select_one_atom(self, structure, selection):
        # We pick coordinates only for first frame
        coordsets =  structure.getSelectionCoordinates(selection)[0]

        if len(coordsets) == 0:
            print "[ERROR RMSDMatrixBuilder:select_one_atom] Selection returned 0 atoms (%s)."%selection
            exit(-1)

        if len(coordsets) > 1:
            print "[ERROR RMSDMatrixBuilder:select_one_atom] Selection returned more than one atom (%s)."%selection
            exit(-1)

        return coordsets[0]
    
    @classmethod
    def locate_index(cls,atom_coords, coordsets):
        for i,coord in enumerate(coordsets[0]): # <- we work with the first frame only
            if  coord[0] == atom_coords[0] and coord[1] == atom_coords[1] and coord[2] == atom_coords[2]:
                return i
        return None


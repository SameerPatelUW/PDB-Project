# -*- coding: utf-8 -*-

from Bio import PDB
pdb1 = PDB.PDBList()
pdb1.retrieve_pdb_file("1C7D")
parser = PDB.PDBParser(PERMISSIVE=1)
structure = parser.get_structure("1C7D",r'C:\Users\Sameer\AppData\Local\Enthought\Canopy\User\Lib\site-packages\Bio\c7\pdb1c7d.ent')
print(structure)
for model in structure:
    for chain in model:
        for residue in chain:
            for atom in residue:                                  
                N = atom.get_name()
                I = atom.get_id()
                Y = atom.get_coord()                    
                V = atom.get_vector()
                O = atom.get_occupancy()
                B = atom.get_bfactor()
                if 10 < B < 50:
                    print(V, B)
                    
print("first commit to git")



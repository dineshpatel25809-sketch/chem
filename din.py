

from rdkit import Chem
import pubchempy as pcp

def name_to_smiles(molecule_name):
    try:
        # Search PubChem for the molecule by name
        compound = pcp.get_compounds(molecule_name, 'name')
        if not compound:
            return f"No compound found for '{molecule_name}'"
        
        # Get the canonical SMILES from PubChem
        smiles = compound[0].canonical_smiles
        
        # Verify with RDKit
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            return f"Invalid SMILES retrieved for '{molecule_name}'"
        
        return smiles
    except Exception as e:
        return f"Error: {str(e)}"


from rdkit.Chem import Descriptors
from rdkit.Chem import Draw

# Create a molecule from a SMILES string
smiles=name_to_smiles(input("Enter name of Chemical compound: "))  # Example molecule
mol = Chem.MolFromSmiles(smiles)

# Compute some properties
mol_weight = Descriptors.MolWt(mol)
num_atoms = mol.GetNumAtoms()
num_bonds = mol.GetNumBonds()

print(f"SMILES: {smiles}")
print(f"Molecular Weight: {mol_weight}")
print(f"Number of Atoms: {num_atoms}")
print(f"Number of Bonds: {num_bonds}")


# Draw the molecule
Draw.MolToImage(mol).show()

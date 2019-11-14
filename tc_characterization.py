
import pandas as pd
import pubchempy as pcp

# from chembl_webresource_client.new_client import new_client

# molecule = new_client.molecule
# molecule.set_format('json')
# res = molecule.search('aspirin')


# df = pd.io.json.json_normalize(res)


# print(df[["pref_name",
#             "molecule_chembl_id", 
#             "molecule_structures.canonical_smiles", 
#             "molecule_structures.standard_inchi_key",
#             "molecule_properties.acd_most_apka",
#             "molecule_properties.alogp",
#             "molecule_properties.mw_freebase"]])
# print(df.columns)

with open('CAS_no_struc.csv', 'r') as cas_file:

    for cas in cas_file:
        cas_num = cas.strip()
        results = pcp.get_compounds(cas_num, 'name')
        if results:
            for compound in results:
                print(compound.isomeric_smiles)
        else:
            print(cas_num)
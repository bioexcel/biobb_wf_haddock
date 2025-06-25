antibody_pdb = '4G6K'
antigen_pdb = '4I1B'
complex_pdb = '4G6M'
out_path = './data/antibody'
ab_pdb = f'{out_path}/pre/{antibody_pdb}_0.pdb'
ag_pdb = f'{out_path}/pre/{antigen_pdb}_0.pdb'
cx_pdb = f'{out_path}/pre/{complex_pdb}_0.pdb'

antibody_prep = f'{out_path}/pre/{antibody_pdb}_clean.pdb'
antigen_prep = f'{out_path}/pre/{antigen_pdb}_clean.pdb'
complex_prep = f'{out_path}/pre/{complex_pdb}_clean.pdb'

ab_actpass = f'{out_path}/pre/{antibody_pdb}_actpass.txt'
ag_actpass = f'{out_path}/pre/{antigen_pdb}_actpass.txt'
complex_tbl = f'{out_path}/pre/ambig-paratope-NMR-epitope.tbl'
body_tbl = f'{out_path}/pre/antibody-unambig.tbl'

step_nb = 1
mol1_output_top_zip_path = f'{out_path}/docking/{step_nb}/top_mol1.zip'
mol2_output_top_zip_path = f'{out_path}/docking/{step_nb}/top_mol2.zip'
wf_topology = f'{out_path}/docking/{step_nb}/wf_topology.zip'

step_nb = 2
docking_output_zip_path = f'{out_path}/docking/{step_nb}/docking.zip'
wf_rigidbody = f'{out_path}/docking/{step_nb}/wf_rigidbody.zip'

step_nb = 3
output_evaluation_zip_path = f'{out_path}/docking/{step_nb}/caprieval.zip'
wf_caprieval = f'{out_path}/docking/{step_nb}/wf_caprieval.zip'

step_nb = 4
output_selection_zip_path = f'{out_path}/docking/{step_nb}/selected.zip'
wf_seletop = f'{out_path}/docking/{step_nb}/wf_seletop.zip'

step_nb = 5
refinement_output_zip_path = f'{out_path}/docking/{step_nb}/flexref.zip'
wf_flexref = f'{out_path}/docking/{step_nb}/wf_flexref.zip'

step_nb = 6
output_evaluation_zip_path2 = f'{out_path}/docking/{step_nb}/caprieval2.zip'
wf_caprieval2 = f'{out_path}/docking/{step_nb}/wf_caprieval2.zip'

step_nb = 7
refinement_output_zip_path = f'{out_path}/docking/{step_nb}/emref.zip'
wf_emref = f'{out_path}/docking/{step_nb}/wf_emref.zip'

step_nb = 8
output_evaluation_zip_path3 = f'{out_path}/docking/{step_nb}/caprieval3.zip'
wf_caprieval3 = f'{out_path}/docking/{step_nb}/wf_caprieval3.zip'

step_nb = 9
output_cluster_zip_path = f'{out_path}/docking/{step_nb}/clustfcc.zip'
wf_clustfcc = f'{out_path}/docking/{step_nb}/wf_clustfcc.zip'

step_nb = 10
output_seletopclusts_zip_path = f'{out_path}/docking/{step_nb}/seletopclusts.zip'
wf_seletopclusts = f'{out_path}/docking/{step_nb}/wf_seletopclusts.zip'

step_nb = 11
output_evaluation_zip_path4 = f'{out_path}/docking/{step_nb}/caprieval4.zip'
wf_caprieval4 = f'{out_path}/docking/{step_nb}/wf_caprieval4.zip'

step_nb = 12
output_contactmap_zip_path = f'{out_path}/docking/{step_nb}/contact_map.zip'
wf_contact_map = f'{out_path}/docking/{step_nb}/wf_contact_map.zip'

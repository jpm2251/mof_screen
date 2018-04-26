from pymofscreen.cif_handler import get_cif_files
from pymofscreen.screen import screener

#Run screening analysis
mofpath = '/projects/p30148/vasp_jobs/structures/CoRE1-DFT-OMS/'
basepath = '/projects/p30148/vasp_jobs/MOFs/testing/'
submit_script = 'sub_screen4_temp.job'
stdout_file = 'driver.out'
cif_files = get_cif_files(mofpath)
s = screener(mofpath,basepath,submit_script=submit_script,
	stdout_file=stdout_file)
for cif_file in cif_files:
	mof = s.run_screen(cif_file,'volume')
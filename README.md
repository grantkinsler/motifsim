Motif Simulation
Grant Kinsler
Written: 15/06/2015
Last Update: 01/03/2016

motifsim_master.py is the master file of the simulation. Options used to indicate the parameters used in the run.
Use --help option for more information on parameter options.

Example command line way to run a simulation (consisting of 2 trials of 100 rounds each, with various other parameters):
python motifsim_master.py --trials=2 --maxStrands=10 --maxStrandLength=7 --numCells=10 --numRounds=100 --motif=10000 --elong=0.05 --bias=0.5

List of other necessary files:
motifsim_trial.py; runs a trial of the simulation
motifsim_motifoutput.py; runs simulations and controls motif data csv output
motifsim_allstrandoutput.py; controls all data csv output
motifsim_fulltrialoutput.py; controls full trial 1 data dsv output
cell.py; defines Cell class
population.py; defines Population class

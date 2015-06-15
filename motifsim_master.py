
import sys
import getopt
from motifsim_motifoutput import motifsim_motifoutput
from motifsim_fulltrialoutput import motifsim_fulltrialoutput
from motifsim_allstrandoutput import motifsim_allstrandoutput

def usage():
	print "Running a Motif Simulation using the parameters designated by options\n"
	print "PARAMETERS:"
	print "--trials, --growthIterations, --maxStrands, --maxStrandLength, --numCells, --numRounds, --motif, --elong, --bias, --basenumber, --p_divide\n"
	print "Outputs three csv files:\n"
	print "1. 'MotifData' designates the csv file containing primarily motif data. First row is parameters."
	print "For each trial, a row of motif frequency per round, a row of freq of total nr_strands used per round, a row of freq_nr_cells_with_motif per round"
	print "Last 6 rows are mean (by round) of the three data types collected, and then standard deviation of the same.\n"
	print "2. 'FullTrial1Data' designates a csv file where each row represents the cell contents for a single cell at a particular time point (plus first row of parameters)."
	print "The first numCells rows are the cells after the first round.\n"
	print "3. 'AllStrandData' designates a csv file where the first row is a list of all possible strands in the simulation."
	print "The rows beneath correspond chronologically with time, first with all mean data and then with stdev data (mean1, mean2, ..., stdev1, stdev2, ...) "


def main(argv):

	try:
		opts, args = getopt.getopt(argv, "h", ["help","testprefix=","trials=","growthIterations=","maxStrands=","maxStrandLength=","numCells=","numRounds=","motif=","elong=","bias=","basenumber=","p_divide="])
	except getopt.GetoptError, error:
		sys.stderr.write(str(error)+"\n")
		usage()
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			usage()
			sys.exit()
		elif opt =="--testprefix":
			testprefix = arg
		elif opt == "--trials" :
			trials = int(arg)
		elif opt == "--growthIterations" :
			growthIterations = int(arg)
		elif opt == "--maxStrands" :
			max_strand_nr = int(arg)
		elif opt == "--maxStrandLength" :
			maxStrandLength = int(arg)
		elif opt == '--numCells' :
			numCells = int(arg)
		elif opt == '--numRounds' :
			numRounds = int(arg)
		elif opt == '--motif' :
			motif = arg
		elif opt == '--elong' :
			elong = float(arg)
		elif opt == '--bias' :
			bias = float(arg)
		elif opt == '--basenumber' :
			basenumber = int(arg)
		elif opt == '--p_divide' :
			p_divide = float(arg)
		else:
			sys.stderr.write("Unknown option %s\n" %opt)
			usage()
			sys.exit(2)

	masterprefix = 'TESTMotifSimulation_'

	parameterlist = [trials, growthIterations, max_strand_nr, maxStrandLength, numCells, numRounds, repr(motif), elong, elong, bias, basenumber, p_divide]

	pop_tracker, nr_strands_per_time = motifsim_motifoutput(parameterlist,masterprefix,testprefix,trials,growthIterations,max_strand_nr,maxStrandLength,numCells,numRounds,motif,elong,bias,basenumber,p_divide)

	motifsim_fulltrialoutput(parameterlist,masterprefix,testprefix,pop_tracker[0],trials,growthIterations,max_strand_nr,maxStrandLength,numCells,numRounds,motif,elong,bias,basenumber,p_divide)

	motifsim_allstrandoutput(parameterlist,masterprefix,testprefix,pop_tracker,nr_strands_per_time,trials,growthIterations,max_strand_nr,maxStrandLength,numCells,numRounds,motif,elong,bias,basenumber,p_divide)


if __name__ == "__main__":
	main(sys.argv[1:])








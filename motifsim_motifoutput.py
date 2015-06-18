import csv
from motifsim_trial import motifsim_trial
import itertools
import numpy

def flatten(items, seqtypes=(list, tuple)): # used for flattening lists
    for i, x in enumerate(items):
        while isinstance(items[i], seqtypes):
            items[i:i+1] = items[i]
    return items

def motifsim_motifoutput(parameterlist,masterprefix,testprefix,trials,growthIterations,max_strand_nr,maxStrandLength,numCells,numRounds,motif,elong,bias,basenumber,p_divide):
	pop_tracker = []


	with open(masterprefix+ testprefix +'_MotifData_motif{motif}_len{maxStrandLength}_bias{bias}_elong{elong}_{trials}trials_numRound{numRounds}_bn{basenumber}_div{p_divide}.csv'.format(motif = motif, maxStrandLength = maxStrandLength, bias=bias, elong=elong, trials=trials, numRounds=numRounds, basenumber= basenumber, p_divide=p_divide), 'wb') as f: 
		writer = csv.writer(f)
		writer.writerow(parameterlist)

		for trial in range(trials):
			pop_tracker.append([])
			nr_motifs, nr_strands, nr_cells_with_motif, pop_tracker[trial] = motifsim_trial(motif,growthIterations,max_strand_nr,maxStrandLength,numCells,numRounds,elong,bias,basenumber,p_divide)

			motif_freq = [motifs / float(total) for motifs,total in itertools.izip(nr_motifs,nr_strands)]
			strands_freq = [strands / float(max_strand_nr*numCells) for strands in nr_strands]
			cells_with_freq = [cells / float(numCells) for cells in nr_cells_with_motif]

			writer.writerow(motif_freq)
			writer.writerow(strands_freq)
			writer.writerow(cells_with_freq)

			if trial == 0:
				motif_freq_aggregate = motif_freq
				strands_freq_aggregate = strands_freq
				cells_with_freq_aggregate = cells_with_freq
				nr_strands_per_time = nr_strands
			else:
				motif_freq_aggregate = [list(round_data) for round_data in zip(motif_freq_aggregate,motif_freq)]
				strands_freq_aggregate = [list(round_data) for round_data in zip(strands_freq_aggregate,strands_freq)]
				cells_with_freq_aggregate = [list(round_data) for round_data in zip(cells_with_freq_aggregate,cells_with_freq)]
				nr_strands_per_time = [list(round_data) for round_data in zip(nr_strands_per_time,nr_strands)]
		
		for time_point in range(numRounds):
			motif_freq_aggregate[time_point] = flatten(motif_freq_aggregate[time_point])
			strands_freq_aggregate[time_point] = flatten(strands_freq_aggregate[time_point])
			cells_with_freq_aggregate[time_point] = flatten(cells_with_freq_aggregate[time_point])
			nr_strands_per_time[time_point] = flatten(nr_strands_per_time[time_point])
		
		means = []
		stdevs = [] 

		for iterator in range(3):
			means.append([])
			stdevs.append([])

		for time_point in range(numRounds):
			means[0].append(numpy.mean(motif_freq_aggregate[time_point]))
			stdevs[0].append(numpy.std(motif_freq_aggregate[time_point]))
			means[1].append(numpy.mean(strands_freq_aggregate[time_point]))
			stdevs[1].append(numpy.std(strands_freq_aggregate[time_point]))
			means[2].append(numpy.mean(cells_with_freq_aggregate[time_point]))
			stdevs[2].append(numpy.std(cells_with_freq_aggregate[time_point]))

		for mean_data in means:
			writer.writerow(mean_data)

		for stdev_data in stdevs:
			writer.writerow(stdev_data)
	f.close()

	return pop_tracker, nr_strands_per_time

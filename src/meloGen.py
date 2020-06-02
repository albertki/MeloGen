# "MeloGen": Informed melody generator program
# Written by Albert Ki
# 5/1/2020

from numpy import random as nprandom, array as nparray
from random import randint, choice
from music21 import *
from copy import deepcopy
from myMarkovChain import initializeMarkovChain	# custom class to determine subsequent note durations

# Custom class containing a music21 score object and useful pertinent attributes
class MyMusic21:
	def __init__(self, myScore):
		self.score = myScore
		self.title = self.getTitle()
		self.bpm = self.getBPM()
		self.timeSig = self.getTimeSig()
		self.strongBeats = self.getStrongBeats()
		self.chordScore = self.getChordified()
		self.keyAnalysis = self.getKeyAnalysis()
		self.scaleOfSong = self.keyAnalysis.getScale()
		self.scalePitches = self.keyAnalysis.pitches[:-1]
		self.noteFrequency = self.getPitchClassData()	# {}
		self.lastMeasureNumber = self.getLastMeasureNumber()
		self.highestTime = self.chordScore.highestTime

	# Print relevant song data for the user
	def printSongData(self):
		print("================================================================")
		print("Song title:", self.title)
		print("BPM:", str(self.bpm).split(' ')[-1][:-1])
		print("Music time signature: {0}/{1}".format(self.timeSig.beatCount, self.timeSig.denominator))
		print("\tStrong Beats: {0} & {1}".format(self.strongBeats[0], self.strongBeats[1]))
		print("Expected music key:", self.keyAnalysis)
		print("Expected scale pitches:", [str(p.name) for p in self.scalePitches])	# ['G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F#5', 'G5']
		print("Pitch spread (%):", {str(k):round(v,2) for k,v in self.noteFrequency.items()})
		print("Music key confidence:", self.keyAnalysis.correlationCoefficient)
		print("Other music key alternatives:")
		for analysis in self.keyAnalysis.alternateInterpretations:
			if (analysis.correlationCoefficient > 0.5):
				print('\t', analysis)
		print("# of measures:", self.lastMeasureNumber)
		print("================================================================\n")

	# Get the title of the song
	def getTitle(self):
		return self.score.metadata.title.split('.')[0]

	# Get the tempo mark of the song
	def getBPM(self):
		for el in self.score.recurse():
			if 'MetronomeMark' in el.classes:
				return el
	
	# Get the time signature of the song
	def getTimeSig(self):
		timeS = self.score.getTimeSignatures()[0]
		return timeS

	# Get the strong beats of the song based on its time signature
	def getStrongBeats(self):
		timeS = self.timeSig
		beatAccents = [timeS.getAccentWeight(x) for x in range(timeS.numerator)]
		strongBeat1 = beatAccents.index(max(beatAccents))
		beatAccents[strongBeat1] = -1
		strongBeat2 = beatAccents.index(max(beatAccents))
		strongBeats = [timeS.getBeat(strongBeat1), timeS.getBeat(strongBeat2)]
		
		return strongBeats

	# Get the key of song
	def getKeyAnalysis(self):
		key = self.chordScore.analyze('key')
		return key

	# Analyze occurring pitches in the song and return the note distribution
	def getPitchClassData(self):
		p = graph.plot.HistogramPitchClass(self.score, title='Pitch Class Histogram: \"{}\"'.format(self.title))
			# HistogramPitchClass shows counts>0 from note C to Bb
			# HistogramPitchClass.data returns list of triples- [(noteIndex, count, {}), ...]
			# where noteIndex=0 for C, 1 for C#, 2 for D, 4 for E, ...etc.
		p.extractData()
		data = p.data
		noteIndices = scale.ChromaticScale('C').pitches[:-1]
		noteCounts = {key: 0 for key in noteIndices}
		# Label data's pitchclass index w/ actual notes
		for i, count, ignore in data:
			noteCounts[noteIndices[i]] = count

		# Create one big list union of both occurring pitches and all scale pitches
		allNotes = {key: 0 for key in self.scalePitches}
		for x in noteCounts:
			flag = False
			# Keep only unique notes (don't re-add enharmonics)
			for y in self.scalePitches:
				if x.pitchClass == y.pitchClass:
					allNotes[y] = noteCounts[x]
					flag = True
					break
			if not flag and noteCounts[x] != 0:
				allNotes[x] = noteCounts[x]
		allNotes = {k: v for k, v in sorted(allNotes.items(), reverse=True, key=lambda item: item[1])}
		
		return self.getNoteFreq(allNotes)

	# Get a list of each appearing pitch's rate of occurrence 
	def getNoteFreq(self, noteFrequency):
		total = sum(noteFrequency.values())

		for k in noteFrequency.keys():
			noteFrequency[k] = noteFrequency[k] / total
		
		return noteFrequency

	# Get a 1-Part chord version of the song
	def getChordified(self):
		chordified = self.score.chordify()		# chordify() returns single Part
		chordifiedScore = stream.Score()
		chordifiedScore.insert(0, chordified)
		chordScore = self.harmonic_reduction(chordifiedScore)
		
		return chordScore

	# Get last measure number of the song
	def getLastMeasureNumber(self):
		pt = next(self.chordScore.getElementsByClass('Part'))
		mIter = pt.getElementsByClass('Measure')
		meas = None
		for meas in mIter:
			pass
		
		return meas.measureNumber
	
	# Returns a simplified Part containing quarter-length chords on downbeats only (bt. 1 & 3)
	def harmonic_reduction(self, chordScore):
		pt = stream.Part()
		pt.append(instrument.Piano())
		pt.append(self.bpm)
		pt.timeSignature = self.timeSig
		pt.keySignature = chordScore.analyze('key')
		mIter = chordScore[0].getElementsByClass('Measure')
		
		for m in mIter:
			tempStrm = stream.Measure('4/4', number=m.measureNumber)
			e1 = m.getElementAtOrBefore(0)
			e2 = m.getElementAtOrBefore(2)
			if e1.isChord:
				e1.closedPosition(inPlace=True, forceOctave=3)
				e1 = chord.Chord(e1.pitches, quarterLength=1)
			elif e1.isRest:
				e1 = note.Rest(quarterLength=1)
			if e2.isChord:
				e2.closedPosition(inPlace=True, forceOctave=3)
				e2 = chord.Chord(e2.pitches, quarterLength=1)
			elif e2.isRest:
				e2 = note.Rest(quarterLength=1)
			
			tempStrm.insert(0, e1)
			tempStrm.insert(1, note.Rest(quarterLength=1))
			tempStrm.insert(2, e2)
			tempStrm.insert(3, note.Rest(quarterLength=1))
			
			pt.append(tempStrm)
		
		score = stream.Score()
		score.insert(0, pt)
		score[0].measure(1).insert(0, self.bpm)
		
		return score
	
	# Generate a melody from the given simplified score of the song
	def addMelody(self):
		print("Building a melody...")
		fullScore = deepcopy(self.chordScore)
		melodyStream = stream.Part()	# empty melody stream
		melodyStream.timeSignature = self.timeSig
		melodyStream.keySignature = self.keyAnalysis
		mIter = fullScore[0].getElementsByClass('Measure')
		prevNoteDuration = 1.0
		# Add a melody per measure
		for m in mIter:
			melodyStream, prevNoteDuration = self.addMelodyToMeasure(melodyStream, m, prevNoteDuration)
		
		# Default melody instrument is set to Flute- can be altered to others accepted by music21
		melodyStream.insert(0, instrument.Flute())
		
		fullScore.insert(1, melodyStream)
		print("Melody created successfully!")
		
		return fullScore
	
	# Generate a melody for the given measure, using an informed search for notes and note durations, per se
	def addMelodyToMeasure(self, currMelodyStream, currMeasure, prevNoteDuration):
		# If already reached last note of melody
		if currMelodyStream.highestTime >= self.highestTime:
			return currMelodyStream, prevNoteDuration
		
		el1 = currMeasure.getElementAtOrBefore(0)	# chord or rest
		el2 = currMeasure.getElementAtOrBefore(2)	# chord or rest

		# If either downbeat has rest, then no melody (temporarily...)
		if el1.isRest or el2.isRest:
			remainingEmptyBeatsInMeasure = (currMeasure.highestTime + currMeasure.offset) - currMelodyStream.highestTime
			currMelodyStream.append(note.Rest(quarterLength=remainingEmptyBeatsInMeasure))
			return currMelodyStream.makeMeasures(), prevNoteDuration

		chord1Tones = el1.pitches
		chord2Tones = el2.pitches
		# (can add note lengths that extend across current measure, but should stop and return afterwards)
		while currMelodyStream.highestTime < currMeasure.highestTime + currMeasure.offset:
			# 1st-order Markov chain to predict subsequent state(note duration) from previous note duration
			noteDuration = markov.note_forecast(1, str(prevNoteDuration)) #float
			# Make sure added note doesn't exceed FINAL bar of piece
			while currMelodyStream.highestTime + noteDuration > self.highestTime:
				noteDuration -= .5
			prevNoteDuration = noteDuration
			p = self.getNoteProb(chord1Tones, chord2Tones)
			n = note.Note(nprandom.choice(list(self.noteFrequency.keys()), p=p).name, quarterLength=noteDuration, octave=choice(oct8ve))	# Note object
			currMelodyStream.append(n)
		
		return currMelodyStream.makeMeasures(), prevNoteDuration
	
	# Returns list of probabilities to determine the choice of note
	def getNoteProb(self, chord1pitches, chord2pitches):
		temp = {k.pitchClass: i for i,k in enumerate(self.noteFrequency.keys())}
		p = nparray(list(self.noteFrequency.values()))
		# Chord tones, scale tones have additional weight
		for c in chord1pitches:
			p[temp[c.pitchClass]] += .15
		for c in chord2pitches:
			p[temp[c.pitchClass]] += .15
		for c in self.scalePitches:
			p[temp[c.pitchClass]] += .10
		p /= sum(p)
		
		return p

# Returns the "best" individual in population, based on the fitness function
def geneticAlgorithm(population, k):
	it = 0
	maxIter = 5
	while it < maxIter: # until some individual is fit enough, or reached "max." iterations
		print('Iteration:', it)
		new_population = []
		fitPopulation = evaluate(population)[:k]
		for i in range(len(fitPopulation)):
			x_i = randint(0,len(fitPopulation)-1)
			y_i = randint(0,len(fitPopulation)-1)
			while x_i == y_i:	# ensure that parents are different individuals
				y_i = randint(0, len(fitPopulation)-1)
			print('{},{} will reproduce'.format(x_i, y_i))
			x = fitPopulation[x_i]
			y = fitPopulation[y_i]
			child = reproduce(x, y)
			new_population.append(child)
		population.extend(new_population)
		it += 1

	# print('outside while loop')
	fitPopulation = evaluate(population)
	fittest = fitPopulation[0]
	
	return fittest

def evaluate(population):
	return sorted(population, reverse=True, key=fitnessFunction)

# Returns fitness VALUE from function- evaluation criteria
# Larger total fitness = "better"
def fitnessFunction(individual):
	f_pv = evaluatePitchVariety(individual)
	weight_pv = 5
	f_ns = evaluateNonScaleNotes(individual)
	weight_ns = 5
	f_cm = evaluateContourMovement(individual)
	weight_cm = 8
	
	totalFitness = sum([f_pv*weight_pv, f_ns*weight_ns, f_cm*weight_cm])
	print('totalFitness:', totalFitness)
	print()

	return totalFitness

# Evaluation criteria 1)- ratio of distinct pitches to total number of notes
	# Measures the diversity of the pitch class set used in composing the melody.
def evaluatePitchVariety(individual):
	pl = graph.plot.HistogramPitchSpace(individual.score.parts[1])
	pl.extractData()
	print("# unique pitches:", len(pl.data), ". total # notes:", len(individual.score.parts[1].pitches))
	
	return (len(pl.data)/len(individual.score.parts[1].pitches))*100

# Evaluation criteria 2)- ratio of nonscalar(not belonging to the piece's respective scale) melody notes to scalar notes
	# Measures the strength of tonality in the melody.
def evaluateNonScaleNotes(individual):
	# count number of non-scalar pitchs
	pl = graph.plot.HistogramPitchClass(individual.score.parts[1])
	pl.extractData()
	scalePC = [c.pitchClass for c in individual.scalePitches]
	sc = 0
	nonsc = 0
	for d in pl.data:
		if d[0] not in scalePC:
			nonsc += d[1]
		else:
			sc += d[1]
	print("scalar:", sc, ". nonscalar:", nonsc)
	
	return -(nonsc/sc)*100	# more nonscalar will result in greater deduction (scalar generally safer)

# Evaluation criteria 3)- proportion of stepwise note movements/intervals (1 <= x <= 2 semitones)
	# Higher values indicate a smooth melodic contour with few large leaps in interval
def evaluateContourMovement(individual):
	p = individual.score.parts[1].pitches
	count = 0
	for index, n in enumerate(p):
		if index == len(p)-1:
			break
		if 1 <= abs(n.pitchClass-p[index+1].pitchClass) <= 2:
			count += 1
	print("# stepwise movements:", count, ". # intervals:", len(p)-1)
	
	return (count/(len(p)-1))*100

# Returns a child individual from a crossover operation between 2 "parent" individuals
def reproduce(x,y):
	child = deepcopy(x)
	fullScore = deepcopy(x.chordScore)

	melodyStream1 = x.score.parts[1]
	melodyStream2 = y.score.parts[1]
	n = x.lastMeasureNumber
	c = randint(1, n)	# split point for crossover
	seg = melodyStream1.measures(1, c)
	seg2 = melodyStream2.measures(c+1, n)

	childMelody = stream.Part()
	childMelody.timeSignature = x.timeSig
	childMelody.keySignature = x.keyAnalysis
	childMelody.append(seg)
	seg2measures = seg2.getElementsByClass('Measure')
	childMelody.append(seg2measures[:])
	childMelody = childMelody.makeMeasures()

	fullScore.insert(1, childMelody)
	child.score = fullScore

	return child

if __name__ == "__main__":
	# configure.run()
	print('Ready to get psuedo-creative?   (Press ENTER)')
	input()
	oct8ve = [4]
	print('Melody in 1 octave (default) or 2?   (ENTER 1 or 2)')
	x = input()
	if x == 2:
		oct8ve = [4,5]

	# Pick ONE song (.mxl) or add one
	# songfile = converter.parse('./input_mxl/Grenade.mxl')
	# songfile = converter.parse('./input_mxl/Desperado.mxl')
	# songfile = converter.parse('./input_mxl/Shes_Got_a_Way.mxl')
	songfile = converter.parse('./input_mxl/Stay_With_Me.mxl')

	song = MyMusic21(songfile)
	song.printSongData()
	markov = initializeMarkovChain()
	
	song2 = deepcopy(song)
	song3 = deepcopy(song)
	song4 = deepcopy(song)

	print('Populating first generation melodies...')
	song.score = song.addMelody()
	song2.score = song2.addMelody()
	song3.score = song3.addMelody()
	song4.score = song4.addMelody()
	population = [song, song2, song3, song4]
	print()
	print('Running genetic algorithm on the population...')
	# Run genetic algorithm on population
	k = 4	# max. size of each population
	fittest = geneticAlgorithm(population, k)
	print('GA finished!')
	
	print("================================================================")

	print('Comparison of fitness between first generation melody and genetically modified version')
	print('First generation melody')
	fitnessFunction(song)
	print('Genetic offspring melody')
	fitnessFunction(fittest)

	p1 = graph.plot.HistogramPitchClass(song.score.parts[1], title='Pitch Class Histogram (Pre-GA):\"{}\"'.format(song.title))
	p2 = graph.plot.HistogramPitchClass(fittest.score.parts[1], title='Pitch Class Histogram (Post-GA):\"{}\"'.format(fittest.title))
	print('Would you like to view the results of your psuedo-creativity [MuseScore application required]?   (y or n)')
	x = input()
	if x == 'y':
		song.chordScore.show()
		song.score.show()
		fittest.score.show()
		p1.run()
		p2.run()
	else:
		pass
	song.chordScore.write(fmt='midi', fp='./{}-chord-score.mid'.format(song.title))
	song.score.write(fmt='midi', fp='./{}-pre-ga-melody-score.mid'.format(song.title))
	fittest.score.write(fmt='midi', fp='./{}-post-ga-melody-score.mid'.format(song.title))

	print('Done')
	print("================================================================")

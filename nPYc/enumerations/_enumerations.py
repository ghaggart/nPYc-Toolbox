import enum

class VariableType(enum.Enum):
	"""
	Enumeration of data sampling modalities.
	
	* :term:`Discreetly<Discrete Data>` sampled data types are those where the adjacency of variables is unimportant
	* In :term:`spectral, continuum, and synonymous data<Spectral Data>`, the ordering of variables is important in the interpretation of the data
	"""
	def __repr__(self):
		return '<%s.%s>' % (self.__class__.__name__, self.name)

	Discrete = 1
	Continuum = 2
	Spectral = Continuum
	Profile = Continuum

class Ionisation(enum.Enum):
	"""
	Enumeration of ionisation methods in Mass Spectrometry.
	"""
	# def __repr__(self):
	# 	return '<%s.%s>' % (self.__class__.__name__, self.name)

	EI = 'Electron Impact'
	ESI = 'Electrospray Ionisation'
	DESI = 'Desorption Electrospray Ionisation'
	MALDI = 'Matrix Assisted Laser Desorption Ionisation'

class Polarity(enum.Enum):
	"""
	Enumeration of ionisation polarity.
	"""
	def __repr__(self):
		return '<%s.%s>' % (self.__class__.__name__, self.name)

	Positive = 1
	Negative = 2

class SampleType(enum.Enum):
	"""
	Enumeration of distinct sample types.
	
	* *Study Sample* comprise the study in question
	* *Study Pool* consists of a mixture of all *study samples*
	* *External Reference* a sample of a comparable :term:`matrix` to the *Study Samples*, but not a sample (or mixture) derived from samples acquired as part of the study. Acquired, for example, for assessing analytical quality between studies.
	* *Method Reference* consists of a synthetic mixture of known chemical standards
	* *Procedural Blank* a blank sample not expected to contain any signals from the sample matrix
	"""
	def __repr__(self):
		return '<%s.%s>' % (self.__class__.__name__, self.name)

	#def __lt__(self, other):
	#	return repr(self) < repr(other)

	def __str__(self):
		return '%s' % self._value_

	StudySample = 'Study Sample'
	StudyPool = 'Study Pool'
	ExternalReference = 'External Reference'
	MethodReference = 'Method Reference'
	ProceduralBlank = 'Procedural Blank'


class AssayRole(enum.Enum):
	"""
	Enumeration of assay roles.

	* *Assay* form the core of an analysis
	* *Precision Reference* repeatedly acquired, and used to calculate measures of analytical precision
	* *Linearity Reference* used to assess the linearity of response in the dataset, often by repeated injection at varying concentrations or levels of dilution. If generated by dilution from a base-level, the percentage concentration of each Linearity Reference sample is indicated in the 'Dilution' field of the :py:attr:`~nPYc.objects.Dataset.sampleMetadata` table
	"""
	def __repr__(self):
		return '<%s.%s>' % (self.__class__.__name__, self.name)

	#def __lt__(self, other):
	#	return repr(self) < repr(other)

	def __str__(self):
		return '%s' % self._value_

	Assay = 'Assay'
	PrecisionReference = 'Precision Reference'
	LinearityReference = 'Linearity Reference'
	Blank = 'Blank'


class SampleMatrix(enum.Enum):
	"""
	Enumeration of sample types
	"""
	def __repr__(self):
		return '<%s.%s>' % (self.__class__.__name__, self.name)

	def __str__(self):
		return '%s' % self._value_

	Urine = 'Urine'
	Serum = 'Serum'
	Plasma = 'Plasma'
	BloodProduct = 'Blood Product'
	CerebrospinalFluid = 'Cerebrospinal Fluid'


class DatasetLevel(enum.Enum):
	def __repr__(self):
		return '<%s.%s>' % (self.__class__.__name__, self.name)

	Unknown = 0
	Empty = 1
	ValuesOnly = 2
	QCReady = 3


class CalibrationMethod(enum.Enum):
	"""
	Enumeration of distinct calibration methods.

	* *noCalibration* for compounds not quantified (monitored for relative information)
	* *noIS* for compounds without Internal Standard (and Internal Standards themselves)
	* *backcalculatedIS* for compounds using an Internal Standard
	* *otherCalibration* for compounds employing another calibration approach
	* *nmrCalibration* for compounds quantified by NMR
	"""
	def __repr__(self):
		return '<%s.%s>' % (self.__class__.__name__, self.name)

	def __str__(self):
		return '%s' % self._value_

	noCalibration = 'No calibration'
	noIS = 'No Internal Standard'
	backcalculatedIS = 'Backcalculated with Internal Standard'
	otherCalibration = 'Other calibration method'
	nmrCalibration = 'NMR quantitation'


class QuantificationType(enum.Enum):
	"""
	Enumeration of quantification types.

	* *IS* for Internal Standards
	* *QuantOwnLabeledAnalogue* for compounds quantified and validated with own labeled analogue
	* *QuantAltLabeledAnalogue* for compounds quantified and validated with alternative labeled analogue
	* *QuantOther* for compounds quantified using another method
	* *Monitored* for compounds monitored for relative information
	* *BrukerivDrQuant* for compounds quantified with Bruker ivDr methods
	* *BrukerivDrEstimate* for compounds estimated with Bruker ivDr methods

	"""
	def __repr__(self):
		return '<%s.%s>' % (self.__class__.__name__, self.name)

	def __str__(self):
		return '%s' % self._value_

	IS = 'Internal Standard'
	QuantOwnLabeledAnalogue = 'Quantified and validated with own labeled analogue'
	QuantAltLabeledAnalogue = 'Quantified and validated with alternative labeled analogue'
	QuantOther = 'Other quantification'
	Monitored = 'Monitored for relative information'
	BrukerivDrQuant = 'Quantified using Bruker Biospin ivDr methods'


class AnalyticalPlatform(enum.Enum):
	"""
	Enumeration of analytical platform types.

	* *NMR* for Nuclear Magnetic Resonance Spectroscopy
	* *MS* for Mass Spectrometry
	* *Other* placeholder for any other type of instrumentation
	"""
	def __repr__(self):
		return '<%s.%s>' % (self.__class__.__name__, self.name)

	def __str__(self):
		return '%s' % self._value_

	NMR = 'NuclearMagneticResonanceSpectroscopy'
	MS = 'MassSpectrometry'
	Other = 'Other'
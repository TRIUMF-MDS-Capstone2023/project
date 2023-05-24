PYTHON = python
RM = rm

# Paths

H5_FILE = data/CaloRICH_Run11100_CTRL_v1.h5

RICH_PMT_POSITIONS_NPY = data/rich_pmt_positions.npy
RICH_PMT_POSITIONS_DAT = data/rich_pmt_positions.dat

FULL_EVENT_FILE = data/events.parquet

FULL_HIT_FILE = data/hits.parquet

FULL_FILES = \
	$(FULL_EVENT_FILE) \
	$(FULL_HIT_FILE)

EVENT_WITH_HIT_FEATURES_FILE_0_1 = data/events_with_hit_features_[cut_off_time=0.1].parquet
EVENT_WITH_HIT_FEATURES_FILE_0_2 = data/events_with_hit_features_[cut_off_time=0.2].parquet
EVENT_WITH_HIT_FEATURES_FILE_0_3 = data/events_with_hit_features_[cut_off_time=0.3].parquet
EVENT_WITH_HIT_FEATURES_FILE_0_4 = data/events_with_hit_features_[cut_off_time=0.4].parquet
EVENT_WITH_HIT_FEATURES_FILE_0_5 = data/events_with_hit_features_[cut_off_time=0.5].parquet
EVENT_WITH_HIT_FEATURES_FILE_1 = data/events_with_hit_features_[cut_off_time=1.0].parquet
EVENT_WITH_HIT_FEATURES_FILE_3 = data/events_with_hit_features_[cut_off_time=3.0].parquet
EVENT_WITH_HIT_FEATURES_FILE_5 = data/events_with_hit_features_[cut_off_time=5.0].parquet
EVENT_WITH_HIT_FEATURES_FILE_8 = data/events_with_hit_features_[cut_off_time=8.0].parquet
EVENT_WITH_HIT_FEATURES_FILE_10 = data/events_with_hit_features_[cut_off_time=10.0].parquet

EVENT_WITH_HIT_FEATURES_FILES = \
	$(EVENT_WITH_HIT_FEATURES_FILE_0_1) \
	$(EVENT_WITH_HIT_FEATURES_FILE_0_2) \
	$(EVENT_WITH_HIT_FEATURES_FILE_0_3) \
	$(EVENT_WITH_HIT_FEATURES_FILE_0_4) \
	$(EVENT_WITH_HIT_FEATURES_FILE_0_5) \
	$(EVENT_WITH_HIT_FEATURES_FILE_1) \
	$(EVENT_WITH_HIT_FEATURES_FILE_3) \
	$(EVENT_WITH_HIT_FEATURES_FILE_5) \
	$(EVENT_WITH_HIT_FEATURES_FILE_8) \
	$(EVENT_WITH_HIT_FEATURES_FILE_10)

SAMPLE_EVENT_ID_FILE_5_45 = \
	data/sampled_event_ids_[muon,min_momentum=5,max_momentum=45].parquet
SAMPLE_EVENT_ID_FILE_10_45 = \
	data/sampled_event_ids_[muon,min_momentum=10,max_momentum=45].parquet
SAMPLE_EVENT_ID_FILE_15_45 = \
	data/sampled_event_ids_[muon,min_momentum=15,max_momentum=45].parquet
SAMPLE_EVENT_ID_FILE_20_45 = \
	data/sampled_event_ids_[muon,min_momentum=20,max_momentum=45].parquet

SAMPLE_EVENT_ID_FILES = \
	$(SAMPLE_EVENT_ID_FILE_5_45) \
	$(SAMPLE_EVENT_ID_FILE_10_45) \
	$(SAMPLE_EVENT_ID_FILE_15_45) \
	$(SAMPLE_EVENT_ID_FILE_20_45)

# `all` and `clean`

.PHONY : clean

all : \
	$(RICH_PMT_POSITIONS_NPY) \
	$(FULL_PARQUET_FILES) \
	$(EVENT_WITH_HIT_FEATURES_FILES) \
	$(SAMPLE_EVENT_ID_FILES)

clean :
	$(RM) \
		$(RICH_PMT_POSITIONS_NPY) \
		$(FULL_PARQUET_FILES) \
		$(EVENT_WITH_HIT_FEATURES_FILES) \
		$(SAMPLE_EVENT_ID_FILES)

# == Position map ==

$(RICH_PMT_POSITIONS_NPY): $(RICH_PMT_POSITIONS_DAT)
	$(PYTHON) scripts/rich_pmt_compile.py $(RICH_PMT_POSITIONS_DAT) $(RICH_PMT_POSITIONS_NPY)

# == Full events and hits ==

$(FULL_FILES): $(H5_FILE) $(RICH_PMT_POSITIONS_NPY)
	$(PYTHON) scripts/data_extract.py $(H5_FILE) $(RICH_PMT_POSITIONS_NPY) $(FULL_EVENT_FILE) $(FULL_HIT_FILE)

# == Event with hit features ==

$(EVENT_WITH_HIT_FEATURES_FILE_0_1): $(FULL_EVENT_FILE) $(FULL_HIT_FILE)
	$(PYTHON) scripts/data_features.py $(FULL_EVENT_FILE) $(FULL_HIT_FILE) $(EVENT_WITH_HIT_FEATURES_FILE_0_1) 0.1

$(EVENT_WITH_HIT_FEATURES_FILE_0_2): $(FULL_EVENT_FILE) $(FULL_HIT_FILE)
	$(PYTHON) scripts/data_features.py $(FULL_EVENT_FILE) $(FULL_HIT_FILE) $(EVENT_WITH_HIT_FEATURES_FILE_0_2) 0.2

$(EVENT_WITH_HIT_FEATURES_FILE_0_3): $(FULL_EVENT_FILE) $(FULL_HIT_FILE)
	$(PYTHON) scripts/data_features.py $(FULL_EVENT_FILE) $(FULL_HIT_FILE) $(EVENT_WITH_HIT_FEATURES_FILE_0_3) 0.3

$(EVENT_WITH_HIT_FEATURES_FILE_0_4): $(FULL_EVENT_FILE) $(FULL_HIT_FILE)
	$(PYTHON) scripts/data_features.py $(FULL_EVENT_FILE) $(FULL_HIT_FILE) $(EVENT_WITH_HIT_FEATURES_FILE_0_4) 0.4

$(EVENT_WITH_HIT_FEATURES_FILE_0_5): $(FULL_EVENT_FILE) $(FULL_HIT_FILE)
	$(PYTHON) scripts/data_features.py $(FULL_EVENT_FILE) $(FULL_HIT_FILE) $(EVENT_WITH_HIT_FEATURES_FILE_0_5) 0.5

$(EVENT_WITH_HIT_FEATURES_FILE_1): $(FULL_EVENT_FILE) $(FULL_HIT_FILE)
	$(PYTHON) scripts/data_features.py $(FULL_EVENT_FILE) $(FULL_HIT_FILE) $(EVENT_WITH_HIT_FEATURES_FILE_1)   1.0

$(EVENT_WITH_HIT_FEATURES_FILE_3): $(FULL_EVENT_FILE) $(FULL_HIT_FILE)
	$(PYTHON) scripts/data_features.py $(FULL_EVENT_FILE) $(FULL_HIT_FILE) $(EVENT_WITH_HIT_FEATURES_FILE_3)   3.0

$(EVENT_WITH_HIT_FEATURES_FILE_5): $(FULL_EVENT_FILE) $(FULL_HIT_FILE)
	$(PYTHON) scripts/data_features.py $(FULL_EVENT_FILE) $(FULL_HIT_FILE) $(EVENT_WITH_HIT_FEATURES_FILE_5)   5.0

$(EVENT_WITH_HIT_FEATURES_FILE_8): $(FULL_EVENT_FILE) $(FULL_HIT_FILE)
	$(PYTHON) scripts/data_features.py $(FULL_EVENT_FILE) $(FULL_HIT_FILE) $(EVENT_WITH_HIT_FEATURES_FILE_8)   8.0

$(EVENT_WITH_HIT_FEATURES_FILE_10): $(FULL_EVENT_FILE) $(FULL_HIT_FILE)
	$(PYTHON) scripts/data_features.py $(FULL_EVENT_FILE) $(FULL_HIT_FILE) $(EVENT_WITH_HIT_FEATURES_FILE_10) 10.0

# == Sample event IDs ==

$(SAMPLE_EVENT_ID_FILE_5_45): $(FULL_PARQUET_FILES)
	$(PYTHON) scripts/data_sample.py $(FULL_EVENT_FILE)  5 45  $(SAMPLE_EVENT_ID_FILE_5_45)

$(SAMPLE_EVENT_ID_FILE_10_45): $(FULL_PARQUET_FILES)
	$(PYTHON) scripts/data_sample.py $(FULL_EVENT_FILE) 10 45 $(SAMPLE_EVENT_ID_FILE_10_45)

$(SAMPLE_EVENT_ID_FILE_15_45): $(FULL_PARQUET_FILES)
	$(PYTHON) scripts/data_sample.py $(FULL_EVENT_FILE) 15 45 $(SAMPLE_EVENT_ID_FILE_15_45)

$(SAMPLE_EVENT_ID_FILE_20_45): $(FULL_PARQUET_FILES)
	$(PYTHON) scripts/data_sample.py $(FULL_EVENT_FILE) 20 45 $(SAMPLE_EVENT_ID_FILE_20_45)

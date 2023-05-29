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
EVENT_WITH_HIT_FEATURES_FILE_0_6 = data/events_with_hit_features_[cut_off_time=0.6].parquet
EVENT_WITH_HIT_FEATURES_FILE_0_7 = data/events_with_hit_features_[cut_off_time=0.7].parquet
EVENT_WITH_HIT_FEATURES_FILE_0_8 = data/events_with_hit_features_[cut_off_time=0.8].parquet
EVENT_WITH_HIT_FEATURES_FILE_0_9 = data/events_with_hit_features_[cut_off_time=0.9].parquet
EVENT_WITH_HIT_FEATURES_FILE_1_0 = data/events_with_hit_features_[cut_off_time=1.0].parquet
EVENT_WITH_HIT_FEATURES_FILE_2_0 = data/events_with_hit_features_[cut_off_time=2.0].parquet
EVENT_WITH_HIT_FEATURES_FILE_3_0 = data/events_with_hit_features_[cut_off_time=3.0].parquet
EVENT_WITH_HIT_FEATURES_FILE_4_0 = data/events_with_hit_features_[cut_off_time=4.0].parquet
EVENT_WITH_HIT_FEATURES_FILE_5_0 = data/events_with_hit_features_[cut_off_time=5.0].parquet
EVENT_WITH_HIT_FEATURES_FILE_6_0 = data/events_with_hit_features_[cut_off_time=6.0].parquet
EVENT_WITH_HIT_FEATURES_FILE_7_0 = data/events_with_hit_features_[cut_off_time=7.0].parquet
EVENT_WITH_HIT_FEATURES_FILE_8_0 = data/events_with_hit_features_[cut_off_time=8.0].parquet
EVENT_WITH_HIT_FEATURES_FILE_9_0 = data/events_with_hit_features_[cut_off_time=9.0].parquet
EVENT_WITH_HIT_FEATURES_FILE_10_0 = data/events_with_hit_features_[cut_off_time=10.0].parquet

EVENT_WITH_HIT_FEATURES_FILES = \
	$(EVENT_WITH_HIT_FEATURES_FILE_0_1) \
	$(EVENT_WITH_HIT_FEATURES_FILE_0_2) \
	$(EVENT_WITH_HIT_FEATURES_FILE_0_3) \
	$(EVENT_WITH_HIT_FEATURES_FILE_0_4) \
	$(EVENT_WITH_HIT_FEATURES_FILE_0_5) \
	$(EVENT_WITH_HIT_FEATURES_FILE_0_6) \
	$(EVENT_WITH_HIT_FEATURES_FILE_0_7) \
	$(EVENT_WITH_HIT_FEATURES_FILE_0_8) \
	$(EVENT_WITH_HIT_FEATURES_FILE_0_9) \
	$(EVENT_WITH_HIT_FEATURES_FILE_1_0)

EVENT_WITH_HIT_FEATURES_FILES_EXTRA = \
	$(EVENT_WITH_HIT_FEATURES_FILE_2_0) \
	$(EVENT_WITH_HIT_FEATURES_FILE_3_0) \
	$(EVENT_WITH_HIT_FEATURES_FILE_4_0) \
	$(EVENT_WITH_HIT_FEATURES_FILE_5_0) \
	$(EVENT_WITH_HIT_FEATURES_FILE_6_0) \
	$(EVENT_WITH_HIT_FEATURES_FILE_7_0) \
	$(EVENT_WITH_HIT_FEATURES_FILE_8_0) \
	$(EVENT_WITH_HIT_FEATURES_FILE_9_0) \
	$(EVENT_WITH_HIT_FEATURES_FILE_10_0)

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

full: \
	$(RICH_PMT_POSITIONS_NPY) \
	$(FULL_PARQUET_FILES) \
	$(EVENT_WITH_HIT_FEATURES_FILES) \
	$(EVENT_WITH_HIT_FEATURES_FILES_EXTRA) \
	$(SAMPLE_EVENT_ID_FILES)

rich_pmt_positions : $(RICH_PMT_POSITIONS_NPY)

events : $(FULL_EVENT_FILE)

hits : $(FULL_HIT_FILE)

event_with_hit_features : $(EVENT_WITH_HIT_FEATURES_FILES)

event_with_hit_features_0_1 : $(EVENT_WITH_HIT_FEATURES_FILE_0_1)

event_with_hit_features_0_2 : $(EVENT_WITH_HIT_FEATURES_FILE_0_2)

event_with_hit_features_0_3 : $(EVENT_WITH_HIT_FEATURES_FILE_0_3)

event_with_hit_features_0_4 : $(EVENT_WITH_HIT_FEATURES_FILE_0_4)

event_with_hit_features_0_5 : $(EVENT_WITH_HIT_FEATURES_FILE_0_5)

event_with_hit_features_0_6 : $(EVENT_WITH_HIT_FEATURES_FILE_0_6)

event_with_hit_features_0_7 : $(EVENT_WITH_HIT_FEATURES_FILE_0_7)

event_with_hit_features_0_8 : $(EVENT_WITH_HIT_FEATURES_FILE_0_8)

event_with_hit_features_0_9 : $(EVENT_WITH_HIT_FEATURES_FILE_0_9)

event_with_hit_features_1_0 : $(EVENT_WITH_HIT_FEATURES_FILE_1_0)

event_with_hit_features_2_0 : $(EVENT_WITH_HIT_FEATURES_FILE_2_0)

event_with_hit_features_3_0 : $(EVENT_WITH_HIT_FEATURES_FILE_3_0)

event_with_hit_features_4_0 : $(EVENT_WITH_HIT_FEATURES_FILE_4_0)

event_with_hit_features_5_0 : $(EVENT_WITH_HIT_FEATURES_FILE_5_0)

event_with_hit_features_6_0 : $(EVENT_WITH_HIT_FEATURES_FILE_6_0)

event_with_hit_features_7_0 : $(EVENT_WITH_HIT_FEATURES_FILE_7_0)

event_with_hit_features_8_0 : $(EVENT_WITH_HIT_FEATURES_FILE_8_0)

event_with_hit_features_9_0 : $(EVENT_WITH_HIT_FEATURES_FILE_9_0)

event_with_hit_features_10_0 : $(EVENT_WITH_HIT_FEATURES_FILE_10_0)

sample_event_ids : $(SAMPLE_EVENT_ID_FILES)

clean :
	$(RM) \
		$(RICH_PMT_POSITIONS_NPY) \
		$(FULL_PARQUET_FILES) \
		$(EVENT_WITH_HIT_FEATURES_FILES) \
		$(SAMPLE_EVENT_ID_FILES)

# == Position map ==

$(RICH_PMT_POSITIONS_NPY): $(RICH_PMT_POSITIONS_DAT)
	$(PYTHON) scripts/rich_pmt_compile.py $(RICH_PMT_POSITIONS_DAT) $@

# == Full events and hits ==

$(FULL_EVENT_FILE) $(FULL_HIT_FILE) : $(H5_FILE) $(RICH_PMT_POSITIONS_NPY)
	$(PYTHON) scripts/data_extract.py $(H5_FILE) $(RICH_PMT_POSITIONS_NPY) $(FULL_EVENT_FILE) $(FULL_HIT_FILE)

# == Event with hit features ==

$(EVENT_WITH_HIT_FEATURES_FILE_0_1): $(FULL_EVENT_FILE) $(FULL_HIT_FILE)
	$(PYTHON) scripts/data_features.py $(FULL_EVENT_FILE) $(FULL_HIT_FILE) $@ 0.1

$(EVENT_WITH_HIT_FEATURES_FILE_0_2): $(FULL_EVENT_FILE) $(FULL_HIT_FILE)
	$(PYTHON) scripts/data_features.py $(FULL_EVENT_FILE) $(FULL_HIT_FILE) $@ 0.2

$(EVENT_WITH_HIT_FEATURES_FILE_0_3): $(FULL_EVENT_FILE) $(FULL_HIT_FILE)
	$(PYTHON) scripts/data_features.py $(FULL_EVENT_FILE) $(FULL_HIT_FILE) $@ 0.3

$(EVENT_WITH_HIT_FEATURES_FILE_0_4): $(FULL_EVENT_FILE) $(FULL_HIT_FILE)
	$(PYTHON) scripts/data_features.py $(FULL_EVENT_FILE) $(FULL_HIT_FILE) $@ 0.4

$(EVENT_WITH_HIT_FEATURES_FILE_0_5): $(FULL_EVENT_FILE) $(FULL_HIT_FILE)
	$(PYTHON) scripts/data_features.py $(FULL_EVENT_FILE) $(FULL_HIT_FILE) $@ 0.5

$(EVENT_WITH_HIT_FEATURES_FILE_0_6): $(FULL_EVENT_FILE) $(FULL_HIT_FILE)
	$(PYTHON) scripts/data_features.py $(FULL_EVENT_FILE) $(FULL_HIT_FILE) $@ 0.6

$(EVENT_WITH_HIT_FEATURES_FILE_0_7): $(FULL_EVENT_FILE) $(FULL_HIT_FILE)
	$(PYTHON) scripts/data_features.py $(FULL_EVENT_FILE) $(FULL_HIT_FILE) $@ 0.7

$(EVENT_WITH_HIT_FEATURES_FILE_0_8): $(FULL_EVENT_FILE) $(FULL_HIT_FILE)
	$(PYTHON) scripts/data_features.py $(FULL_EVENT_FILE) $(FULL_HIT_FILE) $@ 0.8

$(EVENT_WITH_HIT_FEATURES_FILE_0_9): $(FULL_EVENT_FILE) $(FULL_HIT_FILE)
	$(PYTHON) scripts/data_features.py $(FULL_EVENT_FILE) $(FULL_HIT_FILE) $@ 0.9

$(EVENT_WITH_HIT_FEATURES_FILE_1_0): $(FULL_EVENT_FILE) $(FULL_HIT_FILE)
	$(PYTHON) scripts/data_features.py $(FULL_EVENT_FILE) $(FULL_HIT_FILE) $@ 1.0

$(EVENT_WITH_HIT_FEATURES_FILE_2_0): $(FULL_EVENT_FILE) $(FULL_HIT_FILE)
	$(PYTHON) scripts/data_features.py $(FULL_EVENT_FILE) $(FULL_HIT_FILE) $@ 2.0

$(EVENT_WITH_HIT_FEATURES_FILE_3_0): $(FULL_EVENT_FILE) $(FULL_HIT_FILE)
	$(PYTHON) scripts/data_features.py $(FULL_EVENT_FILE) $(FULL_HIT_FILE) $@ 3.0

$(EVENT_WITH_HIT_FEATURES_FILE_4_0): $(FULL_EVENT_FILE) $(FULL_HIT_FILE)
	$(PYTHON) scripts/data_features.py $(FULL_EVENT_FILE) $(FULL_HIT_FILE) $@ 4.0

$(EVENT_WITH_HIT_FEATURES_FILE_5_0): $(FULL_EVENT_FILE) $(FULL_HIT_FILE)
	$(PYTHON) scripts/data_features.py $(FULL_EVENT_FILE) $(FULL_HIT_FILE) $@ 5.0

$(EVENT_WITH_HIT_FEATURES_FILE_6_0): $(FULL_EVENT_FILE) $(FULL_HIT_FILE)
	$(PYTHON) scripts/data_features.py $(FULL_EVENT_FILE) $(FULL_HIT_FILE) $@ 6.0

$(EVENT_WITH_HIT_FEATURES_FILE_7_0): $(FULL_EVENT_FILE) $(FULL_HIT_FILE)
	$(PYTHON) scripts/data_features.py $(FULL_EVENT_FILE) $(FULL_HIT_FILE) $@ 7.0

$(EVENT_WITH_HIT_FEATURES_FILE_8_0): $(FULL_EVENT_FILE) $(FULL_HIT_FILE)
	$(PYTHON) scripts/data_features.py $(FULL_EVENT_FILE) $(FULL_HIT_FILE) $@ 8.0

$(EVENT_WITH_HIT_FEATURES_FILE_9_0): $(FULL_EVENT_FILE) $(FULL_HIT_FILE)
	$(PYTHON) scripts/data_features.py $(FULL_EVENT_FILE) $(FULL_HIT_FILE) $@ 9.0

$(EVENT_WITH_HIT_FEATURES_FILE_10_0): $(FULL_EVENT_FILE) $(FULL_HIT_FILE)
	$(PYTHON) scripts/data_features.py $(FULL_EVENT_FILE) $(FULL_HIT_FILE) $@ 10.0

# == Sample event IDs ==

$(SAMPLE_EVENT_ID_FILE_5_45): $(FULL_PARQUET_FILES)
	$(PYTHON) scripts/data_sample.py $(FULL_EVENT_FILE)  5 45 $@

$(SAMPLE_EVENT_ID_FILE_10_45): $(FULL_PARQUET_FILES)
	$(PYTHON) scripts/data_sample.py $(FULL_EVENT_FILE) 10 45 $@

$(SAMPLE_EVENT_ID_FILE_15_45): $(FULL_PARQUET_FILES)
	$(PYTHON) scripts/data_sample.py $(FULL_EVENT_FILE) 15 45 $@

$(SAMPLE_EVENT_ID_FILE_20_45): $(FULL_PARQUET_FILES)
	$(PYTHON) scripts/data_sample.py $(FULL_EVENT_FILE) 20 45 $@

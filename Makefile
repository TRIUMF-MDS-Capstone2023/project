PYTHON = python
RM = rm

H5_FILE = data/CaloRICH_Run11100_CTRL_v1.h5

RICH_PMT_POSITIONS_NPY = data/rich_pmt_positions.npy
RICH_PMT_POSITIONS_DAT = data/rich_pmt_positions.dat

FULL_PARQUET_FILES = \
	$(EVENT_FILE) \
	$(HIT_FILE)

EVENT_FILE = data/full_events.parquet

HIT_FILE = data/full_hits.parquet

EVENT_WITH_HIT_FEATURES_FILE_0_1 = data/events_with_hit_features_[cut_off_time=0.1].parquet
EVENT_WITH_HIT_FEATURES_FILE_0_2 = data/events_with_hit_features_[cut_off_time=0.2].parquet
EVENT_WITH_HIT_FEATURES_FILE_0_3 = data/events_with_hit_features_[cut_off_time=0.3].parquet
EVENT_WITH_HIT_FEATURES_FILE_0_4 = data/events_with_hit_features_[cut_off_time=0.4].parquet
EVENT_WITH_HIT_FEATURES_FILE_0_5 = data/events_with_hit_features_[cut_off_time=0.5].parquet

EVENT_WITH_HIT_FEATURES_FILES = \
	$(EVENT_WITH_HIT_FEATURES_FILE_0_1) \
	$(EVENT_WITH_HIT_FEATURES_FILE_0_2) \
	$(EVENT_WITH_HIT_FEATURES_FILE_0_3) \
	$(EVENT_WITH_HIT_FEATURES_FILE_0_4) \
	$(EVENT_WITH_HIT_FEATURES_FILE_0_5)

SAMPLE_PARQUET_FILES = \
	data/sampled_events.parquet \
	data/sampled_hits.parquet

.PHONY : clean

all : \
	$(RICH_PMT_POSITIONS_NPY) \
	$(FULL_PARQUET_FILES) \
	$(EVENT_WITH_HIT_FEATURES_FILES) \
	$(SAMPLE_PARQUET_FILES)

clean :
	$(RM) \
		$(RICH_PMT_POSITIONS_NPY) \
		$(FULL_PARQUET_FILES) \
		$(EVENT_WITH_HIT_FEATURES_FILES) \
		$(SAMPLE_PARQUET_FILES)

$(RICH_PMT_POSITIONS_NPY): $(RICH_PMT_POSITIONS_DAT)
	$(PYTHON) scripts/rich_pmt_compile.py $(RICH_PMT_POSITIONS_DAT) $(RICH_PMT_POSITIONS_NPY)

$(FULL_PARQUET_FILES): $(H5_FILE)
	$(PYTHON) scripts/data_extract.py

$(EVENT_WITH_HIT_FEATURES_FILES): $(EVENT_FILE) $(HIT_FILE)
	$(PYTHON) scripts/data_features.py $(EVENT_FILE) $(HIT_FILE) $(EVENT_WITH_HIT_FEATURES_FILE_0_1) in_time_point_1
	$(PYTHON) scripts/data_features.py $(EVENT_FILE) $(HIT_FILE) $(EVENT_WITH_HIT_FEATURES_FILE_0_2) in_time_point_2
	$(PYTHON) scripts/data_features.py $(EVENT_FILE) $(HIT_FILE) $(EVENT_WITH_HIT_FEATURES_FILE_0_3) in_time_point_3
	$(PYTHON) scripts/data_features.py $(EVENT_FILE) $(HIT_FILE) $(EVENT_WITH_HIT_FEATURES_FILE_0_4) in_time_point_4
	$(PYTHON) scripts/data_features.py $(EVENT_FILE) $(HIT_FILE) $(EVENT_WITH_HIT_FEATURES_FILE_0_5) in_time_point_5

$(SAMPLE_PARQUET_FILES): $(FULL_PARQUET_FILES)
	$(PYTHON) scripts/data_sample.py

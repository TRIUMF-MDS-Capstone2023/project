PYTHON = python
RM = rm

, := ,

# Paths

RICH_PMT_POSITIONS_NPY = data/rich_pmt_positions.npy
RICH_PMT_POSITIONS_DAT = data/rich_pmt_positions.dat

# - Full run (Run 11100)

RUN_H5_FILE = data/CaloRICH_Run11100_CTRL_v1.h5

RUN_EVENT_FILE = data/events.parquet
RUN_HIT_FILE = data/hits.parquet

RUN_EVENT_WITH_HIT_FEATURES_FILE_0_1 = data/events_with_hit_features_[cut_off_time=0.1].parquet
RUN_EVENT_WITH_HIT_FEATURES_FILE_0_2 = data/events_with_hit_features_[cut_off_time=0.2].parquet
RUN_EVENT_WITH_HIT_FEATURES_FILE_0_3 = data/events_with_hit_features_[cut_off_time=0.3].parquet
RUN_EVENT_WITH_HIT_FEATURES_FILE_0_4 = data/events_with_hit_features_[cut_off_time=0.4].parquet
RUN_EVENT_WITH_HIT_FEATURES_FILE_0_5 = data/events_with_hit_features_[cut_off_time=0.5].parquet
RUN_EVENT_WITH_HIT_FEATURES_FILE_0_6 = data/events_with_hit_features_[cut_off_time=0.6].parquet
RUN_EVENT_WITH_HIT_FEATURES_FILE_0_7 = data/events_with_hit_features_[cut_off_time=0.7].parquet
RUN_EVENT_WITH_HIT_FEATURES_FILE_0_8 = data/events_with_hit_features_[cut_off_time=0.8].parquet
RUN_EVENT_WITH_HIT_FEATURES_FILE_0_9 = data/events_with_hit_features_[cut_off_time=0.9].parquet
RUN_EVENT_WITH_HIT_FEATURES_FILE_1_0 = data/events_with_hit_features_[cut_off_time=1.0].parquet
RUN_EVENT_WITH_HIT_FEATURES_FILE_2_0 = data/events_with_hit_features_[cut_off_time=2.0].parquet
RUN_EVENT_WITH_HIT_FEATURES_FILE_3_0 = data/events_with_hit_features_[cut_off_time=3.0].parquet
RUN_EVENT_WITH_HIT_FEATURES_FILE_4_0 = data/events_with_hit_features_[cut_off_time=4.0].parquet
RUN_EVENT_WITH_HIT_FEATURES_FILE_5_0 = data/events_with_hit_features_[cut_off_time=5.0].parquet
RUN_EVENT_WITH_HIT_FEATURES_FILE_6_0 = data/events_with_hit_features_[cut_off_time=6.0].parquet
RUN_EVENT_WITH_HIT_FEATURES_FILE_7_0 = data/events_with_hit_features_[cut_off_time=7.0].parquet
RUN_EVENT_WITH_HIT_FEATURES_FILE_8_0 = data/events_with_hit_features_[cut_off_time=8.0].parquet
RUN_EVENT_WITH_HIT_FEATURES_FILE_9_0 = data/events_with_hit_features_[cut_off_time=9.0].parquet
RUN_EVENT_WITH_HIT_FEATURES_FILE_10_0 = data/events_with_hit_features_[cut_off_time=10.0].parquet

RUN_EVENT_WITH_HIT_FEATURES_FILES = \
	$(RUN_EVENT_WITH_HIT_FEATURES_FILE_0_1) \
	$(RUN_EVENT_WITH_HIT_FEATURES_FILE_0_2) \
	$(RUN_EVENT_WITH_HIT_FEATURES_FILE_0_3) \
	$(RUN_EVENT_WITH_HIT_FEATURES_FILE_0_4) \
	$(RUN_EVENT_WITH_HIT_FEATURES_FILE_0_5) \
	$(RUN_EVENT_WITH_HIT_FEATURES_FILE_0_6) \
	$(RUN_EVENT_WITH_HIT_FEATURES_FILE_0_7) \
	$(RUN_EVENT_WITH_HIT_FEATURES_FILE_0_8) \
	$(RUN_EVENT_WITH_HIT_FEATURES_FILE_0_9) \
	$(RUN_EVENT_WITH_HIT_FEATURES_FILE_1_0)

RUN_EVENT_WITH_HIT_FEATURES_FILES_EXTRA = \
	$(RUN_EVENT_WITH_HIT_FEATURES_FILE_2_0) \
	$(RUN_EVENT_WITH_HIT_FEATURES_FILE_3_0) \
	$(RUN_EVENT_WITH_HIT_FEATURES_FILE_4_0) \
	$(RUN_EVENT_WITH_HIT_FEATURES_FILE_5_0) \
	$(RUN_EVENT_WITH_HIT_FEATURES_FILE_6_0) \
	$(RUN_EVENT_WITH_HIT_FEATURES_FILE_7_0) \
	$(RUN_EVENT_WITH_HIT_FEATURES_FILE_8_0) \
	$(RUN_EVENT_WITH_HIT_FEATURES_FILE_9_0) \
	$(RUN_EVENT_WITH_HIT_FEATURES_FILE_10_0)

RUN_SAMPLE_EVENT_ID_FILE_5_45 = \
	data/sampled_event_ids_[muon,min_momentum=5,max_momentum=45].parquet
RUN_SAMPLE_EVENT_ID_FILE_10_45 = \
	data/sampled_event_ids_[muon,min_momentum=10,max_momentum=45].parquet
RUN_SAMPLE_EVENT_ID_FILE_15_45 = \
	data/sampled_event_ids_[muon,min_momentum=15,max_momentum=45].parquet
RUN_SAMPLE_EVENT_ID_FILE_20_45 = \
	data/sampled_event_ids_[muon,min_momentum=20,max_momentum=45].parquet

RUN_SAMPLE_EVENT_ID_FILES = \
	$(RUN_SAMPLE_EVENT_ID_FILE_5_45) \
	$(RUN_SAMPLE_EVENT_ID_FILE_10_45) \
	$(RUN_SAMPLE_EVENT_ID_FILE_15_45) \
	$(RUN_SAMPLE_EVENT_ID_FILE_20_45)

# - PNN filtered dataset

PNN_H5_FILE_2021A_AA = data/CaloRICH_93d0k1cx_CTRL_v1.h5
PNN_H5_FILE_2021A_AB = data/CaloRICH_YZbjqz_CTRL_v1.h5
PNN_H5_FILE_2021A_AC = data/CaloRICH_yxwNNN_CTRL_v1.h5

PNN_EVENT_FILE_2021A_AA = data/pnn_2021a/events_aa.parquet
PNN_EVENT_FILE_2021A_AB = data/pnn_2021a/events_ab.parquet
PNN_EVENT_FILE_2021A_AC = data/pnn_2021a/events_ac.parquet

PNN_HIT_FILE_2021A_AA = data/pnn_2021a/hits_aa.parquet
PNN_HIT_FILE_2021A_AB = data/pnn_2021a/hits_ab.parquet
PNN_HIT_FILE_2021A_AC = data/pnn_2021a/hits_ac.parquet

PNN_EVENT_FILE = data/pnn_2021a/events.parquet
PNN_HIT_FILE = data/pnn_2021a/hits.parquet

# `all` and `clean`

.PHONY : clean

all : \
	$(RICH_PMT_POSITIONS_NPY) \
	$(RUN_EVENT_FILE) \
	$(RUN_HIT_FILE) \
	$(RUN_EVENT_WITH_HIT_FEATURES_FILES) \
	$(RUN_SAMPLE_EVENT_ID_FILES)

full: \
	$(RICH_PMT_POSITIONS_NPY) \
	$(RUN_EVENT_FILE) \
	$(RUN_HIT_FILE) \
	$(RUN_EVENT_WITH_HIT_FEATURES_FILES) \
	$(RUN_EVENT_WITH_HIT_FEATURES_FILES_EXTRA) \
	$(RUN_SAMPLE_EVENT_ID_FILES)

rich_pmt_positions : $(RICH_PMT_POSITIONS_NPY)

events : $(RUN_EVENT_FILE)

hits : $(RUN_HIT_FILE)

event_with_hit_features : \
	$(RUN_EVENT_WITH_HIT_FEATURES_FILES) \
	$(RUN_EVENT_WITH_HIT_FEATURES_FILES_EXTRA)

sample_event_ids : $(RUN_SAMPLE_EVENT_ID_FILES)

clean :
	$(RM) \
		$(RICH_PMT_POSITIONS_NPY) \
		$(RUN_EVENT_FILE) \
		$(RUN_HIT_FILE) \
		$(RUN_EVENT_WITH_HIT_FEATURES_FILES) \
		$(RUN_EVENT_WITH_HIT_FEATURES_FILES_EXTRA) \
		$(RUN_SAMPLE_EVENT_ID_FILES)

# == Position map ==

$(RICH_PMT_POSITIONS_NPY): $(RICH_PMT_POSITIONS_DAT)
	$(PYTHON) scripts/rich_pmt_compile.py $(RICH_PMT_POSITIONS_DAT) $@

# == Events ==

$(RUN_EVENT_FILE) : $(RUN_H5_FILE)
	$(PYTHON) scripts/data_extract_events.py $(RUN_H5_FILE) $@

$(PNN_EVENT_FILE_2021A_AA) : $(PNN_H5_FILE_2021A_AA)
	$(PYTHON) scripts/data_extract_events.py $(PNN_H5_FILE_2021A_AA) $@

$(PNN_EVENT_FILE_2021A_AB) : $(PNN_H5_FILE_2021A_AB)
	$(PYTHON) scripts/data_extract_events.py $(PNN_H5_FILE_2021A_AB) $@

$(PNN_EVENT_FILE_2021A_AC) : $(PNN_H5_FILE_2021A_AC)
	$(PYTHON) scripts/data_extract_events.py $(PNN_H5_FILE_2021A_AC) $@

# == Hits ==

$(RUN_HIT_FILE) : $(RUN_H5_FILE) $(RUN_EVENT_FILE) $(RICH_PMT_POSITIONS_NPY)
	$(PYTHON) scripts/data_extract_hits.py $(RUN_H5_FILE) $(RUN_EVENT_FILE) $(RICH_PMT_POSITIONS_NPY) $@

$(PNN_HIT_FILE_2021A_AA) : $(PNN_H5_FILE_2021A_AA) $(PNN_EVENT_FILE_2021A_AA) $(RICH_PMT_POSITIONS_NPY)
	$(PYTHON) scripts/data_extract_hits.py $(PNN_H5_FILE_2021A_AA) $(PNN_EVENT_FILE_2021A_AA) $(RICH_PMT_POSITIONS_NPY) $@

$(PNN_HIT_FILE_2021A_AB) : $(PNN_H5_FILE_2021A_AB) $(PNN_EVENT_FILE_2021A_AB) $(RICH_PMT_POSITIONS_NPY)
	$(PYTHON) scripts/data_extract_hits.py $(PNN_H5_FILE_2021A_AB) $(PNN_EVENT_FILE_2021A_AB) $(RICH_PMT_POSITIONS_NPY) $@

$(PNN_HIT_FILE_2021A_AC) : $(PNN_H5_FILE_2021A_AC) $(PNN_EVENT_FILE_2021A_AC) $(RICH_PMT_POSITIONS_NPY)
	$(PYTHON) scripts/data_extract_hits.py $(PNN_H5_FILE_2021A_AC) $(PNN_EVENT_FILE_2021A_AC) $(RICH_PMT_POSITIONS_NPY) $@

# == Event with hit features ==

$(RUN_EVENT_WITH_HIT_FEATURES_FILES) $(RUN_EVENT_WITH_HIT_FEATURES_FILES_EXTRA) : $(RUN_EVENT_FILE) $(RUN_HIT_FILE)
	$(PYTHON) scripts/data_features.py \
		$(RUN_EVENT_FILE) \
		$(RUN_HIT_FILE) \
		$@ \
		$(word 1,$(subst ], ,$(word 2,$(subst =, ,$@))))

# == Sample event IDs ==

$(RUN_SAMPLE_EVENT_ID_FILES) : $(RUN_EVENT_FILE)
	$(PYTHON) scripts/data_sample.py \
		$(RUN_EVENT_FILE) \
		$(word 2,$(subst =, ,$(word 2,$(subst $(,), ,$@)))) \
		$(word 1,$(subst ], ,$(word 3,$(subst =, ,$@)))) \
		$@

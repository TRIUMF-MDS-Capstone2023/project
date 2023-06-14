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

RUN_POINTNET_FILE_0_5_10 = \
	data/point_net_[cut_off_time=0.5,sample_size=10].parquet
RUN_POINTNET_FILE_0_5_30 = \
	data/point_net_[cut_off_time=0.5,sample_size=30].parquet
RUN_POINTNET_FILE_0_5_50 = \
	data/point_net_[cut_off_time=0.5,sample_size=50].parquet
RUN_POINTNET_FILE_0_5_80 = \
	data/point_net_[cut_off_time=0.5,sample_size=80].parquet
RUN_POINTNET_FILE_0_5_100 = \
	data/point_net_[cut_off_time=0.5,sample_size=100].parquet

RUN_POINTNET_FILES = \
	$(RUN_POINTNET_FILE_0_5_10) \
	$(RUN_POINTNET_FILE_0_5_30) \
	$(RUN_POINTNET_FILE_0_5_50)

RUN_POINTNET_FILES_EXTRA = \
	$(RUN_POINTNET_FILE_0_5_80) \
	$(RUN_POINTNET_FILE_0_5_100)

# - PNN filtered dataset

PNN_H5_FILE_2021A_AA = data/CaloRICH_93d0k1cx_CTRL_v1.h5
PNN_H5_FILE_2021A_AB = data/CaloRICH_YZbjqz_CTRL_v1.h5
PNN_H5_FILE_2021A_AC = data/CaloRICH_yxwNNN_CTRL_v1.h5

PNN_EVENT_FILE = data/pnn_2021a/events.parquet
PNN_HIT_FILE = data/pnn_2021a/hits.parquet

PNN_EVENT_FILE_2021A_AA = data/pnn_2021a/events_aa.parquet
PNN_EVENT_FILE_2021A_AB = data/pnn_2021a/events_ab.parquet
PNN_EVENT_FILE_2021A_AC = data/pnn_2021a/events_ac.parquet

PNN_HIT_FILE_2021A_AA = data/pnn_2021a/hits_aa.parquet
PNN_HIT_FILE_2021A_AB = data/pnn_2021a/hits_ab.parquet
PNN_HIT_FILE_2021A_AC = data/pnn_2021a/hits_ac.parquet

PNN_EVENT_WITH_HIT_FEATURES_FILE_0_1 = data/pnn_2021a/events_with_hit_features_[cut_off_time=0.1].parquet
PNN_EVENT_WITH_HIT_FEATURES_FILE_0_2 = data/pnn_2021a/events_with_hit_features_[cut_off_time=0.2].parquet
PNN_EVENT_WITH_HIT_FEATURES_FILE_0_3 = data/pnn_2021a/events_with_hit_features_[cut_off_time=0.3].parquet
PNN_EVENT_WITH_HIT_FEATURES_FILE_0_4 = data/pnn_2021a/events_with_hit_features_[cut_off_time=0.4].parquet
PNN_EVENT_WITH_HIT_FEATURES_FILE_0_5 = data/pnn_2021a/events_with_hit_features_[cut_off_time=0.5].parquet
PNN_EVENT_WITH_HIT_FEATURES_FILE_0_6 = data/pnn_2021a/events_with_hit_features_[cut_off_time=0.6].parquet
PNN_EVENT_WITH_HIT_FEATURES_FILE_0_7 = data/pnn_2021a/events_with_hit_features_[cut_off_time=0.7].parquet
PNN_EVENT_WITH_HIT_FEATURES_FILE_0_8 = data/pnn_2021a/events_with_hit_features_[cut_off_time=0.8].parquet
PNN_EVENT_WITH_HIT_FEATURES_FILE_0_9 = data/pnn_2021a/events_with_hit_features_[cut_off_time=0.9].parquet
PNN_EVENT_WITH_HIT_FEATURES_FILE_1_0 = data/pnn_2021a/events_with_hit_features_[cut_off_time=1.0].parquet

PNN_EVENT_WITH_HIT_FEATURES_FILES = \
	$(PNN_EVENT_WITH_HIT_FEATURES_FILE_0_1) \
	$(PNN_EVENT_WITH_HIT_FEATURES_FILE_0_2) \
	$(PNN_EVENT_WITH_HIT_FEATURES_FILE_0_3) \
	$(PNN_EVENT_WITH_HIT_FEATURES_FILE_0_4) \
	$(PNN_EVENT_WITH_HIT_FEATURES_FILE_0_5) \
	$(PNN_EVENT_WITH_HIT_FEATURES_FILE_0_6) \
	$(PNN_EVENT_WITH_HIT_FEATURES_FILE_0_7) \
	$(PNN_EVENT_WITH_HIT_FEATURES_FILE_0_8) \
	$(PNN_EVENT_WITH_HIT_FEATURES_FILE_0_9) \
	$(PNN_EVENT_WITH_HIT_FEATURES_FILE_1_0)

PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AA_0_1 = data/pnn_2021a/events_aa_with_hit_features_[cut_off_time=0.1].parquet
PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AA_0_2 = data/pnn_2021a/events_aa_with_hit_features_[cut_off_time=0.2].parquet
PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AA_0_3 = data/pnn_2021a/events_aa_with_hit_features_[cut_off_time=0.3].parquet
PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AA_0_4 = data/pnn_2021a/events_aa_with_hit_features_[cut_off_time=0.4].parquet
PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AA_0_5 = data/pnn_2021a/events_aa_with_hit_features_[cut_off_time=0.5].parquet
PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AA_0_6 = data/pnn_2021a/events_aa_with_hit_features_[cut_off_time=0.6].parquet
PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AA_0_7 = data/pnn_2021a/events_aa_with_hit_features_[cut_off_time=0.7].parquet
PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AA_0_8 = data/pnn_2021a/events_aa_with_hit_features_[cut_off_time=0.8].parquet
PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AA_0_9 = data/pnn_2021a/events_aa_with_hit_features_[cut_off_time=0.9].parquet
PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AA_1_0 = data/pnn_2021a/events_aa_with_hit_features_[cut_off_time=1.0].parquet

PNN_EVENT_WITH_HIT_FEATURES_FILES_2021A_AA = \
	$(PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AA_0_1) \
	$(PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AA_0_2) \
	$(PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AA_0_3) \
	$(PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AA_0_4) \
	$(PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AA_0_5) \
	$(PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AA_0_6) \
	$(PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AA_0_7) \
	$(PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AA_0_8) \
	$(PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AA_0_9) \
	$(PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AA_1_0)

PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AB_0_1 = data/pnn_2021a/events_ab_with_hit_features_[cut_off_time=0.1].parquet
PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AB_0_2 = data/pnn_2021a/events_ab_with_hit_features_[cut_off_time=0.2].parquet
PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AB_0_3 = data/pnn_2021a/events_ab_with_hit_features_[cut_off_time=0.3].parquet
PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AB_0_4 = data/pnn_2021a/events_ab_with_hit_features_[cut_off_time=0.4].parquet
PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AB_0_5 = data/pnn_2021a/events_ab_with_hit_features_[cut_off_time=0.5].parquet
PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AB_0_6 = data/pnn_2021a/events_ab_with_hit_features_[cut_off_time=0.6].parquet
PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AB_0_7 = data/pnn_2021a/events_ab_with_hit_features_[cut_off_time=0.7].parquet
PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AB_0_8 = data/pnn_2021a/events_ab_with_hit_features_[cut_off_time=0.8].parquet
PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AB_0_9 = data/pnn_2021a/events_ab_with_hit_features_[cut_off_time=0.9].parquet
PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AB_1_0 = data/pnn_2021a/events_ab_with_hit_features_[cut_off_time=1.0].parquet

PNN_EVENT_WITH_HIT_FEATURES_FILES_2021A_AB = \
	$(PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AB_0_1) \
	$(PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AB_0_2) \
	$(PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AB_0_3) \
	$(PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AB_0_4) \
	$(PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AB_0_5) \
	$(PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AB_0_6) \
	$(PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AB_0_7) \
	$(PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AB_0_8) \
	$(PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AB_0_9) \
	$(PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AB_1_0)

PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AC_0_1 = data/pnn_2021a/events_ac_with_hit_features_[cut_off_time=0.1].parquet
PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AC_0_2 = data/pnn_2021a/events_ac_with_hit_features_[cut_off_time=0.2].parquet
PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AC_0_3 = data/pnn_2021a/events_ac_with_hit_features_[cut_off_time=0.3].parquet
PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AC_0_4 = data/pnn_2021a/events_ac_with_hit_features_[cut_off_time=0.4].parquet
PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AC_0_5 = data/pnn_2021a/events_ac_with_hit_features_[cut_off_time=0.5].parquet
PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AC_0_6 = data/pnn_2021a/events_ac_with_hit_features_[cut_off_time=0.6].parquet
PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AC_0_7 = data/pnn_2021a/events_ac_with_hit_features_[cut_off_time=0.7].parquet
PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AC_0_8 = data/pnn_2021a/events_ac_with_hit_features_[cut_off_time=0.8].parquet
PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AC_0_9 = data/pnn_2021a/events_ac_with_hit_features_[cut_off_time=0.9].parquet
PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AC_1_0 = data/pnn_2021a/events_ac_with_hit_features_[cut_off_time=1.0].parquet

PNN_EVENT_WITH_HIT_FEATURES_FILES_2021A_AC = \
	$(PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AC_0_1) \
	$(PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AC_0_2) \
	$(PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AC_0_3) \
	$(PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AC_0_4) \
	$(PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AC_0_5) \
	$(PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AC_0_6) \
	$(PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AC_0_7) \
	$(PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AC_0_8) \
	$(PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AC_0_9) \
	$(PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AC_1_0)

PNN_POINTNET_FILE_2021A_AA_0_5_10 = \
	data/pnn_2021a/point_net_aa_[cut_off_time=0.5,sample_size=10].parquet
PNN_POINTNET_FILE_2021A_AA_0_5_30 = \
	data/pnn_2021a/point_net_aa_[cut_off_time=0.5,sample_size=30].parquet
PNN_POINTNET_FILE_2021A_AA_0_5_50 = \
	data/pnn_2021a/point_net_aa_[cut_off_time=0.5,sample_size=50].parquet
PNN_POINTNET_FILE_2021A_AA_0_5_80 = \
	data/pnn_2021a/point_net_aa_[cut_off_time=0.5,sample_size=80].parquet
PNN_POINTNET_FILE_2021A_AA_0_5_100 = \
	data/pnn_2021a/point_net_aa_[cut_off_time=0.5,sample_size=100].parquet

PNN_POINTNET_FILES_2021A_AA = \
	$(PNN_POINTNET_FILE_2021A_AA_0_5_10) \
	$(PNN_POINTNET_FILE_2021A_AA_0_5_30) \
	$(PNN_POINTNET_FILE_2021A_AA_0_5_50)

PNN_POINTNET_FILES_EXTRA_2021A_AA = \
	$(PNN_POINTNET_FILE_2021A_AA_0_5_80) \
	$(PNN_POINTNET_FILE_2021A_AA_0_5_100)

PNN_POINTNET_FILE_2021A_AB_0_5_10 = \
	data/pnn_2021a/point_net_ab_[cut_off_time=0.5,sample_size=10].parquet
PNN_POINTNET_FILE_2021A_AB_0_5_30 = \
	data/pnn_2021a/point_net_ab_[cut_off_time=0.5,sample_size=30].parquet
PNN_POINTNET_FILE_2021A_AB_0_5_50 = \
	data/pnn_2021a/point_net_ab_[cut_off_time=0.5,sample_size=50].parquet
PNN_POINTNET_FILE_2021A_AB_0_5_80 = \
	data/pnn_2021a/point_net_ab_[cut_off_time=0.5,sample_size=80].parquet
PNN_POINTNET_FILE_2021A_AB_0_5_100 = \
	data/pnn_2021a/point_net_ab_[cut_off_time=0.5,sample_size=100].parquet

PNN_POINTNET_FILES_2021A_AB = \
	$(PNN_POINTNET_FILE_2021A_AB_0_5_10) \
	$(PNN_POINTNET_FILE_2021A_AB_0_5_30) \
	$(PNN_POINTNET_FILE_2021A_AB_0_5_50)

PNN_POINTNET_FILES_EXTRA_2021A_AB = \
	$(PNN_POINTNET_FILE_2021A_AB_0_5_80) \
	$(PNN_POINTNET_FILE_2021A_AB_0_5_100)

PNN_POINTNET_FILE_2021A_AC_0_5_10 = \
	data/pnn_2021a/point_net_ac_[cut_off_time=0.5,sample_size=10].parquet
PNN_POINTNET_FILE_2021A_AC_0_5_30 = \
	data/pnn_2021a/point_net_ac_[cut_off_time=0.5,sample_size=30].parquet
PNN_POINTNET_FILE_2021A_AC_0_5_50 = \
	data/pnn_2021a/point_net_ac_[cut_off_time=0.5,sample_size=50].parquet
PNN_POINTNET_FILE_2021A_AC_0_5_80 = \
	data/pnn_2021a/point_net_ac_[cut_off_time=0.5,sample_size=80].parquet
PNN_POINTNET_FILE_2021A_AC_0_5_100 = \
	data/pnn_2021a/point_net_ac_[cut_off_time=0.5,sample_size=100].parquet

PNN_POINTNET_FILES_2021A_AC = \
	$(PNN_POINTNET_FILE_2021A_AC_0_5_10) \
	$(PNN_POINTNET_FILE_2021A_AC_0_5_30) \
	$(PNN_POINTNET_FILE_2021A_AC_0_5_50)

PNN_POINTNET_FILES_EXTRA_2021A_AC = \
	$(PNN_POINTNET_FILE_2021A_AC_0_5_80) \
	$(PNN_POINTNET_FILE_2021A_AC_0_5_100)

PNN_POINTNET_FILE_0_5_10 = \
	data/pnn_2021a/point_net_[cut_off_time=0.5,sample_size=10].parquet
PNN_POINTNET_FILE_0_5_30 = \
	data/pnn_2021a/point_net_[cut_off_time=0.5,sample_size=30].parquet
PNN_POINTNET_FILE_0_5_50 = \
	data/pnn_2021a/point_net_[cut_off_time=0.5,sample_size=50].parquet
PNN_POINTNET_FILE_0_5_80 = \
	data/pnn_2021a/point_net_[cut_off_time=0.5,sample_size=80].parquet
PNN_POINTNET_FILE_0_5_100 = \
	data/pnn_2021a/point_net_[cut_off_time=0.5,sample_size=100].parquet

PNN_POINTNET_FILES = \
	$(PNN_POINTNET_FILE_0_5_10) \
	$(PNN_POINTNET_FILE_0_5_30) \
	$(PNN_POINTNET_FILE_0_5_50)

PNN_POINTNET_FILES_EXTRA = \
	$(PNN_POINTNET_FILE_0_5_80) \
	$(PNN_POINTNET_FILE_0_5_100)

# `all` and `clean`

.PHONY : clean

all : \
	run-all \
	pnn-all

full : \
	run-full \
	pnn-full

rich_pmt_positions : $(RICH_PMT_POSITIONS_NPY)

run-all : \
	run-events \
	run-hits \
	run-sample_event_ids \
	$(RUN_POINTNET_FILES) \
	$(RUN_EVENT_WITH_HIT_FEATURES_FILES)

run-full: \
	run-all \
	$(RUN_POINTNET_FILES_EXTRA)
	$(RUN_EVENT_WITH_HIT_FEATURES_FILES_EXTRA)

run-events : $(RUN_EVENT_FILE)

run-hits : $(RUN_HIT_FILE)

run-event_with_hit_features : \
	$(RUN_EVENT_WITH_HIT_FEATURES_FILES) \
	$(RUN_EVENT_WITH_HIT_FEATURES_FILES_EXTRA)

run-sample_event_ids : $(RUN_SAMPLE_EVENT_ID_FILES)

run-pointnet : \
	$(RUN_POINTNET_FILES)
	$(RUN_POINTNET_FILES_EXTRA)

pnn-all : \
	pnn-events \
	pnn-hits \
	pnn-event_with_hit_features \
	$(PNN_POINTNET_FILES)

pnn-full: \
	pnn-all \
	$(PNN_POINTNET_FILES_EXTRA)

pnn-events : $(PNN_EVENT_FILE)

pnn-hits : $(PNN_HIT_FILE)

pnn-event_with_hit_features : \
	$(PNN_EVENT_WITH_HIT_FEATURES_FILES)

pnn-pointnet : \
	$(PNN_POINTNET_FILES) \
	$(PNN_POINTNET_FILES_EXTRA)

clean :
	$(RM) \
		$(RICH_PMT_POSITIONS_NPY) \
		$(RUN_EVENT_FILE) \
		$(RUN_HIT_FILE) \
		$(RUN_EVENT_WITH_HIT_FEATURES_FILES) \
		$(RUN_EVENT_WITH_HIT_FEATURES_FILES_EXTRA) \
		$(RUN_SAMPLE_EVENT_ID_FILES) \
		$(RUN_POINTNET_FILES) \
		$(PNN_EVENT_FILE) \
		$(PNN_HIT_FILE) \
		$(PNN_EVENT_WITH_HIT_FEATURES_FILES) \
		$(PNN_EVENT_WITH_HIT_FEATURES_FILES_2021A_AA) \
		$(PNN_EVENT_WITH_HIT_FEATURES_FILES_2021A_AB) \
		$(PNN_EVENT_WITH_HIT_FEATURES_FILES_2021A_AC) \
		$(PNN_POINTNET_FILES)

# == Position map ==

$(RICH_PMT_POSITIONS_NPY): $(RICH_PMT_POSITIONS_DAT)
	$(PYTHON) scripts/rich_pmt_compile.py $(RICH_PMT_POSITIONS_DAT) $@

# == Events ==

$(RUN_EVENT_FILE) : $(RUN_H5_FILE)
	$(PYTHON) scripts/data_extract_events.py $(RUN_H5_FILE) $@

$(PNN_EVENT_FILE) : $(PNN_H5_FILE_2021A_AA) $(PNN_H5_FILE_2021A_AB) $(PNN_H5_FILE_2021A_AC)
	$(PYTHON) scripts/data_merge.py $(PNN_H5_FILE_2021A_AA) $(PNN_H5_FILE_2021A_AB) $(PNN_H5_FILE_2021A_AC) $@

$(PNN_EVENT_FILE_2021A_AA) : $(PNN_H5_FILE_2021A_AA)
	$(PYTHON) scripts/data_extract_events.py $(PNN_H5_FILE_2021A_AA) $@

$(PNN_EVENT_FILE_2021A_AB) : $(PNN_H5_FILE_2021A_AB)
	$(PYTHON) scripts/data_extract_events.py $(PNN_H5_FILE_2021A_AB) $@

$(PNN_EVENT_FILE_2021A_AC) : $(PNN_H5_FILE_2021A_AC)
	$(PYTHON) scripts/data_extract_events.py $(PNN_H5_FILE_2021A_AC) $@

# == Hits ==

$(RUN_HIT_FILE) : $(RUN_H5_FILE) $(RUN_EVENT_FILE) $(RICH_PMT_POSITIONS_NPY)
	$(PYTHON) scripts/data_extract_hits.py $(RUN_H5_FILE) $(RUN_EVENT_FILE) $(RICH_PMT_POSITIONS_NPY) $@

$(PNN_HIT_FILE) : $(PNN_HIT_FILE_2021A_AA) $(PNN_HIT_FILE_2021A_AB) $(PNN_HIT_FILE_2021A_AC)
	$(PYTHON) scripts/data_merge.py $(PNN_HIT_FILE_2021A_AA) $(PNN_HIT_FILE_2021A_AB) $(PNN_HIT_FILE_2021A_AC) $@

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

$(PNN_EVENT_WITH_HIT_FEATURES_FILES) : $(PNN_EVENT_WITH_HIT_FEATURES_FILES_2021_AA) $(PNN_EVENT_WITH_HIT_FEATURES_FILES_2021_AB) $(PNN_EVENT_WITH_HIT_FEATURES_FILES_2021_AC)
	$(PYTHON) scripts/data_merge.py \
		$(subst events,events_aa,$@) \
		$(subst events,events_ab,$@) \
		$(subst events,events_ac,$@) \
		$@

$(PNN_EVENT_WITH_HIT_FEATURES_FILES_2021A_AA) : $(PNN_EVENT_FILE_2021A_AA) $(PNN_HIT_FILE_2021A_AA)
	$(PYTHON) scripts/data_features.py \
		$(PNN_EVENT_FILE_2021A_AA) \
		$(PNN_HIT_FILE_2021A_AA) \
		$@ \
		$(word 1,$(subst ], ,$(word 2,$(subst =, ,$@))))

$(PNN_EVENT_WITH_HIT_FEATURES_FILES_2021A_AB) : $(PNN_EVENT_FILE_2021A_AB) $(PNN_HIT_FILE_2021A_AB)
	$(PYTHON) scripts/data_features.py \
		$(PNN_EVENT_FILE_2021A_AB) \
		$(PNN_HIT_FILE_2021A_AB) \
		$@ \
		$(word 1,$(subst ], ,$(word 2,$(subst =, ,$@))))

$(PNN_EVENT_WITH_HIT_FEATURES_FILES_2021A_AC) : $(PNN_EVENT_FILE_2021A_AC) $(PNN_HIT_FILE_2021A_AC)
	$(PYTHON) scripts/data_features.py \
		$(PNN_EVENT_FILE_2021A_AC) \
		$(PNN_HIT_FILE_2021A_AC) \
		$@ \
		$(word 1,$(subst ], ,$(word 2,$(subst =, ,$@))))

# == Sample event IDs ==

$(RUN_SAMPLE_EVENT_ID_FILES) : $(RUN_EVENT_FILE)
	$(PYTHON) scripts/data_sample.py \
		$(RUN_EVENT_FILE) \
		$(word 2,$(subst =, ,$(word 2,$(subst $(,), ,$@)))) \
		$(word 1,$(subst ], ,$(word 3,$(subst =, ,$@)))) \
		$@

# == PointNet ==

$(RUN_POINTNET_FILES) : $(RUN_EVENT_WITH_HIT_FEATURES_FILE_0_5) $(RUN_HIT_FILE)
	$(PYTHON) scripts/wrangle_point_net.py \
		$(RUN_EVENT_WITH_HIT_FEATURES_FILE_0_5) \
		$(RUN_HIT_FILE) \
		$(word 1,$(subst ], ,$(word 3,$(subst =, ,$@)))) \
		$@

$(PNN_POINTNET_FILES) : $(PNN_POINTNET_FILES_2021A_AA) $(PNN_POINTNET_FILES_2021A_AB) $(PNN_POINTNET_FILES_2021A_AC)
	$(PYTHON) scripts/data_merge.py \
		$(subst point_net,point_net_aa,$@) \
		$(subst point_net,point_net_ab,$@) \
		$(subst point_net,point_net_ac,$@) \
		$@

$(PNN_POINTNET_FILES_EXTRA) : $(PNN_POINTNET_FILES_EXTRA_2021A_AA) $(PNN_POINTNET_FILES_EXTRA_2021A_AB) $(PNN_POINTNET_FILES_EXTRA_2021A_AC)
	$(PYTHON) scripts/data_merge.py \
		$(subst point_net,point_net_aa,$@) \
		$(subst point_net,point_net_ab,$@) \
		$(subst point_net,point_net_ac,$@) \
		$@

$(PNN_POINTNET_FILES_2021A_AA) : $(PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AA_0_5) $(PNN_HIT_FILE_2021A_AA)
	$(PYTHON) scripts/wrangle_point_net.py \
		$(PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AA_0_5) \
		$(PNN_HIT_FILE_2021A_AA) \
		$(word 1,$(subst ], ,$(word 3,$(subst =, ,$@)))) \
		$@

$(PNN_POINTNET_FILES_2021A_AB) : $(PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AB_0_5) $(PNN_HIT_FILE_2021A_AB)
	$(PYTHON) scripts/wrangle_point_net.py \
		$(PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AB_0_5) \
		$(PNN_HIT_FILE_2021A_AB) \
		$(word 1,$(subst ], ,$(word 3,$(subst =, ,$@)))) \
		$@

$(PNN_POINTNET_FILES_2021A_AC) : $(PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AC_0_5) $(PNN_HIT_FILE_2021A_AC)
	$(PYTHON) scripts/wrangle_point_net.py \
		$(PNN_EVENT_WITH_HIT_FEATURES_FILE_2021A_AC_0_5) \
		$(PNN_HIT_FILE_2021A_AC) \
		$(word 1,$(subst ], ,$(word 3,$(subst =, ,$@)))) \
		$@

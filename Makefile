PYTHON = python
RM = rm

H5_FILE = data/CaloRICH_Run11100_CTRL_v1.h5

RICH_PMT_POSITIONS_NPY = data/rich_pmt_positions.npy
RICH_PMT_POSITIONS_DAT = data/rich_pmt_positions.dat

FULL_PARQUET_FILES = \
	data/full_events.parquet \
	data/full_hits.parquet

SAMPLE_PARQUET_FILES = \
	data/sampled_events.parquet \
	data/sampled_hits.parquet

.PHONY : clean

all : \
	$(RICH_PMT_POSITIONS_NPY) \
	$(FULL_PARQUET_FILES) \
	$(SAMPLE_PARQUET_FILES)

clean :
	$(RM) \
		$(RICH_PMT_POSITIONS_NPY) \
		$(FULL_PARQUET_FILES) \
		$(SAMPLE_PARQUET_FILES)

$(RICH_PMT_POSITIONS_NPY): $(RICH_PMT_POSITIONS_DAT)
	$(PYTHON) scripts/rich_pmt_compile.py $(RICH_PMT_POSITIONS_DAT) $(RICH_PMT_POSITIONS_NPY)

$(FULL_PARQUET_FILES): $(H5_FILE)
	$(PYTHON) scripts/data_extract.py

$(SAMPLE_PARQUET_FILES): $(FULL_PARQUET_FILES)
	$(PYTHON) scripts/data_sample.py

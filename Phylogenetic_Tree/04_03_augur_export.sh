#!/bin/bash

# PARAMS ---
PROJECT_PREFIX=sarscov2_npl

# DEFINE PATHS ---
DIR_WRK=/home/himanshu/covseq/sarscov2_genome_nepal
DIR_METADATA=${DIR_WRK}/metadata/metadata_curated
DIR_MAPS=${DIR_WRK}/data/maps
DIR_ANALYSIS=${DIR_WRK}/analysis/05_nextstrain
DIR_INPUT=${DIR_ANALYSIS}/tree
DIR_OUTPUT=${DIR_ANALYSIS}/auspice_tree

# DEFINE FILES FOR ANALYSIS ---
FILE_METADATA=${DIR_METADATA}/metadata_nextstrain.tsv
FILE_COLORS=${DIR_MAPS}/nextstrain_npl_colors.tsv
FILE_LATLONG=${DIR_MAPS}/nextstrain_npl_lat_long.tsv
FILE_CONFIG=${DIR_WRK}/data/nextstrain/auspice/auspice_npl_config.json
FILE_TREE=${DIR_INPUT}/${PROJECT_PREFIX}_tree.nwk
FILE_NODE_DATA_1=${DIR_INPUT}/${PROJECT_PREFIX}_branch_lengths.json
FILE_NODE_DATA_2=${DIR_INPUT}/${PROJECT_PREFIX}_traits.json
FILE_NODE_DATA_3=${DIR_INPUT}/${PROJECT_PREFIX}_nt_muts.json
FILE_NODE_DATA_4=${DIR_INPUT}/${PROJECT_PREFIX}_aa_muts.json
FILE_OUTPUT=${DIR_OUTPUT}/${PROJECT_PREFIX}.json

echo ${FILE_OUTPUT}

DT=$(date '+%Y-%m-%d %H:%M:%S');
echo ${DT} "[START] AUGUR EXPORT ..."

# AUGUR EXPORT ---
augur export v2 \
	--metadata ${FILE_METADATA} \
	--tree ${FILE_TREE} \
	--node-data ${FILE_NODE_DATA_1} \
		${FILE_NODE_DATA_2} \
		${FILE_NODE_DATA_3} \
		${FILE_NODE_DATA_4} \
	--colors ${FILE_COLORS} \
	--lat-longs ${FILE_LATLONG} \
	--auspice-config ${FILE_CONFIG} \
	--output ${FILE_OUTPUT}

DT=$(date '+%Y-%m-%d %H:%M:%S');
echo ${DT} "[END] AUGUR EXPORT ..."

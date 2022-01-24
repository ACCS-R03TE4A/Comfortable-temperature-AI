#!/bin/bash
if [ -z $ACCS_HOME ]; then
  echo "[`date`] Please register ACCS_HOME as an environment variable first.ACCS_HOME is the absolute path of ACCS-SERVER." >&2
  exit -1
fi
echo "[`date`] The path to ACCS-SERVER is $ACCS_HOME."
cd $ACCS_HOME
source env/bin/activate
rm Learn.csv
python Comfortable_temperature_AI/scripts/learn_and_save.py
echo "[`date`] save model."
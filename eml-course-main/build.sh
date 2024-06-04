#!/bin/sh

# Prompt the user to proceed with processing
read -p "Sensor data captured. Do you want to proceed with processing? (yes/no) " user_input

if [ "$user_input" = "yes" ]; then
    echo "Proceeding with data processing..."

    i=1
    for csvfile in ./tools/data/captured/*.csv; do
        cut -d ',' -f 1-11 "$csvfile" > ./tools/data/preprocessed/filters/$i.csv
        awk -F, 'NR==1 || ($4>=500 || $5>=500 || $6>=500 || $7>=500 || $8>=500 || $9>=500 || $10>=500 || $11>=500)' ./tools/data/preprocessed/filters/$i.csv > ./tools/data/preprocessed/normalizations/$i.csv
        echo "$csvfile $i"
        i=$((i+1))
    done

    echo "The latest column (assumed to be 'tof measurement') has been removed from the CSV files."

    python3 ./tools/preprocessing/feature_selection/feature_functions.py

    python3 ./tools/preprocessing/feature_selection/feature_functions_c2dll.py

    python3 ./tools/preprocessing/feature_selection/feature_calculator.py

    # Check if the processing script executed successfully
    if [ $? -ne 0 ]; then
        echo "Data processing failed."
        exit 1
    else
        echo "Data processing completed successfully."
    fi
else
    echo "Processing aborted by the user."
    exit 1
fi

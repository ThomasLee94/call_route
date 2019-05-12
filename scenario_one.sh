#!/usr/bin/env bash

Assign phone number and file path to rout-costs-<>.txt
PHONENUM=${1?Error: no phone number given}
FILE=${2?Error: file path not given}
grep "${PHONENUM:0:9}" $FILE

# if exact match is not found (exit code), cut phone number to first 5 digits
if (($?));
    then grep -w "${PHONENUM:0:7}" $FILE;
fi 

# if match is not found after 2 checks, phone number does not exist in file
if (($?));
    then echo "Phone number is not in provided file";
fi


# Scenario One bash script

## How to use

``` 
bash scenario_one.sh <PHONENUM> <FILE_PATH>
```
This will return the prefix and cost of matching number

PHONENUM is any number including the '+' at the very start.
FILE is the path to the file containing the prefix and cost.

## Example

``` 
$ bash scenario_one.sh +4979448939 ../data/route-costs-35000.txt
    => +4979448939,0.48 # Returns prefix and cost
```


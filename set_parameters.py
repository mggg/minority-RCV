import os
import datetime
now = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

### User-Chosen Parameters ###
parameters = {
  "locality_tag":"chelan",
  "race_tag":"POC_CVAP",
  "poc_cvaps":[0.193, 0.227],
  "support_for_POC":[
    [0.95, 0.05], # [POC for POC, White for POC]
    [0.75, 0.20],
    [0.60, 0.40]
  ],
  "seats":[
    [3, 3, 3], # [seats open, C-cands, W-cands]
    [5, 5, 5],
    [7, 7, 7]
  ]
}

### Setting up output folders and metadata file ###
output_path = f'outputs/{now}_{parameters["locality_tag"]}_{parameters["race_tag"]}'
metadata_path = f'{output_path}/metadata.txt'
os.system('echo Creating an output folder for these parameters...')
os.system(f'mkdir -p {output_path}') # think about how to re-do runs...
os.system(f"echo 'This folder contains RCV analyses made from the following parameters:\n' >> {metadata_path}")

for varname, var in parameters.items():
  os.system(f"echo '{varname} = {var}' >> {metadata_path}")
os.system(f"echo '\n'Output files will be named like: poc-cvaps_POC-support-for-POC_White-support-for-POC_seats-open_num-C-cands_num-W-Cands.csv'\n' >> {metadata_path}")

### Running RCV analyses ###
for support_for_POC in parameters['support_for_POC']:
  for seats in parameters['seats']:
    for poc_cvaps in parameters['poc_cvaps']:
      RCV_run = f'{poc_cvaps}_{support_for_POC[0]}_{support_for_POC[1]}_{seats[0]}_{seats[1]}_{seats[2]}'
      analysis_path = f'{output_path}/{RCV_run}.csv'
      os.system(f"sbatch runcityargs.sh {RCV_run} {analysis_path}")

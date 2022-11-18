from pprint import pprint

import yaml

# Read YAML file
with open("/srv/configs/configs/raw/pobeda_delivery.yaml", 'r') as stream:
    config = yaml.safe_load(stream)

pprint(config)
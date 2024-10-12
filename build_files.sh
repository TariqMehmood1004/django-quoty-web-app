echo "BUILD START"

#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Collect static files
python3 manage.py collectstatic --noinput


 echo "BUILD END"
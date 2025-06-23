# In any of Cloud Shell folders, create a new folder called venv, install the venv package, and activate it:
mkdir venv
cd venv
python3 -m venv beam-env
source beam-env/bin/activate

# After running these commands, Python will use the dedicated environment for our Beam program.

# To install the apache-beam package WITHIN the environment:
pip install --upgrade pip
pip install wheel
# pip install 'apache-beam[gcp]==2.49.0'
# pip install apache-beam
pip install 'apache-beam[gcp]'
cd ~/scripts # [your hello world python code directory]

# declare environment variables
export PROJECT_ID=formal-vertex-463708-q6
export REGION=us-central1
export BUCKET_NAME=logs-bus-trips

# Run the Beam application:
python3 beam_helloworld.py \
    --project=$PROJECT_ID \
    --region=$REGION \
    --runner=DirectRunner \
    --temp_location=gs://$BUCKET_NAME/dataflow/temp

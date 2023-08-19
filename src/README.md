# src/README.md

### Environment
```bash
# Create a Conda Environment with Python 3.8 (or the desired version)
conda create --name env_name python=3.8

# Activate the Conda Environment
conda activate env_name

# (Optional) Deactivate the Conda Environment when finished
conda deactivate
```
> Note: Replace `env_name` with the desired name for your environment.

### Version
```bash
# Check the Python Version to Verify the Environment
python --version
```

### Run
```bash
# With the environment activated, run the script
python src/image_to_base64.py images/ output output/README.md
```
- Replace `images/` with the desired input directory.
- Replace `output` with the desired output directory.
- Replace `output/README.md` with the desired output file. The output file will be created if it does not already exist.

### Dependencies
```bash
# Install the Required Packages
pip install pandas numpy matplotlib sklearn psutil
```

### Usage
```bash
conda activate env_name
python src/plot_undernourished_stats.py  
python src/transform_data.py
```

# Mlops-project

## Conda 
```bash
# create Environment
conda create -n environment_name python==Version -y 

# Activate and Deactivate conda environment. 
conda activate env_path 
conda deactivate

# delete environment
conda env remove -n "environment_name"
conda env remove -p "Path_of_environment"
```


```bash
# Setting the aws access key and secret key in environment variable. 
export AWS_ACCESS_KEY_ID=your_access_key_id
export AWS_SECRET_ACCESS_KEY=your_secret_access_key
export AWS_DEFAULT_REGION=your_preferred_region

# To check the environment variable set or not
echo $AWS_ACCESS_KEY_ID

# To unset the environment variable. 
unset AWS_ACCESS_KEY_ID
```
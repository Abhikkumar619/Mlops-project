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


# Docker setup in EC2 instance. 

sudo apt-get update -y
sudo apt-get upgrade
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

# Next step is to connect Github with EC2(Self hosted runner):
- select your project on Github >> go to settings >> Actions >> Runner >> New self hosted runner
- Select OS (Linux) >> Now step by step run all "Download" related commands on EC2 server 
- run first "Configure" command (hit enter instead of setting a runner group, runner name: self-hosted)
- enter any additional label (hit enter to skip) >> name of work folder (again hit enter)
- Now run second "Configure" command (./run.sh) and runner will get connected to Github
- To crosscheck, go back to Github and click on Runner and you will see runner state as "idle"
- If you do ctrl+c on EC2 server then runner will shut then restart with "./run.sh"


# Setup your Github secrets: (Github project>Settings>SecretandVariable>Actions>NewRepoSecret)
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_DEFAULT_REGION
- ECR_REPO
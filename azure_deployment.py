import os.path
from deployer import Deployer
from azure.profiles import KnownProfiles

# This script expects that the following environment vars are set:
#
# AZURE_TENANT_ID: with your Azure Active Directory tenant id or domain
# AZURE_CLIENT_ID: with your Azure Active Directory Application Client ID
# AZURE_CLIENT_SECRET: with your Azure Active Directory Application Secret
# ARM_ENDPOINT: your Resource Manager Endpoint
# AZURE_SUBSCRIPTION_ID: your subscription id
# AZURE_RESOURCE_LOCATION: with your azure stack resource location
# this example assumes your ssh public key present here: ~/id_rsa.pub

my_subscription_id = os.environ.get(
    'AZURE_SUBSCRIPTION_ID')   # your Azure Subscription Id
# the resource group for deployment
my_resource_group = 'azure-python-deployment-sample'
# the path to your rsa public key file
my_pub_ssh_key_path = os.path.expanduser('~/id_rsa.pub')

# Set Azure stack supported API profile as the default profile
KnownProfiles.default.use(KnownProfiles.v2018_03_01_hybrid)

msg = "\nInitializing the Deployer class with subscription id: {}, resource group: {}" \
    "\nand public key located at: {}...\n\n"
msg = msg.format(my_subscription_id, my_resource_group, my_pub_ssh_key_path)
print(msg)

# Initialize the deployer class
deployer = Deployer(my_subscription_id, my_resource_group, my_pub_ssh_key_path)

print("Beginning the deployment... \n\n")
# Deploy the template
my_deployment = deployer.deploy()

print("Done deploying!!\n\nYou can connect via: `ssh azureSample@{}.local.cloudapp.azurestack.external`".format(
    deployer.dns_label_prefix))

# Destroy the resource group which contains the deployment
# deployer.destroy()

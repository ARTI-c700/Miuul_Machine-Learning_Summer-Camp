# # List of Virtual Environments
# conda env list

# # Create a custom Virtual Environment
# conda create -n <env-name>

# # For Deleting
# conda env remove -n <env-name>

# # List of packets in any environments
# conda list

# # Install package
# pip install <package_name>
# conda install numpy scipy pandas
# OR
# conda install numpy=1.20.1
# pip install numpy==1.20.1


# # removing a package
# conda remove package_name

# # Updating a package
# conda upgrade -all
# conda upgrade <package_name>

# # Transferring environment packages into different one
# conda env export > environment.yaml

# # Creating an environment from the base
# conda env create -f <document_name>

Skippy CLI
==========


Build & Install
---------------

Run

    make install
    source .venv/bin/activate

Then use

    skippy
    
Config 

create skippy.yml in your 
    
    <openfaas-function-yaml>/skippy.yml
    data-api-demo/skippy.yml 
    
accepted labels:

    data:
      consume:
        - mybucket.myfile1
        - mybucket.myfile2
      produce:
        - mybucket.myfile1
    policy:
      capability: gpu
     

openfaas limitations : labels must consist of alphanumeric characters, '-', '_' and must start and end with an alphanumeric character
skippy: '.' should be only used for bucket.file.txt delimitation and extension. File extension must be present. 

Deploy 

    skippy deploy <openfaas-function-yaml>
    skippy deploy data-api-demo.yml 
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
     
Deploy 

    skippy deploy <openfaas-function-yaml>
    skippy deploy data-api-demo.yml 
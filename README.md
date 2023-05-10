# CloudProject
The final project for CPSC415- Building Cloud Native apps

***Statement of the project application nature and purpose*** 

The project will be built using microservice, it will host a website application that allow user to input images and will auto caption the image.
The user will also help evaluate the performance of the model and the result will be stored for further analysis.

***Statement of team members that may be just yourself or with a partner*** 

Yicheng Zhu

***Statement of the estimated modules*** 

A front-end website will serve as the graphic interface and I/O. The image caption generator https://ml-exchange.org/models/max-image-caption-generator will be consisted in another module. A rating/evaluation model will handle the evaluation process from the user and collect the data.

***Statement of the estimated languages and frameworks*** 

The frontend might be written in C# and xml. The rest will be written in python.

***General description of the UI with the primary actions*** 

The UI will have a canvas to show the image uploaded by the user, and will have the predicton caption shown in a label. Several buttons will be there for image upload and clear/reset. The evaluation collection bar will be available when there is a prediction being generated, and assoicated with that there will be a submit button.

***Expect all of the above to change and evolve, this is just to kickstart.*** 

----------------------------------------------------------------------------

![alt text](https://github.com/Mayonezyck/CloudProject/blob/main/Gitreadme/structure.png)

## Instruction of Using (image:051000)

On GKE, run the all-in-one manifest file

>cd kubernetes
>kubectl apply -f apply_all.yaml
>kubectl get all

find the external ip for service/max-image-front-service
open a browser and enter its port 5000



## Logs 
2023-05-09

The image is now implemented with kubernetes API, roles are set.
The image version is 051000 now.
The auto-routing is acheived by config map!


2023-05-07

By the time this note is written, the repo have the for front-end microservice written in python.

In the folder called flask, that is a python virtual env has the dependencies.

The UI folder has all the .html files that the website needs to visualize the output.

The kubernetes directory now contains only yaml to apply the max-image-caption generator. After finishing microservice 2, I will add it as well.

DOCKERFILE is used to make a docker image.

main.py is the only python file for the frontend microservice.

Currently, if the service is run directly from main.py, it works fine. However, if I tried to build and run through docker, it doesn't

The two services that make my project: 

    1. MAX-image-caption-generator, which is needed to run on Google cloud Kubernetes Engine. Once the Load-balancer is online, the external ip should be copied and pasted in the main.py's model_path parameter.

    2. The front-end website that allows a submission of picture. It will save the picture locally and it will request a prediction from the microservice 1. After getting the prediction, the picture and the prediction will be shown on the same page.
 
----------------------------------------------------------------------------
2023-04-02

To launch the model, the container image can be found at codait/max-image-caption-generator

The service should be exposed to port 5000 or it would not work.

Another microservice would be used to host a server that allows the user to upload the file and pass the file to the port, receive the returned information and show them on the screen along with the image.


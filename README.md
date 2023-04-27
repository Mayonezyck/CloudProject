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
2023-04-02

To launch the model, the container image can be found at codait/max-image-caption-generator

The service should be exposed to port 5000 or it would not work.

Another microservice would be used to host a server that allows the user to upload the file and pass the file to the port, receive the returned information and show them on the screen along with the image.

----------------------------------------------------------------------------

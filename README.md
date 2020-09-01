1.Collecting Dataset
  We have taken a dataset from Kaggle which contain images classified into 8 groups: cat, dog, airplane, car, flower, fruit, motorbike, person. 

2. Preprocessing Data
Preprocessing data is one of the integral part of any data Science project life cycle before we can use it for training purpose. For this model, we have applied a basic image transformation steps needed to put the images in the required format for our model training:
Converting images into an RGB array using open cv library.
Resize all the image to a standard size(32 X 32).
Scaling down pixel values from range (0, 255) to (0,1). 
Converting class label for each image to categorical value using One Hot Encoding.
Splitting the data set into training and Test dataset.
There are many more steps that can be applied during this step such as blurring the image, introducing noise and flipping the image etc to improve the model performance during training by exposing model with different variant of data.
Preprocessing images using cv23. 

3Preparing & Training model (Work in progress)
Here, We have a simple sequential neural network with 2 convolution(conv 2d) layers connected with dense layer with softmax activation for classifying an image in one of the desired classes.
Next we compile our model with optimizer(categorical_crossentropy), loss function(adam) and metrics so that our model can learn upon exposure with the training data.
After compiling the model and defining the batch size and epoch, we need to pass our training data to the model. We need to define epoch and batch size on the basis of the computing power available with us.
Model Creation and Preparation4. Saving the model and Predicting the output class
After training the model on training data, we pass the testing data to the model to check for overfitting and underfitting of the model. 
If the accuracy of the training data and test data do not differ by much, we can use our model to make prediction with the real life data.
For this, we save the model after training and loading the model to make the prediction. 

4.Saving model and loading the model 

5. Preparing Flask Application for deployment
We prepared a flask application to deploy our model for use in local environment, this application refers to a html page which inputs the data using an html page form and gives output for an input image in a text box.
Flask API to access Model

6. Containerize the application using Docker
Before discussing how we dockerize our application, I believe we need to mention some obvious benefits of the dockerizing the application:
 a.) Isolation : Docker ensures that our code and associated resources are isolated and segregated. 
b.) Security : Docker ensures that applications that are running on containers are completely segregated and isolated from each other, granting complete control over traffic flow and management.
c.) Portability : Docker images can be uploaded to docker hub and then from there it can be downloaded to any environment(cloud, on prem server and local) for easy deployment.
Following are the steps to containerize  any application in docker:
a.) Create docker file to define the steps used for creating an custom docker image.
b.) Also, we will prepare a requirement file which contains all the dependencies and libraries required. This dependencies and libraries will be installed in our docker image when we create it using docker file.
c.) Lastly, we will build a container from the image created by mapping the docker ports and port of the host server where the application is deployed.

7. HTML page for Image classification
For this application, we use HTML page to input the data in the model using Flask API. Input should be an image URL, image will be retrieved and given as input in the model. Then, image will be classified into one of the classes and response will be displayed in another text box.
HTML page for Image classification

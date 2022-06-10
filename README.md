# REST API For Predict Pose Using Phyton

Overview
--
This application is a solution so that the prediction process carried out by the TensorFlow model can be carried out by computing in the cloud, where the prediction results will be stored in firebase storage which is connected to google cloud storage and can be accessed through one of the endpoints in this application.

How To Install
--
1. Create vm 
2. Install pip3, nodejs16, and pm2
4. Clone this repository
5. Get your own key.json from google Cloud Service Account
6. Put pre-trained model into this folder, name it " model_facev1.h5 " for the pose prediction model and change the name to " my_model.h5 "
7. pip install -r requirements.txt

How to run
--
On Linux
--
pm2 start main.py --name face-api --interpreter python3

Endpoints
--


Testing The Application
--
1. We will use POSTMAN to test this application.
2. Start your application. (Refer to: How To Run section of the documentation)
3. Your application should be running on 127.0.0.1:8000/
4. Set the HTTP Request to GET and set http://127.0.0.1:8000/ as the URL
5. We will use 5nBCJLTWi0 as unique_id for demonstration purposes
6. Change URL to http://external IP on your vm:8000/?file=5nBCJLTWi0 then click Send
7. You should get a JSON response





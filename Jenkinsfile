pipeline {
    agent any
    stages { 
        stage('Git Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/ayra1215/project.git'
            }
        }
        stage ('Build') {
 	
sh """ 
cd project/flask/
docker build -t python/${BUILD_NUMBER}:v1.0 . 
 """		// Shell build step
sh """ 
export KEYID=$KEYID SECRETKEY=$SECRETKEY REGION=$REGION
 """		// Shell build step
sh """ 
aws configure set aws_access_key_id $KEYID
aws configure set aws_secret_access_key $SECRETKEY
aws configure set region $REGION
aws configure set output json 
 """		// Shell build step
sh """ 
aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin 944893048172.dkr.ecr.eu-central-1.amazonaws.com
docker tag project-ecr/${BUILD_NUMBER}:v1.0 944893048172.dkr.ecr.eu-central-1.amazonaws.com/project-ecr:${BUILD_NUMBER}
docker push 944893048172.dkr.ecr.eu-central-1.amazonaws.com/project-ecr:${BUILD_NUMBER} 
 """ 
	}
    }
}

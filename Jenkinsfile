pipeline {

    agent any

    stages{
	    stage ('Workspace Cleanup') {
		steps {    
	    cleanWs()
          }	
	}
	    stage('Git Checkout') {
            steps {
		    git branch: 'main', url: 'https://github.com/ayra1215/project.git'
            }
        }
        stage('build') {
            steps{
                sh "echo hello world"
		sh "pwd"   
		sh "ls"
                sh "docker build -t python/$BUILD_NUMBER:v1.0 project/flask"
                }
            }

        stage('push') {
            steps {
                sh "aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin 944893048172.dkr.ecr.eu-central-1.amazonaws.com"
                sh "docker tag python/$BUILD_NUMBER:v1.0 944893048172.dkr.ecr.eu-central-1.amazonaws.com/project-ecr:flask$BUILD_NUMBER"
                sh "docker push 944893048172.dkr.ecr.eu-central-1.amazonaws.com/project-ecr:flask$BUILD_NUMBER"
            }
        }

    }
}

pipeline {
    agent any
    
    environment {
        PATH = "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/ubuntu/.local/bin"
    }
    
    stages {
        stage('checkout github stage') {
            steps {
                checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/mauricewainaina/python-playground.git']])
            }
        }
        stage('Build Stage') {
            steps {
                sh 'python3 helloworld.py'
            }
        }
        stage('Test Stage') {
            steps {
                sh 'python3 -m pytest testing.py'
                
            }
        }
    }
}

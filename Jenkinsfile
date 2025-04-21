pipeline {
    agent {
      docker {
        image 'python:3'
        label 'install-jenkins-docker'
      }
    }
    stages {
        stage('Test') {
            steps {
              sh """
              python --version
              python ./script.py
              """
            }
        }
    }
}
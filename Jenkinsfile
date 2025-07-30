@Library('shared-lib') _

def imageName = "harbor.local/library/python-api:${env.BUILD_NUMBER}"

pipeline {
  agent any
  environment {
    IMAGE = imageName
  }
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Build with Kaniko') {
      steps {
        buildDocker(IMAGE)
      }
    }
    stage('Install Dependencies') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('Test') {
      steps {
        sh 'pytest tests'
      }
    }
    stage('Push to Harbor') {
      steps {
        echo "Pushed image: ${IMAGE}"
      }
    }
  }
pipeline {
  agent any
  environment {
    DOCKER_REGISTRY = 'harbor.local'
    DOCKER_CREDENTIALS = credentials('harbor-credentials')
    IMAGE = "harbor.local/library/python-api:${BUILD_NUMBER}"
  }
  stages {
    stage('Checkout') {
      steps { checkout scm }
    }
    stage('Test') {
      steps { sh 'pytest tests' }
    }
    stage('Build with Kaniko') {
      steps {
        script {
          // Build Docker image using kaniko (local build only)
          sh '''
            /kaniko/executor --dockerfile Dockerfile --context . --destination ${IMAGE} --no-push
          '''
        }
      }
    }
    stage('Push to Harbor') {
      steps {
        // TODO: Push image if not already pushed by Kaniko
        echo "TODO: Push to Harbor"
      }
    }
    stage('Deploy') {
      steps {
        // TODO: Add deployment logic
        echo "TODO: Deploy"
      }
    }
  }
}

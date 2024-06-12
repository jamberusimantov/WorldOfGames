pipeline {
    agent any
    // agent {
    //     docker { image 'node:20.11.1-alpine3.19' }
    // }
    stages {
        stage('Test') {
            steps {
                sh 'git --version'
                sh 'java --version'
                sh 'docker --version'
                sh 'pwd'
                sh 'ls -ltra'
                sh 'docker ps'
            }
        }
    }
}

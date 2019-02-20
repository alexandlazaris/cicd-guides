pipeline {
    agent any 
    stages {
        stage('Build') { 
            // agent {
            //     docker {
            //         image 'python:2-alpine' 
            //     }
            // }
            steps {
                //build
                echo ">>> RUNNING PYTHON SCRIPT TO GENERATE HTML <<<"
                sh 'python makeHTML.py'
                sh 'ls -l' 
            }
        }
        stage('Test') { 
            steps {
                echo ">>> RUNNING PYTHON TESTS <<<"
                sh 'mkdir test-reports'
                sh 'pytest --setup-show -v --junitxml test-reports/report.xml'
            }
        }
        stage('Deploy') { 
            steps {
                echo "Deploy things using AWS CLI" 
            }
        }
    }
}
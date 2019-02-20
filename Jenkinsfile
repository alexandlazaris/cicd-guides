pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                //build
                echo ">>> RUNNING PYTHON SCRIPT TO GENERATE HTML <<<"
                python makeHTML.py
                ls -l 
            }
        }
        stage('Test') { 
            steps {
                echo ">>> RUNNING PYTHON TESTS <<<"
                mkdir test-reports
                pytest --setup-show -v --junitxml test-reports/report.xml
            }
        }
        stage('Deploy') { 
            steps {
                echo "Deploy things using AWS CLI" 
            }
        }
    }
}
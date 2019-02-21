pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                echo ">>> RUNNING PYTHON SCRIPT TO GENERATE HTML <<<"
                sh 'python makeHTML.py'
                sh 'ls -l' 
                stash(name: 'index', includes: 'index.html')
                // archiveArtifacts artifacts: 'index.html', fingerprint: true 
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
                echo " >>> Deploy things using AWS CLI <<<" 
                echo "chech unstash restores file to local dir"
                sh 'ls -l' 
                unstash('index')
                sh 'ls -l' 
                echo ">>> list then copy file to s3 <<<"
                sh "aws s3 ls s3://cicd-guide"
                sh 'aws s3 cp index.html s3://cicd-guide'
                sh "aws s3 ls s3://cicd-guide"
            }
        }
    }
}
pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                    source venv/bin/activate
                    export PYTHONPATH=.
                    pytest tests/ --junitxml=report.xml
                '''
            }
        }
    }
    post {
        always {
            junit 'report.xml'
        }
    }
}

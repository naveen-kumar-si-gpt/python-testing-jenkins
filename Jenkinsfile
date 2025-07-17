pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pip install --upgrade pip
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

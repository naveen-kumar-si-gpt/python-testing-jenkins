pipeline {
    agent any

    triggers {
        githubPush()
    }

    environment {
        VENV = 'venv'
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv ${VENV}
                    . ${VENV}/bin/activate
                    pip install --upgrade pip
                    if [ -f requirements.txt ]; then
                        pip install -r requirements.txt
                    fi
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . ${VENV}/bin/activate
                    export PYTHONPATH=.
                    pytest tests/ --junitxml=report.xml
                '''
            }
        }
    }

    post {
        always {
            junit 'report.xml'

            emailext(
                subject: "Jenkins: ${env.JOB_NAME} [#${env.BUILD_NUMBER}] - ${currentBuild.currentResult}",
                body: """
                    <p><b>Project:</b> ${env.JOB_NAME}</p>
                    <p><b>Build #:</b> ${env.BUILD_NUMBER}</p>
                    <p><b>Status:</b> ${currentBuild.currentResult}</p>
                    <p><b>Logs:</b> <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>
                """,
                to: 'naveen.kumar@si-gpt.com',
                mimeType: 'text/html'
            )
        }
    }
}

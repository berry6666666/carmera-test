pipeline {
    agent any
    stages {
        stage('Run test') {
            parallel {
                stage ('RL1XXZ0007'){
                    steps {
                        dir('carmera-test') {
                            echo 'hellowe'
                            sh 'pytest test/ --udid RL1XXZ0007 --platform-version 10 --alluredir report'
                        }
                    }
                }
            }
        }
    }
}

pipeline {
    agent any
    stages {
        stage('Run test') {
            parallel {
                stage ('RL1XXZ0007'){
                    steps {
                        echo 'hellow'
                        bat 'conda activate test2'
                        bat 'conda list'
                        bat 'pip install -r requirements.txt'
                        bat 'pytest test/ --udid RL1XXZ0007 --platform-version 10 --alluredir report'
                        
                    }
                }
            }
        }
    }
}

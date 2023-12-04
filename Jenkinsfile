pipeline {
    agent any
    stages {
        stage('Run test') {
            parallel {
                stage ('RL1XXZ0007'){
                    steps {
                        echo 'hellow'
                        bat "call C:\\Users\\barry.huang\\anaconda3\\envs\\test2\\Scripts\\activate.bat"
                        bat 'pytest test/ --udid RL1XXZ0007 --platform-version 10 --alluredir report'
                        
                    }
                }
            }
        }
    }
}

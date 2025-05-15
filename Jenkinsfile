pipeline {
    agent {
        docker {
            image 'debian:latest'
            args '-u root'
        }
    }

    environment {
        SMB_USER = credentials('network-user')
    }

    stages {
        stage('Install Tools') {
            steps {
                sh '''
                    apt-get update
                    apt-get install -y smbclient
                '''
            }
        }

        stage('Copy Excel from Network') {
            steps {
                sh """
                    smbclient 'C:\\\\Users\\SIDDHARTH\\PyCharmMiscProject\\' -U ${SMB_USER_USR}%${SMB_USER_PSW} -c 'get Hanuman Chalisa - Print Out.xlsx ${WORKSPACE}/file.xlsx'
                """
            }
        }
    }
}



// pipeline{
    
//     agent any {

//         stages{

//             stage('version'){

//                 agent{
//                     docker{
//                         image 'my-playwright'
//                         reuseNode true
//                     }
//                 }

//                 steps{

//                     sh 'python3 --version'

//                 }
//             }

//             stage('Hello'){

//                 steps{

//                     sh 'python3 script.py'

//                 }
//             }

//         }

//     }


// }
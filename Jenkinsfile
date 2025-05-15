pipeline {
    agent any

    stages {
        stage('Copy Excel File') {
            steps {
                script {
                    // Copy using smbclient
                    sh """
                        smbclient 'C:\\\\Users\\SIDDHARTH\\PyCharmMiscProject\\' -U siddharth%password -c 'get Hanuman Chalisa - Print Out.xlsx ${WORKSPACE}/file.xlsx'
                    """
                }
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
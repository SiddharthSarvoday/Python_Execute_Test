pipeline {
    agent any

    stages {
        stage('Copy Excel File') {
            steps {
                script {
                    // Define source and destination
                    def source = 'C:\\Users\\SIDDHARTH\\PyCharmMiscProject\\Testing_File.xlsx'
                    def destination = "${env.WORKSPACE}\\Testing_File.xlsx"

                    // Copy using bat command
                    bat "copy \"${source}\" \"${destination}\""
                }
            }
        }

        stage('Verify Copy') {
            steps {
                bat "dir ${env.WORKSPACE}"
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
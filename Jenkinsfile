pipeline{
    
    agent any

        environment {
            // Set the UNC path of the network file
            NETWORK_FILE = 'C:\\\\Users\\SIDDHARTH\\PyCharmMiscProject\\Hanuman Chalisa - Print Out.xlsx'
            // Optional: Jenkins workspace path if you want to hardcode or use $WORKSPACE
            DEST_FILE = "${WORKSPACE}\\file.xlsx"
        }

        stages{



            stage('Copy Excel File') {
                steps {
                    script {
                        bat """
                        echo Copying Excel file from network drive...
                        copy "${env.NETWORK_FILE}" "${env.DEST_FILE}"
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
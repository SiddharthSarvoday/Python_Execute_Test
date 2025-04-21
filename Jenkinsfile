// pipeline{
    
//     agent any {

//         stages{

//             stage('version'){

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

pipeline{
    
    agent any {

        stages{

            stage('version'){

                agent{
                    docker{
                        image 'my-playwright'
                        reuseNode true
                    }
                }

                steps{

                    sh 'python3 --version'

                }
            }

            stage('Hello'){

                steps{

                    sh 'python3 script.py'

                }
            }

        }

    }


}
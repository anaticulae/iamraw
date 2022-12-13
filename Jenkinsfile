@Library('caelum@a1411f1288b8bc739b27c2e76f50554a6fdcda8c') _

pipeline{
    agent{
        docker{
            image '169.254.149.20:6001/arch_python_git_ghost_opencv_baw:v1.32.0'
        }
    }
    stages{
        stage('integrate'){
            steps{
                script{baw.integrate()}
            }
        }
        stage('setup'){
            steps{script{baw.setup()}}
        }
        stage('test'){
            failFast true
            parallel{
                stage('doc'){
                    steps{
                        script{baw.doctest()}
                    }
                }
                stage('fast'){
                    steps{
                        script{baw.fast()}
                    }
                }
                stage('long'){
                    steps{
                        script{baw.longrun()}
                    }
                }
            }
        }
        stage('quality'){
            failFast true
            parallel{
                stage('lint'){
                    steps{
                        script{baw.lint()}
                    }
                }
                stage('format'){
                    steps{
                        script{baw.format()}
                    }
                }
            }
        }
        stage('generate'){
            steps{
                sh 'baw --docken generate all'
            }
            post{
                always{script{publish.generated()}}
            }
        }
        stage('all'){
            steps{
                sh 'baw --docken test all -n32'
                //script{baw.all()}
            }
        }
        stage('release'){
            steps{
                script{publish.release()}
            }
        }
    }
}

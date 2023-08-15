pipeline {
    agent {
        // a.i. Agent should be based on the Dockerfile you created in step 1 and run in privileged mode with label zip-job-docker
        dockerfile {
            filename 'Dockerfile'
            label 'zip-job-docker'
            args '-u root:root'
        }
    }
    stages {
        stage('Build') {
            // b. Build stage should execute the zip_job.py you've created in step 2
            steps {
                sh 'python3 /tmp/zip_job.py'
            }
        }
        stage('Publish') {
            steps {
                script {
                    def server = Artifactory.server 'artifactory'
                    def uploadSpec = """{
                        "files": [
                            {
                                "pattern": "*.zip",
                                "target": "targil/"
                            }
                        ]
                    }"""
                    def buildInfo = server.upload spec: uploadSpec
                    server.publishBuildInfo buildInfo
                }
            }
        }
        stage('Report') {
            // d. Report stage - send email with job status in the subject to some email address
            steps {
                mail to: 'nimrodfix@gmail.com',
                     subject: "Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]': ${currentBuild.currentResult}",
                     body: "Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' finished with result: ${currentBuild.currentResult}"
            }
        }
    }
    post {
        always {
            // e. Cleanup stage - delete the workspace
            cleanWs()
        }
    }
}

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
            // c. Publish stage should upload all the zip files created (only in case build stage succeeded) to Artifactory you installed using the following properties:
            steps {
                script {
                    // Get the VERSION environment variable from the Docker image
                    def version = sh(returnStdout: true, script: 'echo $VERSION').trim()
                    // Set Artifactory server, user, password, and repository to upload to
                    def server = "http://10.0.2.30:8082"
                    def user = "nimrod"
                    def password = "Dc@U57!{y22T*}"
                    def repository = "targil"
                    // Upload all zip files to Artifactory
                    sh "find . -name '*.zip' -exec curl -u ${user}:${password} -X PUT ${server}/${repository}/{} -T {} \\;"
                }
            }
        }
        stage('Report') {
            // d. Report stage - send email with job status in the subject to some email address
            steps {
                mail to: 'some-email@example.com',
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

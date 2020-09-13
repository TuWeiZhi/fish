pipeline {
  agent {
    node {
      label '39-107-233-152'
    }

  }
  stages {
    stage('del dockerfile') {
      parallel {
        stage('del dockerfile') {
          steps {
            sh 'rm -rf /home/fish-dockerfile'
          }
        }

        stage('del containers') {
          steps {
            sh 'docker rm -f `docker ps -a -q`'
          }
        }

      }
    }

    stage('pull dockerfile') {
      steps {
        sh '''cd /home
git clone git@github.com:TuWeiZhi/fish-dockerfile.git'''
      }
    }

    stage('build image') {
      steps {
        sh '''cd /home/fish-dockerfile
docker build -t back-fish:`date +"%Y-%m-%d"` -f Dockerfile .'''
      }
    }

    stage('run container') {
      steps {
        sh 'docker run -tid --name=back-fish-`date +"%Y-%m-%d"` -h back-fish --net=host -v /home/uwsgi-log:/tmp/uwsgi-log back-fish:`date +"%Y-%m-%d"`'
      }
    }

    stage('test') {
      steps {
        build 'curl_django39-107-233-152'
      }
    }

  }
}
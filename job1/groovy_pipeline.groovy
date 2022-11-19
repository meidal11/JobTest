pipelineJob('job-dsl-plugin') {
  definition {
    cpsScm {
      scm {
        git {
          remote {
            url('https://github.com/meidal11/JobTest.git')
          }
          branch('*/main')
        }
      }
      lightweight()
    }
  }
}



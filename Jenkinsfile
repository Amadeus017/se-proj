pipeline
agent any {
	stages {
		stage('Cloning Stage') {
			steps {
				git 'https://github.com/Amadeus017/se-proj.git'
			}
		}
		stage('Run Code') {
			steps {
				sh "/usr/bin/python3 p1.py"
			}
		}
		stage('Testing stage') {
			steps {
				sh "/usr/bin/python3 test1.py'
			}
		}
	}
}


stages {
    stage('Veracode Scan') {
        steps {
            script {
                def config = readJSON file: 'veracode-config.json'                
                veracodeScan(config)
            }
        }
    }
}

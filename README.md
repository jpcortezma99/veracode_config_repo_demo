# ejemplo de como deberia ir en el PIPELINE
# del repo viene el 'veracode-config.json'

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
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    
    return "<center><h1>Progetto di Tirocinio</h1></center><p>Il progetto di tirocinio si concentra su concetti fondamentali di CI/CD e DevOps.</p><h2>DevOps</h2><p>DevOps è una cultura e una pratica che promuove la collaborazione e la comunicazione tra sviluppatori (Dev) e operatori di sistema (Ops) per migliorare l'efficienza e la velocità di sviluppo, distribuzione e gestione del software. L'obiettivo è creare un ambiente in cui lo sviluppo e le operazioni lavorino insieme in modo sinergico, riducendo i tempi di rilascio e migliorando la stabilità del sistema.</p><h2>Pipeline CI/CD</h2><p>Una pipeline CI/CD è un insieme di processi automatizzati che guidano il rilascio continuo (CI) e la distribuzione continua (CD) di un'applicazione. In questo contesto, la Continuous Integration (CI) si riferisce all'integrazione automatica del codice sorgente in un repository con il fine di identificare e risolvere conflitti in modo tempestivo. La Continuous Deployment (CD) estende questo concetto garantendo che le modifiche vengano distribuite automaticamente e in modo affidabile all'ambiente di produzione.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
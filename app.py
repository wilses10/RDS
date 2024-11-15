from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Dossier pour stocker les fichiers téléchargés
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Récupération des données du formulaire
        nom = request.form['nom']
        prenom = request.form['prenom']
        age = request.form['age']
        ville = request.form['ville']
        fichier = request.files['fichier']

        # Enregistrement du fichier
        if fichier:
            chemin_fichier = os.path.join(app.config['UPLOAD_FOLDER'], fichier.filename)
            fichier.save(chemin_fichier)

        # Affichage des informations dans la console
        print(f'Nom: {nom}, Prénom: {prenom}, Âge: {age}, Ville: {ville}')
        print(f'Fichier téléchargé : {chemin_fichier}')

        return redirect(url_for('index'))

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)


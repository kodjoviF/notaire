// Fonctions pour la page des membres

// Fonction pour afficher les membres
function afficherMembres() {
    // Récupérer les données des membres
    fetch('/api/membres')
      .then(response => response.json())
      .then(data => {
        // Afficher les membres
        const membres = document.getElementById('membres');
        membres.innerHTML = '';
        data.forEach(membre => {
          const li = document.createElement('li');
          li.innerHTML = `
            <h3>${membre.nom} ${membre.prenom}</h3>
            <p>${membre.email}</p>
            <p>${membre.tel}</p>
          `;
          membres.appendChild(li);
        });
      })
      .catch(error => console.error(error));
  }
  
  // Fonction pour ajouter un membre
  function ajouterMembre() {
    // Récupérer les données du formulaire
    const nom = document.getElementById('nom').value;
    const prenom = document.getElementById('prenom').value;
    const email = document.getElementById('email').value;
    const tel = document.getElementById('tel').value;
  
    // Envoyer les données au serveur
    fetch('/api/membres', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        nom,
        prenom,
        email,
        tel
      })
    })
      .then(response => response.json())
      .then(data => {
        // Afficher le message de confirmation
        alert('Membre ajouté avec succès !');
        // Afficher les membres
        afficherMembres();
      })
      .catch(error => console.error(error));
  }
  
  // Fonction pour supprimer un membre
  function supprimerMembre(id) {
    // Envoyer la requête de suppression au serveur
    fetch(`/api/membres/${id}`, {
      method: 'DELETE'
    })
      .then(response => response.json())
      .then(data => {
        // Afficher le message de confirmation
        alert('Membre supprimé avec succès !');
        // Afficher les membres
        afficherMembres();
      })
      .catch(error => console.error(error));
  }
  
  // Ajouter des événements aux boutons
  document.getElementById('ajouter').addEventListener('click', ajouterMembre);
  document.getElementById('supprimer').addEventListener('click', function() {
    const id = this.dataset.id;
    supprimerMembre(id);
  });
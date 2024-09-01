// Fonction pour formater la date
function formatDate(dateString) {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return new Date(dateString).toLocaleDateString('fr-FR', options);
}

// Fonction pour créer une carte d'activité
function createActivityCard(activity) {
    return `
        <div class="col-md-4">
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title">${activity.titre}</h5>
                    <p class="card-text">${formatDate(activity.date)}</p>
                    <a href="#" class="btn btn-primary" data-id="${activity.id}">En savoir plus</a>
                </div>
            </div>
        </div>
    `;
}

// Fonction pour charger les activités depuis l'API
function loadActivities() {
    fetch('/api/activites/')
        .then(response => response.json())
        .then(data => {
            const container = document.querySelector('.row');
            container.innerHTML = data.map(createActivityCard).join('');
        })
        .catch(error => console.error('Erreur:', error));
}

// Fonction pour afficher les détails d'une activité
function showActivityDetails(id) {
    fetch(`/api/activites/${id}/`)
        .then(response => response.json())
        .then(data => {
            alert(`Détails de l'activité:\n\nTitre: ${data.titre}\nDate: ${formatDate(data.date)}\nDescription: ${data.description}`);
        })
        .catch(error => console.error('Erreur:', error));
}

// Écouteur d'événements pour le chargement du DOM
document.addEventListener('DOMContentLoaded', function() {
    loadActivities();

    // Délégation d'événements pour les boutons "En savoir plus"
    document.querySelector('.row').addEventListener('click', function(e) {
        if (e.target.classList.contains('btn-primary')) {
            e.preventDefault();
            const id = e.target.getAttribute('data-id');
            showActivityDetails(id);
        }
    });
});
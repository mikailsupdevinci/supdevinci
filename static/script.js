// Attachez un gestionnaire d'événements au bouton de l'API
$("#bouton-api").click(function() {
  // Utilisez jQuery pour appeler l'API
  $.getJSON("/appeler-api", function(data) {
    // Insérez les données de l'API dans le div de résultat
    $("#resultat-api").html(JSON.stringify(data));
  });
});

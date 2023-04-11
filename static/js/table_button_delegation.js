const table = document.querySelector('table');

table.addEventListener('click', function(event) {
  if (event.target.tagName === 'BUTTON') {

    // Pobieramy id rekordu z atrybutu 'data-id'
    var id = event.target.getAttribute('data-id');
    // Przekierowujemy użytkownika na stronę edycji rekordu
    window.location.href = '{{ request.path }}' + "edit/" + id + "/"
  }
});
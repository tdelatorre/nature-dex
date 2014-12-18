/* global Klass, SpecimenById, Services, jQuery, console */
(function ( scope, $ ) {
    'use strict';

    var ListView = new Klass();
    ListView.extend({
        init: function () {
            console.log( 'ListView::init' );

            // Render data
            var data = Services.getLoadedList();

            console.log( 'ListView::Services::', data );

            for ( var specimen in data.specimenes.results) {
                var obj = data.specimenes.results[specimen];

                // Datos para renderizarcontent-list
                var image = (obj.specimen_image !== null) ? obj.specimen_image : Services.getLocation() + 'static/images/animal_fallback.jpg';
                var specimenId = obj.id;
                var commonName = obj.common_name;
                var scientificName = obj.scientific_name;
                var html = '';
                html += '<li data-theme="c" class="ui-btn ui-btn-icon-right ui-li-has-arrow ui-li ui-li-has-thumb ui-btn-up-c">';
                html += '    <div class="ui-btn-inner ui-li" aria-hidden="true">';
                html += '        <div class="ui-btn-text">';
                html += '            <a href="#" class="ui-link-inherit" data-specimen-id="' + specimenId + '">';
                html += '                <img src="' + image + '" class="ui-li-thumb">';
                html += '                <h3 class="ui-li-heading">' + scientificName + '</h3>';
                html += '                <p class="ui-li-desc">' + commonName + '</p>';
                html += '            </a>';
                html += '        </div>';
                html += '        <span class="ui-icon ui-icon-arrow-r ui-icon-shadow"></span>';
                html += '    </div>';
                html += '</li>';

                console.log( 'specimen', obj.scientific_name );
                $( '#listview' ).find( '#content-list' ).append( html );
            }

            // Eventos de la lista
            $( '#listview' ).find( '#content-list' ).find( 'li a' ).on( 'click', function ( event ) {

                var specimenId = $(this).attr( 'data-specimen-id' );

                console.log( specimenId );

                SpecimenById.getSpecimenById(specimenId);
                
                event.preventDefault();
            });
        }
    });

    if ( !('ListView' in scope) )
        scope.ListView = ListView;

})( window, jQuery );
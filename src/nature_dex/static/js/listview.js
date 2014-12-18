/* global Klass, SpecimenById, Services, jQuery, console */
(function ( scope, $ ) {
    'use strict';

    var _$view = null;
    var _page = 0;

    function renderList () {

        _$view.find( '#content-list' ).html( '' );

        // Render data
        var data = Services.getLoadedList();

        if ( data.specimenes.previous === null) {
            _page = 1;
        }
        else if ( data.specimenes.next === null ) {
            var preg = data.specimenes.previous.split('=');
            _page = Number(preg[preg.length - 1]) + 1;
        }
        else {
            var preg = data.specimenes.next.split('=');
            _page = Number(preg[preg.length - 1]) - 1;
        }

        console.log( 'ListView::Services::', data );
        console.log(data.specimenes.results);

        if (!data.specimenes.results.length) {
            var html = '<p>No hemos encontrado nada</p>';
            $( '#content-list' ).append( html );

        } else {
            for ( var specimen in data.specimenes.results) {
                var obj = data.specimenes.results[specimen];

                // Datos para renderizarcontent-list
                var image = (obj.specimen_image !== null) ? obj.specimen_image : Services.getLocation() + 'static/images/animal_fallback.jpg';
                var specimenId = obj.id;
                var commonName = obj.common_name;
                var scientificName = obj.scientific_name;
                var identification = obj.identification;
                var html = '';
                html += '<li data-theme="c" class="ui-btn ui-li ui-li-has-thumb ui-btn-up-c">';
                html += '    <div class="ui-btn-inner ui-li" aria-hidden="true">';
                html += '        <div class="ui-btn-text">';
                html += '            <a href="#" class="ui-link-inherit" data-specimen-id="' + specimenId + '">';
                html += '                <div class="thumb-content" style="background-image: url(' + image + ')"></div>';
                html += '                <h3 class="ui-li-heading">' + commonName + '</h3>';
                html += '                <p class="ui-li-desc">' + scientificName + '</p>';
                html += '                <p class="ui-li-desc">' + identification + '</p>';
                html += '            </a>';
                html += '        </div>';
                html += '        <span class="ui-icon ui-icon-arrow-r ui-icon-shadow"></span>';
                html += '    </div>';
                html += '</li>';

                console.log( 'specimen', obj.scientific_name );
                _$view.find( '#content-list' ).append( html );
            }
        }

        // Events
        _$view.find( '#content-list' ).find( 'li a' ).on( 'click', onSpecimenClick);

        // Update page
        _$view.find( 'span.currentPage' ).html( _page );
    }

    function onSpecimenClick ( event ) {

        var specimenId = $(this).attr( 'data-specimen-id' );

        SpecimenById.getSpecimenById(specimenId);

        event.preventDefault();
    }

    var ListView = new Klass();
    ListView.extend({
        init: function () {
            console.log( 'ListView::init' );

            // Recogery the view
            _$view = $( '#listview' );

            // Check if exists data form Service
            if ( Services.getLoadedList === null ) {
                window.location = Services.getLocation();
            }

            // Render
            renderList();

            // Eventos de la lista

            _$view.find( 'button.next' ).off().on( 'click', function ( event ) {
                SeeAll.next( ListView.nextDataReceived() );

                event.preventDefault();
            });

            _$view.find( 'button.prev' ).off().on( 'click', function ( event ) {
                SeeAll.prev( ListView.prevDataReceived() );

                event.preventDefault();
            });
        },
        prevDataReceived: function ( data ) {
            var self = this;

            return function ( data ) {

                console.log( 'ListView::prevDataReceived', data );

                if ( data === false ) {
                    console.log( 'no hay página anterior' );
                    return;
                }

                _page--;
                renderList();
            }
        },
        nextDataReceived: function ( data ) {
            var self = this;

            return function ( data ) {

                console.log( 'ListView::nextDataReceived', data );

                if ( data === false ) {
                    console.log( 'no hay página siguiente' );
                    return;
                }

                _page++;
                renderList();
            }
        }
    });

    if ( !('ListView' in scope) )
        scope.ListView = ListView;

})( window, jQuery );

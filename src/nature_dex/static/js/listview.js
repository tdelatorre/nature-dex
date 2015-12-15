/* global Klass, SpecimenById, Services, jQuery, console */
(function ( scope, $ ) {
    'use strict';

    var _$view = null;
    var _page = getParameterByName('page') || 1;

    function renderList () {
        _$view.find( '#content-list' ).html( '' );

        // Render data
        var data = Services.getLoadedList();

        var title = data.label;
        _$view.find( 'h1.title' ).html( title );

        if ( data.specimenes.count <= 10 ) {
            _$view.find('div.pagination').hide();
        }

        console.log( 'ListView::Services::', data );

        if (!data.specimenes.results.length) {
            var html = 'No hemos encontrado nada';
            _$view.find( 'h1.title' ).html( html );

        } else {
            for ( var specimen in data.specimenes.results) {
                var obj = data.specimenes.results[specimen];

                // Datos para renderizarcontent-list
                var image = (obj.specimen_image !== null) ? obj.specimen_image : Services.getLocation() + 'static/images/animal_fallback.jpg';
                var specimenId = obj.id;
                var commonName = obj.common_name;
                var scientificName = obj.scientific_name;
                var group = obj.group;
                var html = '';
                html += '<li data-theme="c" class="ui-btn ui-li ui-li-has-thumb ui-btn-up-c">';
                html += '    <div class="ui-btn-inner ui-li" aria-hidden="true">';
                html += '        <div class="ui-btn-text">';
                html += '            <a href="#" class="ui-link-inherit" data-specimen-id="' + specimenId + '">';
                html += '                <div class="thumb-content" style="background-image: url(' + image + ')"></div>';
                html += '                <h3 class="ui-li-heading">' + commonName + '</h3>';
                html += '                <p class="ui-li-desc">' + scientificName + '</p>';
                html += '                <p class="ui-li-desc">Grupo: ' + group + '</p>';
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
            _page = getParameterByName('page') || 1;

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

                var group = getParameterByName('kingdom');
                var kingdom = getParameterByName('group');

                var params = [];

                params.push('page=' + (Number(_page) + 1));

                if(group) {
                  params.push('group='+ group);
                }

                if(kingdom) {
                  params.push('kingdom='+ kingdom);
                }

                window.history.pushState({},"",Services.getLocation() + 'listview/?' + params.join('&'));
                event.preventDefault();
            });

            _$view.find( 'button.prev' ).off().on( 'click', function ( event ) {
                SeeAll.prev( ListView.prevDataReceived() );

                var group = getParameterByName('kingdom');
                var kingdom = getParameterByName('group');

                var params = [];

                params.push('page=' + (Number(_page) - 1));

                if(group) {
                  params.push('group='+ group);
                }

                if(kingdom) {
                  params.push('kingdom='+ kingdom);
                }

                if (Number(_page) > 1) {
                  window.history.pushState({},"",Services.getLocation() + 'listview/?' + params.join('&'));
                }

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

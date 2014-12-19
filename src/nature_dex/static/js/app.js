/* global jQuery, Position, console */
(function ( $ ) {
    'use strict';

    var _$view = null;

    $( document )
    .off( 'pagebeforechange', appBeforeChange )
    .on( 'pagebeforechange', appBeforeChange )
    .on( 'pagecontainershow', function(){
        console.log( 'app.pagecontainershow' );

        _$view = $( '#home' );

        $( 'button.btn-whereami' )
            .off( 'click' )
            .on( 'click', function ( event ) {
                Position.whereami( getResults );
            });

        $( 'button.btn-see-all' )
            .off( 'click' )
            .on( 'click', function ( event ) {
                SeeAll.seeall();
            });

        getResults();

        switch(Services.viewName){
            case 'listview':
                Services.view = ListView;
                ListView.init();
                break;
            case 'file':
                Services.view = Ficha;
                Ficha.init();
                break;
            default:
                break;
        }
    });

    function getResults () {
        // Cargamos los primeros resultados
        SeeAll.getFirstResults( renderList );
    }

    function appBeforeChange (event, data) {
        console.log( 'app.pagebeforechange:' , data);
        // console.log( 'Data: ', $.mobile.path.parseUrl( data.toPage ) );

        if (typeof data.prevPage === 'undefined') {
            // $.mobile.changePage( Services.getLocation() + '/' , {
            //     type: 'get'
            // });
        }

        var $page = $(data.toPage[0]);
        console.log( 'Página cargada: ', $page.find('.ui-content').attr('id') );
        Services.viewName = $page.find('.ui-content').attr('id');
    }

    function renderList ( data ) {

        _$view.find( '#home-content-list' ).html( '' );

        if (!data.results.length) {
            var html = '<p>No hemos encontrado nada</p>';
            $( '#content-list' ).append( html );

        } else {
            
            var i = 0;
            for ( var specimen in data.results) {

                var obj = data.results[specimen];

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
                _$view.find( '#home-content-list' ).append( html );
                
                i++;
                if (i > 1) { break; } 
            }
        }

        // Events
        _$view.find( '#home-content-list' ).find( 'li a' ).on( 'click', onSpecimenClick);
    }

    function onSpecimenClick ( event ) {

        var specimenId = $(this).attr( 'data-specimen-id' );

        SpecimenById.getSpecimenById(specimenId);

        event.preventDefault();
    }

})( jQuery );

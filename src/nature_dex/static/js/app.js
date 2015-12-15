/* global jQuery, Position, console */

function getParameterByName(name) {
    name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
    var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
        results = regex.exec(location.search);
    return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
}

(function ( $ ) {
    'use strict';

    var _$view = null;

    $( document )
    .off( 'pagebeforechange', appBeforeChange )
    .on( 'pagebeforechange', appBeforeChange )
    .on('ready', function() {
      if (window.location.href.indexOf(Services.getLocation() + 'listview/') !== -1) {
        var page = getParameterByName('page') || 1;
        var kingdom = getParameterByName('kingdom');
        var group = getParameterByName('group');

        SeeAll.seeall(group, kingdom, page).then(function() {
          Services.viewName = 'listview';
          Services.view = ListView;
          ListView.init();
        });
      }
    })
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
              $.mobile.changePage( Services.getLocation() + 'listview', {
                type: 'get'
              });
            });

        getResults();

        switch(Services.viewName){
          case 'listview':
              var kingdom = getParameterByName('kingdom');
              var group = getParameterByName('group');

              SeeAll.seeall(group, kingdom, 1).then(function() {
                 Services.viewName = 'listview';
                 Services.view = ListView;
                 ListView.init();
              });
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

/* global jQuery, console */
(function ( $ ) {
    'use strict';

    $( document )
    .off( 'pagebeforechange', onListViewBeforeChange)
    .on( 'pagebeforechange', onListViewBeforeChange)
    .on( 'pagecontainershow', onListViewContainerShow);

    function onListViewBeforeChange (event, data) {
        console.log( 'listview.pagebeforechange:' , data);
        console.log( 'Data: ', $.mobile.path.parseUrl( data.toPage ) );
    }

    function onListViewContainerShow () {

        console.log( 'app.pagecontainershow' );

        // Función por defecto de los enlaces
        $( '#listview' )
        .find( 'a' ).off().on( 'click' , function ( event ) {

            event.preventDefault();

            console.log( 'A la ficha!' );

            // Navigation
            $.mobile.changePage( window.location.protocol + '//' + window.location.host +  '/file/', true);
        });
    }

})( jQuery );
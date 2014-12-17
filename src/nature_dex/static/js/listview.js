/* global jQuery, Position, console */
(function ( $ ) {
    'use strict';

    $( document )
    .off( 'pagebeforechange', onListViewBeforeChange)
    .on( 'pagebeforechange', onListViewBeforeChange)
    .on( 'pagecontainershow', onListViewContainerShow);

    function obListViewBeforeChange (event, data) {
        console.log( 'listview.pagebeforechange:' , data);
        console.log( 'Data: ', $.mobile.path.parseUrl( data.toPage ) );
    }

    function onListViewContainerShow () {
        
        console.log( 'app.pagecontainershow' );

        $( 'button.btn-whereami' ).off().on( 'click', function ( event ) {
            Position.whereami();
        });

        // Función por defecto de los enlaces [res="external"]
        $( 'a[rel="external"]' ).off().on( 'click' , function ( event ) {

        });
    }

})( jQuery );
/* global jQuery, Position, console */
(function ( $ ) {
    'use strict';

    $( document )
    .on( 'pagebeforechange', function (event, data) {
        console.log( 'listview.pagebeforechange:' , data);
        console.log( 'Data: ', $.mobile.path.parseUrl( data.toPage ) );
    })
    .on( 'pagecontainershow', function(){
        console.log( 'app.pagecontainershow' );

        $( 'button.btn-whereami' ).off( 'click' ).on( 'click', function ( event ) {
            Position.whereami();
        });

        $( 'button.btn-see-all' ).off( 'click' ).on( 'click', function ( event ) {
            SeeAll.seeall();
        });

        // Función por defecto de los enlaces [res="external"]
        $( 'a[rel="external"]' ).off( 'click' ).on( 'click' , function ( event ) {

        });
    });

})( jQuery );

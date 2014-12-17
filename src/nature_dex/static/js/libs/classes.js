/* global Klass, jQuery, console */
(function ( scope, $ ) {
    'use strict';

    var Position = new Klass();
    Position.extend({
        whereami: function () {
            if ( !('navigator' in window) ) {
                console.log( 'Your browser not support geolocation features' );
                return;
            }

            // Showing loader

            navigator.geolocation.getCurrentPosition( function ( position ) {
                console.log( 'Position: ', position );

                // Navigation
                $.mobile.changePage( 'listview/' , {
                    type: 'get',
                    data: {
                        label: 'herbage',
                        position: position.coords
                    }
                });
            });
        }
    });

    scope.Position = Position;

})( window, jQuery );
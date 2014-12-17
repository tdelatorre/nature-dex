/* global Klass, jQuery, console */
(function ( scope, $ ) {
    'use strict';

    var client = new $.RestClient('/api/');
    var position = {};


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

                position = {
                    lat: position.coords.latitude,
                    lon: position.coords.longitude
                }

                Species.getSpecies();

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

    var Specimenes = new Klass();
    Specimenes.extend({
        data: {},
        getSpecimenes: function () {
            client.add('specimenes');

            client.foo.read({
                lat: position.coords.latitude,
                lon: position.coords.longitude
            }).done(function ( data ) {

                Specimenes.data = data;
            });
        }
    })

    scope.Position = Position;
    scope.Specimenes = Specimenes;

})( window, jQuery );
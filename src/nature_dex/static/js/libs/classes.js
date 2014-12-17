/* global Klass, jQuery, console */
(function ( scope, $ ) {
    'use strict';

    var client = new $.RestClient('/api/');
    var position = {};
    var group = '';
    var kingdom = '';


    var Position = new Klass();
    Position.extend({
        whereami: function () {
            if ( !('navigator' in window) ) {
                console.log( 'Your browser not support geolocation features' );
                return;
            }

            // Showing loader

            navigator.geolocation.getCurrentPosition( function ( position ) {
                position = {
                    lat: position.coords.latitude,
                    lon: position.coords.longitude
                };

                Specimenes.getSpecimenes(position['lon'], position['lat'], group, kingdom);

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
        getSpecimenes: function (lon, lat, group, kingdom) {
            client.add('specimenes');
            client.specimenes.read({
                lon: lon,
                lat: lat,
                group: group,
                kingdom: kingdom
            }).done(function ( data ) {
                Specimenes.data = data;
            });
        }
    })

    var SpecimenById = new Klass();
    SpecimenById.extend({
        data: {},
        getSpecimenById: function (specimenId) {
            client.add('specimenes');
            client.specimenes.read(specimenId).done(function ( data ) {
                SpecimenById.data = data;
            });
        }
    })

    scope.Position = Position;
    scope.Specimenes = Specimenes;

})( window, jQuery );

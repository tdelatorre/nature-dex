/* global Klass, jQuery, console */
(function ( scope, $ ) {
    'use strict';

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
            });
        }
    });

    var SeeAll = new Klass();
    SeeAll.extend({
        seeall: function (group, kingdom) {
            // Showing loader

            navigator.geolocation.getCurrentPosition( function ( position ) {
                position = {
                    lat: position.coords.latitude,
                    lon: position.coords.longitude
                };

                var promise = Specimenes.getSpecimenes(position['lon'], position['lat'], group, kingdom);
                promise.done(function ( specimenes ) {
                    // Navigation
                    $.mobile.changePage( 'listview/' , {
                        type: 'get',
                        data: {
                            label: 'Ver todo',
                            specimenes: specimenes
                        }
                    });
                });

            });
        }
    });

    var Specimenes = new Klass();
    Specimenes.extend({
        data: {},
        getSpecimenes: function (lon, lat, group, kingdom) {
            var client = new $.RestClient('/api/');
            client.add('specimenes');
            return client.specimenes.read({
                lon: lon,
                lat: lat,
                group: group,
                kingdom: kingdom
            })

        }
    })

    var SpecimenById = new Klass();
    SpecimenById.extend({
        data: {},
        getSpecimenById: function (specimenId) {
            var client = new $.RestClient('/api/');
            client.add('specimenes');
            client.specimenes.read(specimenId).done(function ( data ) {
                SpecimenById.data = data;
            });
        }
    })

    scope.Position = Position;
    scope.SeeAll = SeeAll;
    scope.Specimenes = Specimenes;

})( window, jQuery );

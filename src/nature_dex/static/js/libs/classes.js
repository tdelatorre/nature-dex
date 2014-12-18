/* global Klass, jQuery, console */
(function ( scope, $ ) {
    'use strict';

    var position = {};
    var group = '';
    var kingdom = '';

    var Services = new Klass();
    Services.extend({
        loadedData: null,
        loadedView: null,
        getLoadedData: function () {
            return this.loadedData;
        },
        getLoadedView: function () {
            return this.loadedView;
        },
        getLocation: function () {
            return window.location.protocol + '//' + window.location.host + '/';
        }
    });

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

                $( 'button.btn-whereami' ).hide()
                $('img').attr('src', "http://maps.googleapis.com/maps/api/staticmap?zoom=16&size=400x100&maptype=terrain&markers=color:red%7C" + position['lat'] + "," + position['lon'] + "&sensor=false")
            });
        }
    });

    var SeeAll = new Klass();
    SeeAll.extend({
        lastData: {},
        seeall: function (group, kingdom) {
            // Showing loader

            navigator.geolocation.getCurrentPosition( function ( position ) {
                position = {
                    lat: position.coords.latitude,
                    lon: position.coords.longitude
                };

                var promise = Specimenes.getSpecimenes(position['lon'], position['lat'], group, kingdom);
                promise.done(function ( specimenes ) {

                    Services.loadedData = {
                        label: 'Ver todo',
                        specimenes: specimenes
                    }

                    // Navigation

                    $.mobile.changePage( 'listview/' , {
                        type: 'get'
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
    });

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
    });

    if ( !('Position' in scope) )
        scope.Position = Position;
    if ( !('SeeAll' in scope) )
        scope.SeeAll = SeeAll;
    if ( !('Specimenes' in scope) )
        scope.Specimenes = Specimenes;
    if ( !('Services' in scope) )
        scope.Services = Services;

})( window, jQuery );

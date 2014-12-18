/* global Klass, jQuery, console */
(function ( scope, $ ) {
    'use strict';

    var _position = {};
    var group = '';
    var kingdom = '';

    var Services = new Klass();
    Services.extend({
        loadedList: null,
        loadedFile: null,
        loadedView: null,
        getLoadedList: function () {
            return this.loadedList;
        },
        getLoadedFile: function () {
            return this.loadedFile;
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
                _position = {
                    lat: position.coords.latitude,
                    lon: position.coords.longitude
                };

                $( 'button.btn-whereami' ).hide()
                $('img').attr('src', "http://maps.googleapis.com/maps/api/staticmap?zoom=16&size=600x200&maptype=terrain&markers=color:red%7C" + _position['lat'] + "," + _position['lon'] + "&sensor=false")
            });
        }
    });

    var SeeAll = new Klass();
    SeeAll.extend({
        lastData: {},
        seeall: function (group, kingdom) {
            // Showing loader

            navigator.geolocation.getCurrentPosition( function ( position ) {
                _position = {
                    lat: position.coords.latitude,
                    lon: position.coords.longitude
                };

                var promise = Specimenes.getSpecimenes(_position['lon'], _position['lat'], group, kingdom);
                promise.done(function ( specimenes ) {

                    Services.loadedList = {
                        label: 'Ver todo',
                        specimenes: specimenes
                    }

                    // Navigation

                    $.mobile.changePage( Services.getLocation() + 'listview/' , {
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
        getSpecimenById: function (specimenId) {
            var client = new $.RestClient('/api/');
            client.add('specimenes');
            client.specimenes.read(specimenId).done(function ( data ) {
                Services.loadedFile = {
                    label: 'Ver ficha',
                    specimen: data
                }

                // Navigation

                $.mobile.changePage( Services.getLocation() + 'file/' , {
                    type: 'get'
                });
            });
        }
    });

    if ( !('Position' in scope) )
        scope.Position = Position;
    if ( !('SeeAll' in scope) )
        scope.SeeAll = SeeAll;
    if ( !('Specimenes' in scope) )
        scope.Specimenes = Specimenes;
    if ( !('SpecimenById' in scope) )
        scope.SpecimenById = SpecimenById;
    if ( !('Services' in scope) )
        scope.Services = Services;

})( window, jQuery );

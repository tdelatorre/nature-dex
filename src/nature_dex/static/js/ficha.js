/* global Klass, Services, jQuery, console */
(function ( scope, $ ) {
    'use strict';

    var _$view = null;

    var Ficha = new Klass();
    Ficha.extend({
        init: function () {
            console.log( 'Ficha::init' );

            _$view = $('#file');

            // Render data
            var data = Services.getLoadedFile();

            var specimenImage = data.specimen.specimen_image;
            if ( specimenImage === null ) {
                if ( data.specimen.kingdom === 'Animalia' ) {
                    specimenImage = Services.getLocation() + 'static/images/animal_fallback.jpg';
                }
                else if ( data.specimen.kingdom === 'Plantae' ) {
                    specimenImage = Services.getLocation() + 'static/images/leaf_fallback.png';
                }
            }

            var trackImage = data.specimen.track_image;
            if ( trackImage === null) {
                trackImage = Services.getLocation() + 'static/images/track_fallback.jpg';
            }

            if ( data.specimen.kingdom === 'Plantae' ) {
                _$view.find( 'div.trackImageContent img').hide();
            }

            console.log( 'Ficha::Services::', data );
            console.log( 'Vista::', _$view.find( 'span.commonName' ) );
            _$view.find( 'span.commonName' ).html(data.specimen.common_name);
            _$view.find( 'span.scientificName' ).html(data.specimen.scientific_name);
            _$view.find( 'div.specimentImageContent img').attr( 'src', specimenImage);
            _$view.find( 'span.identification').attr( 'src', data.specimen.identification);
            _$view.find( 'div.trackImageContent img').attr( 'src', trackImage);
            _$view.find( 'span.kingdom' ).html(data.specimen.kingdom);
            _$view.find( 'span.group' ).html(data.specimen.group);
            _$view.find( 'span.family' ).html(data.specimen.family);
            _$view.find( 'span.species' ).html(data.specimen.species);

            // Eventos de la ficha
        }
    });

    if ( !('Ficha' in scope) )
        scope.Ficha = Ficha;

})( window, jQuery );
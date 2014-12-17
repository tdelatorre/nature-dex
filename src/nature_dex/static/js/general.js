/* global jQuery */
(function ( $ ) {
    'use strict';

    var _count = 0;

    $( document ).on( 'pagecontainershow', generalFunctionality);

    function generalFunctionality () {

        _count++;

        console.log('general pagecontainershow:', _count); // jshint ignore:line

        // WIDGETS

        /**
         *  Search panel functionality
         * */
        var $panelSearch = $( '#panelsearch' );

        $panelSearch
        .addClass( 'eventattached' )
        .find('a.panelsearch-link').off( 'click' ).on( 'click', function (event) {
            event.preventDefault();
            console.log( 'Searching...' );
        });

        /**
         *  Menu panel functionality
         * */
        var $panelMenu = $( '#panelmenu' );
        
        $panelMenu
        .addClass( 'eventattached' )
        .find('a.panelmenu-link').off( 'click' ).on( 'click', panelMenuLinkClick);
    }

    function panelMenuLinkClick ( event ) {
        event.preventDefault();
        console.log( 'Menu option selected' );
    }

    function pageChange () {

        console.log( 'general pagechange!' );

        $( document )
        .off( 'pagecontainershow', generalFunctionality)
        .on( 'pagecontainershow', generalFunctionality);
    }

})( jQuery )
/* global jQuery, Position, console */
(function ( $ ) {
    'use strict';

    var _viewName = null,
        _view = null;

    $( document )
    .off( 'pagebeforechange', appBeforeChange )
    .on( 'pagebeforechange', appBeforeChange )
    .on( 'pagecontainershow', function(){
        console.log( 'app.pagecontainershow' );

        $( 'button.btn-whereami' )
            .off( 'click' )
            .on( 'click', function ( event ) {
                Position.whereami();
            });

        $( 'button.btn-see-all' )
            .off( 'click' )
            .on( 'click', function ( event ) {
                SeeAll.seeall();
            });

        // Función por defecto de los enlaces [res="external"]
        $( 'a[rel="external"]' )
            .off( 'click' )
            .on( 'click' , function ( event ) {

            });

        switch(_viewName){
            case 'listview':
                _view = ListView;
                ListView.init();
                break;
            case 'file':
                _view = Ficha;
                Ficha.init();
                break;
            default:
                break;
        }
    });

    function appBeforeChange (event, data) {
        console.log( 'app.pagebeforechange:' , data);
        // console.log( 'Data: ', $.mobile.path.parseUrl( data.toPage ) );

        if (typeof data.prevPage === 'undefined') {
            // $.mobile.changePage( Services.getLocation() + '/' , {
            //     type: 'get'
            // });
        }

        var $page = $(data.toPage[0]);
        console.log( 'Página cargada: ', $page.find('.ui-content').attr('id') );
        _viewName = $page.find('.ui-content').attr('id');
    }

})( jQuery );

(function ( scope ) {
    'use strict';

	/**
     * Klass
     * Base class to create heriatic
     */
    var Klass = function ( parent ) {
        var instance = function () {
            this.init.apply(this, arguments);
        };

        instance.fn = instance.prototype;

        instance.fn.init = function () {};

        if ( parent ) {
            var Kinstance = function () {};
            Kinstance.prototype = parent.prototype;
            instance.prototype = new Kinstance();
        }

       	instance.extend = function ( obj ) {
            for ( var param in obj ) {
                instance[param] = obj[param];
       		}
       	};

       	instance.include = function ( obj ) {
       		for ( var param in obj ) {
       	        instance.prototype[param] = obj[param];
       		}
       	};

        return instance;
    };

    scope.Klass = Klass;

})( window );
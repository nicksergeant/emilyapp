var emilyapp = {
    module: function() {
        var modules = {};

        return function(name) {
            if (modules[name]) {
                return modules[name];
            }

            return modules[name] = { Views: {} };
        };
    }()
};

jQuery(function($) {

    AppView = emilyapp.module('events').Views.AppView;
    window.app = new AppView();

});

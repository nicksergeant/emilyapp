(function(Events) {

    Events.EventModel = Backbone.Model.extend();

    EventView = Backbone.View.extend({
        initialize: function() {
            this.model = new Events.EventModel();
            this.model.view = this;
            this.$el = $(this.el);
        },
        events: {
            'click a.collapse': 'collapse'
        }
    });
    AppView = Backbone.View.extend({
        el: '#app',

        initialize: function(opts) {
            if (window.n) {
                $('tbody tr').eq(0).children().effect('highlight', {
                    'color': '#D4F2AF'
                }, 3000);
            }
            $('a.kids-dropdown').click(function() {
                $(this).siblings('ul').toggle();
                return false;
            });
        },
        addEvent: function() {
            model = new EventView({ el: this });
        }
    });
    Events.Views = {
        'AppView': AppView
    };

})(emilyapp.module('events'));

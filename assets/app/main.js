(function() {
    var app = angular.module('stellar', []);

    app.controller('PanelShipController', function(){
        this.tab = 1;

        this.selectedTab = function(setTab){
            this.tab = setTab;
        };

        this.isSelected = function(checkTab){
            return this.tab === checkTab;
        };
    });
})();

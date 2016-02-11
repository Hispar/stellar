(function () {
    var app = angular.module('stellar', []);

    app.controller('PanelShipController', function ($scope, $http) {
        this.tab = 1;

        this.selectShip = function (id) {
            $http.get('/api/v1/ships/' + id)
                .then(function (res) {
                    $scope.ship = res.data;
                });
            this.tab = 2;
        };

        this.selectedTab = function (setTab) {
            this.tab = setTab;
        };

        this.isSelected = function (checkTab) {
            return this.tab === checkTab;
        };
    });
})();

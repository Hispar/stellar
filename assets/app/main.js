(function () {
    var app = angular.module('stellar', []);

    app.controller('PanelShipController', function ($scope, $http) {
        this.tab = 1;
        this.passengers = Object.keys(Array.apply(1, Array(10))).map(Number);

        this.selectShip = function (id) {
            $http.get('/api/v1/ships/' + id)
                .then(function (res) {
                    $scope.ship = res.data;
                });
            this.tab = 2;
        };

        this.editShip = function (id) {
            $http.get('/api/v1/ships/' + id)
                .then(function (res) {
                    $scope.ship = res.data;
                });
            this.tab = 3;
        };

        this.selectedTab = function (setTab) {
            this.tab = setTab;
        };

        this.isSelected = function (checkTab) {
            return this.tab === checkTab;
        };
    });
})();

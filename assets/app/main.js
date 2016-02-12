(function () {
    var app = angular.module('stellar', []);

    app.controller('PanelShipController', function ($scope, $http) {
        this.tab = 1;
        this.passengers = Object.keys(Array.apply(1, Array(10))).map(Number);

        $http.defaults.xsrfCookieName = 'csrftoken';
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';

        this.loadShips = function () {
            $http.get('/api/v1/ships/')
                .then(function (res) {
                    $scope.ships = res.data.results;
                });
        };

        /**
         * Load data from selected ship
         * @param id
         */
        this.selectShip = function (id) {
            $http.get('/api/v1/ships/' + id)
                .then(function (res) {
                    $scope.ship = res.data;
                });
            this.tab = 2;
        };

        /**
         * Load data to edit ship
         * @param id
         */
        this.editShip = function (id) {
            $http.get('/api/v1/ships/' + id)
                .then(function (res) {
                    $scope.ship = res.data;
                });
            this.tab = 3;
        };

        /**
         * Save configuration for the current ship
         * @param ship
         */
        this.reserve = function (ship) {
            $http.put('/api/v1/ships/' + ship.id + '/', ship)
                .then(function (res) {
                    $scope.ship = res.data;
                });
        };

        /**
         * Save current ship as a new one
         * @param ship
         */
        this.build = function (ship) {
            $http.post('/api/v1/ships/', ship)
                .then(function (res) {
                    $scope.ship = res.data;
                });
        };

        /**
         * Set current tab
         * @param setTab
         */
        this.selectedTab = function (setTab) {
            this.tab = setTab;
        };

        /**
         * Check selected tab
         * @param checkTab
         * @returns {boolean}
         */
        this.isSelected = function (checkTab) {
            return this.tab === checkTab;
        };
    });
})();

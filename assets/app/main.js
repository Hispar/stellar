(function () {
    var app = angular.module('stellar', []);

    app.controller('PanelShipController', function ($scope, $http) {
        this.tab = 1;
        this.passengers = Object.keys(Array.apply(1, Array(10))).map(Number);

        $http.defaults.xsrfCookieName = 'csrftoken';
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';

        this.loadShips = function () {
            this.tab = 1;
            $http.get('/api/v1/ships/')
                .then(function (res) {
                    res.data.reservation_date = new Date(res.data.reservation_date);
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
                    res.data.reservation_date = new Date(res.data.reservation_date);
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
                    res.data.reservation_date = new Date(res.data.reservation_date);
                    $scope.ship = res.data;
                });
            this.tab = 3;
        };

        /**
         * Save configuration for the current ship
         * @param ship
         */
        this.reserve = function (ship) {
            if (ship.boost === undefined) {
                ship.boost = false;
            }
            if (ship.detection === undefined) {
                ship.detection = false;
            }
            $http.put('/api/v1/ships/' + ship.id + '/', ship)
                .then(function (res) {
                    res.data.reservation_date = new Date(res.data.reservation_date);
                    $scope.ship = res.data;
                });
            ship.reservation_date = new Date(ship.reservation_date);
        };

        /**
         * Save current ship as a new one
         * @param ship
         */
        this.build = function (ship) {
            if (ship.boost === undefined) {
                ship.boost = false;
            }
            if (ship.detection === undefined) {
                ship.detection = false;
            }
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

        /**
         * Load map
         */
        this.loadmap = function () {
            lat = 28.182329;
            lon = -82.352912;

            var mapOptions = {
                center: new google.maps.LatLng(lat, lon),
                zoom: 9,
                mapTypeId: google.maps.MapTypeId.ROADMAP,
                scrollwheel: true,
                draggable: true,
                panControl: true,
                zoomControl: true,
                mapTypeControl: true,
                scaleControl: true,
                streetViewControl: false,
                overviewMapControl: true,
                rotateControl: true,
            };
            var mapDiv = document.getElementById('map');
            $scope.map = new google.maps.Map(mapDiv, mapOptions);
            $scope.map;
        }

        /**
         * Load map
         */
        this.showmap = function (lat, lon) {
            setTimeout(function() {google.maps.event.trigger($scope.map, 'resize')}, 100);
            if (lat === null) {
                lat = 28.182329;
            }
            if (lon === null) {
                lon = -82.352912;
            }
            var center = new google.maps.LatLng(lat, lon);
            $scope.map.setCenter(center);
        }
    });
})();

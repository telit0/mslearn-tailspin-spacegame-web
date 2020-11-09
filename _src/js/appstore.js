(function(){
    'use strict';

    angular.module('appstore.demo',[])
        .controller('appstoreController',['$scope','$http',appstoreController]);

    function appstoreController($scope,$http){
        $scope.data=[];
        $http.get('/appstore/sw')
            .then(function(response){
                $scope.data=response.data
            });
    };
}());

(function(){
    'use strict';

    angular.module('appstore.demo')
        .directive('appstoreSoftware',SoftwareDirective);

        function SoftwareDirective(){
            return {
                templateUrl: '/static/software.html',
                restrict: 'E'
            };
        }
})();


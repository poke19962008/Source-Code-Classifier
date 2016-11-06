(function() {
  'use strict';

  angular
    .module('frontend')
    .controller('MainController', MainController);

  /** @ngInject */
  function MainController($http, $scope) {
    $scope.loader = true;
    $scope.res = true; // change to true
    $scope.showTextArea = true;

    $scope.langs = {
      'Python': 'py',
      'C': 'c',
      'C++': 'cpp',
      'Java': 'java',
      'Ruby': 'ruby'
    }
    $scope.prob = {};

    $scope.maxProb = undefined;

    $scope.process = function() {
      $scope.loader = false;
      $http.post('http://10.5.59.27:5000/check', {'sc': $scope.sc})
      .then(function(res, err) {
        var d = res.data;

        var max = -1, maxExt;
        for (var ext in d) {
          console.log(ext);
          if (d[ext] > max) {
            max = d[ext];
            maxExt = ext;
          }
        }
        $scope.maxProb = maxExt;
        $scope.prob = d;

        $scope.loader = true;
        $scope.res = false;
      })
      .catch(function(err) {
        notie.alert(3, 'Error Processing Request', 2.5);
        $scope.loader = true;
      });
    }
  }
})();

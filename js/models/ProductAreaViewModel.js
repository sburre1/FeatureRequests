var ProductAreaModel = function(data){
    var self = this;
    self.id = ko.observable(data.id);
    self.label = ko.observable(data.label);
};

var viewModel = function(data) {
   var self = this;
   self.selectedChoice = ko.observable();
   self.areas = ko.observableArray([
        new ProductAreaModel({id: "policies", label: "Policies"}),
        new ProductAreaModel({id: "billing", label: "Billing"}),
        new ProductAreaModel({id: "claims", label: "Claims"}),
        new ProductAreaModel({id: "reports", label: "Reports"})
        ]);
};

ko.applyBindings(new viewModel(), document.getElementById("productAreas"));
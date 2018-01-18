var ClientModel = function(data){
    var self = this;
    self.id = ko.observable(data.id);
    self.label = ko.observable(data.label);
};

var viewModel = function(data) {
   var self = this;
   self.selectedChoice = ko.observable();
   self.clients = ko.observableArray([
        new ClientModel({id: "clientA", label: "Client A"}),
        new ClientModel({id: "clientB", label: "Client B"}),
        new ClientModel({id: "clientC", label: "Client C"})
        ]);
};

ko.applyBindings(new viewModel(), document.getElementById("clients"));
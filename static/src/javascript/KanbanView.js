odoo.define('extended_periods.extend.extendedperiodslist', function (require) {
"use strict";
    var KanbanController = require('web.KanbanController');
    var KanbanView = require('web.KanbanView');
    var ListController = require('web.ListController');
    var ListView = require('web.ListView');
    var viewRegistry = require('web.view_registry');


    var ExpensesListView = ListView.extend({
        config: _.extend({}, ListView.prototype.config, {
            Controller: ExpensesListController,
        }),
    });



    var ExpensesKanbanView = KanbanView.extend({
        config: _.extend({}, KanbanView.prototype.config, {
            Controller: ExpensesKanbanController,
        }),
    });

    viewRegistry.add('extended_tree', ExpensesListView);
    viewRegistry.add('extended_kanban', ExpensesKanbanView);
});

app_name = "verp"
app_title = "VERP"
app_publisher = "Frappe Technologies Pvt. Ltd."
app_description = """ERP made simple"""
app_icon = "fa fa-th"
app_color = "#e74c3c"
app_email = "info@verp.com"
app_license = "GNU General Public License (v3)"
source_link = "https://github.com/frappe/verp"
app_logo_url = "/assets/verp/images/verp-logo.svg"


develop_version = "14.x.x-develop"

app_include_js = "verp.bundle.js"
app_include_css = "verp.bundle.css"
web_include_js = "verp-web.bundle.js"
web_include_css = "verp-web.bundle.css"
email_css = "email_verp.bundle.css"

doctype_js = {
	"Address": "public/js/address.js",
	"Communication": "public/js/communication.js",
	"Event": "public/js/event.js",
	"Newsletter": "public/js/newsletter.js",
	"Contact": "public/js/contact.js",
}

override_doctype_class = {"Address": "verp.accounts.custom.address.VERPAddress"}

override_whitelisted_methods = {"frappe.www.contact.send_message": "verp.templates.utils.send_message"}

welcome_email = "verp.setup.utils.welcome_email"

# setup wizard
setup_wizard_requires = "assets/verp/js/setup_wizard.js"
setup_wizard_stages = "verp.setup.setup_wizard.setup_wizard.get_setup_stages"
setup_wizard_complete = "verp.setup.setup_wizard.setup_wizard.setup_demo"
setup_wizard_test = "verp.setup.setup_wizard.test_setup_wizard.run_setup_wizard_test"

before_install = [
	"verp.setup.install.check_setup_wizard_not_completed",
]
after_install = "verp.setup.install.after_install"

boot_session = "verp.startup.boot.boot_session"
notification_config = "verp.startup.notifications.get_notification_config"
get_help_messages = "verp.utilities.activation.get_help_messages"
leaderboards = "verp.startup.leaderboard.get_leaderboards"
filters_config = "verp.startup.filters.get_filters_config"
additional_print_settings = "verp.controllers.print_settings.get_print_settings"

on_session_creation = "verp.portal.utils.create_customer_or_supplier"

treeviews = [
	"Account",
	"Cost Center",
	"Warehouse",
	"Item Group",
	"Customer Group",
	"Supplier Group",
	"Sales Person",
	"Territory",
	"Department",
]

demo_master_doctypes = [
	"item_group",
	"item",
	"customer_group",
	"supplier_group",
	"customer",
	"supplier",
]
demo_transaction_doctypes = [
	"purchase_order",
	"sales_order",
]

jinja = {
	"methods": [
		"verp.stock.serial_batch_bundle.get_serial_or_batch_nos",
	],
}

# website
webform_list_context = "verp.controllers.website_list_for_contact.get_webform_list_context"

calendars = ["Task", "Work Order", "Sales Order", "Holiday List", "ToDo"]

website_generators = ["BOM", "Sales Partner"]

website_context = {
	"favicon": "/assets/verp/images/verp-favicon.svg",
	"splash_image": "/assets/verp/images/verp-logo.svg",
}

# nosemgrep
website_route_rules = [
	{"from_route": "/orders", "to_route": "Sales Order"},
	{
		"from_route": "/orders/<path:name>",
		"to_route": "order",
		"defaults": {"doctype": "Sales Order", "parents": [{"label": "Orders", "route": "orders"}]},
	},
	{"from_route": "/invoices", "to_route": "Sales Invoice"},
	{
		"from_route": "/invoices/<path:name>",
		"to_route": "order",
		"defaults": {
			"doctype": "Sales Invoice",
			"parents": [{"label": "Invoices", "route": "invoices"}],
		},
	},
	{"from_route": "/supplier-quotations", "to_route": "Supplier Quotation"},
	{
		"from_route": "/supplier-quotations/<path:name>",
		"to_route": "order",
		"defaults": {
			"doctype": "Supplier Quotation",
			"parents": [{"label": "Supplier Quotation", "route": "supplier-quotations"}],
		},
	},
	{"from_route": "/purchase-orders", "to_route": "Purchase Order"},
	{
		"from_route": "/purchase-orders/<path:name>",
		"to_route": "order",
		"defaults": {
			"doctype": "Purchase Order",
			"parents": [{"label": "Purchase Order", "route": "purchase-orders"}],
		},
	},
	{"from_route": "/purchase-invoices", "to_route": "Purchase Invoice"},
	{
		"from_route": "/purchase-invoices/<path:name>",
		"to_route": "order",
		"defaults": {
			"doctype": "Purchase Invoice",
			"parents": [{"label": "Purchase Invoice", "route": "purchase-invoices"}],
		},
	},
	{"from_route": "/quotations", "to_route": "Quotation"},
	{
		"from_route": "/quotations/<path:name>",
		"to_route": "order",
		"defaults": {
			"doctype": "Quotation",
			"parents": [{"label": "Quotations", "route": "quotations"}],
		},
	},
	{"from_route": "/shipments", "to_route": "Delivery Note"},
	{
		"from_route": "/shipments/<path:name>",
		"to_route": "order",
		"defaults": {
			"doctype": "Delivery Note",
			"parents": [{"label": "Shipments", "route": "shipments"}],
		},
	},
	{"from_route": "/rfq", "to_route": "Request for Quotation"},
	{
		"from_route": "/rfq/<path:name>",
		"to_route": "rfq",
		"defaults": {
			"doctype": "Request for Quotation",
			"parents": [{"label": "Request for Quotation", "route": "rfq"}],
		},
	},
	{"from_route": "/addresses", "to_route": "Address"},
	{
		"from_route": "/addresses/<path:name>",
		"to_route": "addresses",
		"defaults": {"doctype": "Address", "parents": [{"label": "Addresses", "route": "addresses"}]},
	},
	{"from_route": "/boms", "to_route": "BOM"},
	{"from_route": "/timesheets", "to_route": "Timesheet"},
	{"from_route": "/material-requests", "to_route": "Material Request"},
	{
		"from_route": "/material-requests/<path:name>",
		"to_route": "material_request_info",
		"defaults": {
			"doctype": "Material Request",
			"parents": [{"label": "Material Request", "route": "material-requests"}],
		},
	},
	{"from_route": "/project", "to_route": "Project"},
	{"from_route": "/tasks", "to_route": "Task"},
]

standard_portal_menu_items = [
	{"title": "Projects", "route": "/project", "reference_doctype": "Project", "role": "Customer"},
	{
		"title": "Request for Quotations",
		"route": "/rfq",
		"reference_doctype": "Request for Quotation",
		"role": "Supplier",
	},
	{
		"title": "Supplier Quotation",
		"route": "/supplier-quotations",
		"reference_doctype": "Supplier Quotation",
		"role": "Supplier",
	},
	{
		"title": "Purchase Orders",
		"route": "/purchase-orders",
		"reference_doctype": "Purchase Order",
		"role": "Supplier",
	},
	{
		"title": "Purchase Invoices",
		"route": "/purchase-invoices",
		"reference_doctype": "Purchase Invoice",
		"role": "Supplier",
	},
	{
		"title": "Quotations",
		"route": "/quotations",
		"reference_doctype": "Quotation",
		"role": "Customer",
	},
	{
		"title": "Orders",
		"route": "/orders",
		"reference_doctype": "Sales Order",
		"role": "Customer",
	},
	{
		"title": "Invoices",
		"route": "/invoices",
		"reference_doctype": "Sales Invoice",
		"role": "Customer",
	},
	{
		"title": "Shipments",
		"route": "/shipments",
		"reference_doctype": "Delivery Note",
		"role": "Customer",
	},
	{"title": "Issues", "route": "/issues", "reference_doctype": "Issue", "role": "Customer"},
	{"title": "Addresses", "route": "/addresses", "reference_doctype": "Address"},
	{
		"title": "Timesheets",
		"route": "/timesheets",
		"reference_doctype": "Timesheet",
		"role": "Customer",
	},
	{"title": "Newsletter", "route": "/newsletters", "reference_doctype": "Newsletter"},
	{
		"title": "Material Request",
		"route": "/material-requests",
		"reference_doctype": "Material Request",
		"role": "Customer",
	},
	{"title": "Appointment Booking", "route": "/book_appointment"},
]

sounds = [
	{"name": "incoming-call", "src": "/assets/verp/sounds/incoming-call.mp3", "volume": 0.2},
	{"name": "call-disconnect", "src": "/assets/verp/sounds/call-disconnect.mp3", "volume": 0.2},
]

has_upload_permission = {"Employee": "verp.setup.doctype.employee.employee.has_upload_permission"}

has_website_permission = {
	"Sales Order": "verp.controllers.website_list_for_contact.has_website_permission",
	"Quotation": "verp.controllers.website_list_for_contact.has_website_permission",
	"Sales Invoice": "verp.controllers.website_list_for_contact.has_website_permission",
	"Supplier Quotation": "verp.controllers.website_list_for_contact.has_website_permission",
	"Purchase Order": "verp.controllers.website_list_for_contact.has_website_permission",
	"Purchase Invoice": "verp.controllers.website_list_for_contact.has_website_permission",
	"Material Request": "verp.controllers.website_list_for_contact.has_website_permission",
	"Delivery Note": "verp.controllers.website_list_for_contact.has_website_permission",
	"Issue": "verp.support.doctype.issue.issue.has_website_permission",
	"Timesheet": "verp.controllers.website_list_for_contact.has_website_permission",
	"Project": "verp.controllers.website_list_for_contact.has_website_permission",
}

before_tests = "verp.setup.utils.before_tests"


period_closing_doctypes = [
	"Sales Invoice",
	"Purchase Invoice",
	"Journal Entry",
	"Bank Clearance",
	"Stock Entry",
	"Dunning",
	"Invoice Discounting",
	"Payment Entry",
	"Period Closing Voucher",
	"Process Deferred Accounting",
	"Asset",
	"Asset Capitalization",
	"Asset Repair",
	"Delivery Note",
	"Landed Cost Voucher",
	"Purchase Receipt",
	"Stock Reconciliation",
	"Subcontracting Receipt",
]

doc_events = {
	"*": {
		"validate": [
			"verp.support.doctype.service_level_agreement.service_level_agreement.apply",
			"verp.setup.doctype.transaction_deletion_record.transaction_deletion_record.check_for_running_deletion_job",
		],
	},
	tuple(period_closing_doctypes): {
		"validate": "verp.accounts.doctype.accounting_period.accounting_period.validate_accounting_period_on_doc_save",
	},
	"Stock Entry": {
		"on_submit": "verp.stock.doctype.material_request.material_request.update_completed_and_requested_qty",
		"on_cancel": "verp.stock.doctype.material_request.material_request.update_completed_and_requested_qty",
	},
	"User": {
		"after_insert": "frappe.contacts.doctype.contact.contact.update_contact",
		"validate": "verp.setup.doctype.employee.employee.validate_employee_role",
		"on_update": [
			"verp.setup.doctype.employee.employee.update_user_permissions",
			"verp.portal.utils.set_default_role",
		],
	},
	"Communication": {
		"on_update": [
			"verp.support.doctype.service_level_agreement.service_level_agreement.on_communication_update",
			"verp.support.doctype.issue.issue.set_first_response_time",
		],
		"after_insert": "verp.crm.utils.link_communications_with_prospect",
	},
	"Event": {
		"after_insert": "verp.crm.utils.link_events_with_prospect",
	},
	"Sales Invoice": {
		"on_submit": [
			"verp.regional.create_transaction_log",
			"verp.regional.italy.utils.sales_invoice_on_submit",
		],
		"on_cancel": ["verp.regional.italy.utils.sales_invoice_on_cancel"],
		"on_trash": "verp.regional.check_deletion_permission",
	},
	"Purchase Invoice": {
		"validate": [
			"verp.regional.united_arab_emirates.utils.update_grand_total_for_rcm",
			"verp.regional.united_arab_emirates.utils.validate_returns",
		]
	},
	"Payment Entry": {
		"on_submit": [
			"verp.regional.create_transaction_log",
			"verp.accounts.doctype.dunning.dunning.resolve_dunning",
		],
		"on_cancel": ["verp.accounts.doctype.dunning.dunning.resolve_dunning"],
		"on_trash": "verp.regional.check_deletion_permission",
	},
	"Address": {
		"validate": [
			"verp.regional.italy.utils.set_state_code",
		],
	},
	"Contact": {
		"on_trash": "verp.support.doctype.issue.issue.update_issue",
		"after_insert": "verp.telephony.doctype.call_log.call_log.link_existing_conversations",
		"validate": ["verp.crm.utils.update_lead_phone_numbers"],
	},
	"Email Unsubscribe": {
		"after_insert": "verp.crm.doctype.email_campaign.email_campaign.unsubscribe_recipient"
	},
	"Integration Request": {
		"validate": "verp.accounts.doctype.payment_request.payment_request.validate_payment"
	},
}

# function should expect the variable and doc as arguments
naming_series_variables = {
	"FY": "verp.accounts.utils.parse_naming_series_variable",
}

# On cancel event Payment Entry will be exempted and all linked submittable doctype will get cancelled.
# to maintain data integrity we exempted payment entry. it will un-link when sales invoice get cancelled.
# if payment entry not in auto cancel exempted doctypes it will cancel payment entry.
auto_cancel_exempted_doctypes = [
	"Payment Entry",
]

scheduler_events = {
	"cron": {
		"0/15 * * * *": [
			"verp.manufacturing.doctype.bom_update_log.bom_update_log.resume_bom_cost_update_jobs",
			"verp.accounts.doctype.process_payment_reconciliation.process_payment_reconciliation.trigger_reconciliation_for_queued_docs",
		],
		"0/30 * * * *": [
			"verp.utilities.doctype.video.video.update_youtube_data",
		],
		# Hourly but offset by 30 minutes
		"30 * * * *": [
			"verp.accounts.doctype.gl_entry.gl_entry.rename_gle_sle_docs",
		],
		# Daily but offset by 45 minutes
		"45 0 * * *": [
			"verp.stock.reorder_item.reorder_item",
		],
	},
	"hourly": [
		"verp.verp_integrations.doctype.plaid_settings.plaid_settings.automatic_synchronization",
		"verp.projects.doctype.project.project.project_status_update_reminder",
		"verp.projects.doctype.project.project.hourly_reminder",
		"verp.projects.doctype.project.project.collect_project_status",
	],
	"hourly_long": [
		"verp.stock.doctype.repost_item_valuation.repost_item_valuation.repost_entries",
		"verp.utilities.bulk_transaction.retry",
	],
	"daily": [
		"verp.support.doctype.issue.issue.auto_close_tickets",
		"verp.crm.doctype.opportunity.opportunity.auto_close_opportunity",
		"verp.controllers.accounts_controller.update_invoice_status",
		"verp.accounts.doctype.fiscal_year.fiscal_year.auto_create_fiscal_year",
		"verp.projects.doctype.task.task.set_tasks_as_overdue",
		"verp.stock.doctype.serial_no.serial_no.update_maintenance_status",
		"verp.buying.doctype.supplier_scorecard.supplier_scorecard.refresh_scorecards",
		"verp.setup.doctype.company.company.cache_companies_monthly_sales_history",
		"verp.assets.doctype.asset.asset.update_maintenance_status",
		"verp.assets.doctype.asset.asset.make_post_gl_entry",
		"verp.crm.doctype.contract.contract.update_status_for_contracts",
		"verp.projects.doctype.project.project.update_project_sales_billing",
		"verp.projects.doctype.project.project.send_project_status_email_to_users",
		"verp.quality_management.doctype.quality_review.quality_review.review",
		"verp.support.doctype.service_level_agreement.service_level_agreement.check_agreement_status",
		"verp.crm.doctype.email_campaign.email_campaign.send_email_to_leads_or_contacts",
		"verp.crm.doctype.email_campaign.email_campaign.set_email_campaign_status",
		"verp.selling.doctype.quotation.quotation.set_expired_status",
		"verp.buying.doctype.supplier_quotation.supplier_quotation.set_expired_status",
		"verp.accounts.doctype.process_statement_of_accounts.process_statement_of_accounts.send_auto_email",
		"verp.accounts.utils.auto_create_exchange_rate_revaluation_daily",
		"verp.accounts.utils.run_ledger_health_checks",
	],
	"weekly": [
		"verp.accounts.utils.auto_create_exchange_rate_revaluation_weekly",
	],
	"daily_long": [
		"verp.accounts.doctype.process_subscription.process_subscription.create_subscription_process",
		"verp.setup.doctype.email_digest.email_digest.send",
		"verp.manufacturing.doctype.bom_update_tool.bom_update_tool.auto_update_latest_price_in_all_boms",
		"verp.crm.utils.open_leads_opportunities_based_on_todays_event",
		"verp.assets.doctype.asset.depreciation.post_depreciation_entries",
	],
	"monthly_long": [
		"verp.accounts.deferred_revenue.process_deferred_accounting",
	],
}

email_brand_image = "assets/verp/images/verp-logo.jpg"

default_mail_footer = """
	<span>
		Sent via
		<a class="text-muted" href="https://verp.com?source=via_email_footer" target="_blank">
			VERP
		</a>
	</span>
"""

get_translated_dict = {("doctype", "Global Defaults"): "frappe.geo.country_info.get_translated_dict"}

bot_parsers = [
	"verp.utilities.bot.FindItemBot",
]

get_site_info = "verp.utilities.get_site_info"

payment_gateway_enabled = "verp.accounts.utils.create_payment_gateway_account"

communication_doctypes = ["Customer", "Supplier"]

advance_payment_receivable_doctypes = ["Sales Order"]
advance_payment_payable_doctypes = ["Purchase Order"]

invoice_doctypes = ["Sales Invoice", "Purchase Invoice"]

bank_reconciliation_doctypes = [
	"Payment Entry",
	"Journal Entry",
	"Purchase Invoice",
	"Sales Invoice",
]

accounting_dimension_doctypes = [
	"GL Entry",
	"Payment Ledger Entry",
	"Sales Invoice",
	"Purchase Invoice",
	"Payment Entry",
	"Asset",
	"Stock Entry",
	"Budget",
	"Delivery Note",
	"Sales Invoice Item",
	"Purchase Invoice Item",
	"Purchase Order Item",
	"Sales Order Item",
	"Journal Entry Account",
	"Material Request Item",
	"Delivery Note Item",
	"Purchase Receipt Item",
	"Stock Entry Detail",
	"Payment Entry Deduction",
	"Sales Taxes and Charges",
	"Purchase Taxes and Charges",
	"Shipping Rule",
	"Landed Cost Item",
	"Asset Value Adjustment",
	"Asset Repair",
	"Asset Capitalization",
	"Loyalty Program",
	"Stock Reconciliation",
	"POS Profile",
	"Opening Invoice Creation Tool",
	"Opening Invoice Creation Tool Item",
	"Subscription",
	"Subscription Plan",
	"POS Invoice",
	"POS Invoice Item",
	"Purchase Order",
	"Purchase Receipt",
	"Sales Order",
	"Subcontracting Order",
	"Subcontracting Order Item",
	"Subcontracting Receipt",
	"Subcontracting Receipt Item",
	"Account Closing Balance",
	"Supplier Quotation",
	"Supplier Quotation Item",
	"Payment Reconciliation",
	"Payment Reconciliation Allocation",
	"Payment Request",
]

get_matching_queries = (
	"verp.accounts.doctype.bank_reconciliation_tool.bank_reconciliation_tool.get_matching_queries"
)

get_amounts_not_reflected_in_system_for_bank_reconciliation_statement = "verp.accounts.report.bank_reconciliation_statement.bank_reconciliation_statement.get_amounts_not_reflected_in_system_for_bank_reconciliation_statement"

get_payment_entries_for_bank_clearance = (
	"verp.accounts.doctype.bank_clearance.bank_clearance.get_payment_entries_for_bank_clearance"
)

get_entries_for_bank_clearance_summary = "verp.accounts.report.bank_clearance_summary.bank_clearance_summary.get_entries_for_bank_clearance_summary"

get_entries_for_bank_reconciliation_statement = "verp.accounts.report.bank_reconciliation_statement.bank_reconciliation_statement.get_entries_for_bank_reconciliation_statement"

regional_overrides = {
	"France": {"verp.tests.test_regional.test_method": "verp.regional.france.utils.test_method"},
	"United Arab Emirates": {
		"verp.controllers.taxes_and_totals.update_itemised_tax_data": "verp.regional.united_arab_emirates.utils.update_itemised_tax_data",
		"verp.accounts.doctype.purchase_invoice.purchase_invoice.make_regional_gl_entries": "verp.regional.united_arab_emirates.utils.make_regional_gl_entries",
	},
	"Saudi Arabia": {
		"verp.controllers.taxes_and_totals.update_itemised_tax_data": "verp.regional.united_arab_emirates.utils.update_itemised_tax_data"
	},
	"Italy": {
		"verp.controllers.taxes_and_totals.update_itemised_tax_data": "verp.regional.italy.utils.update_itemised_tax_data",
		"verp.controllers.accounts_controller.validate_regional": "verp.regional.italy.utils.sales_invoice_validate",
	},
}
user_privacy_documents = [
	{
		"doctype": "Lead",
		"match_field": "email_id",
		"personal_fields": ["phone", "mobile_no", "fax", "website", "lead_name"],
	},
	{
		"doctype": "Opportunity",
		"match_field": "contact_email",
		"personal_fields": ["contact_mobile", "contact_display", "customer_name"],
	},
]

# VERP doctypes for Global Search
global_search_doctypes = {
	"Default": [
		{"doctype": "Customer", "index": 0},
		{"doctype": "Supplier", "index": 1},
		{"doctype": "Item", "index": 2},
		{"doctype": "Warehouse", "index": 3},
		{"doctype": "Account", "index": 4},
		{"doctype": "Employee", "index": 5},
		{"doctype": "BOM", "index": 6},
		{"doctype": "Sales Invoice", "index": 7},
		{"doctype": "Sales Order", "index": 8},
		{"doctype": "Quotation", "index": 9},
		{"doctype": "Work Order", "index": 10},
		{"doctype": "Purchase Order", "index": 11},
		{"doctype": "Purchase Receipt", "index": 12},
		{"doctype": "Purchase Invoice", "index": 13},
		{"doctype": "Delivery Note", "index": 14},
		{"doctype": "Stock Entry", "index": 15},
		{"doctype": "Material Request", "index": 16},
		{"doctype": "Delivery Trip", "index": 17},
		{"doctype": "Pick List", "index": 18},
		{"doctype": "Payment Entry", "index": 22},
		{"doctype": "Lead", "index": 23},
		{"doctype": "Opportunity", "index": 24},
		{"doctype": "Item Price", "index": 25},
		{"doctype": "Purchase Taxes and Charges Template", "index": 26},
		{"doctype": "Sales Taxes and Charges", "index": 27},
		{"doctype": "Asset", "index": 28},
		{"doctype": "Project", "index": 29},
		{"doctype": "Task", "index": 30},
		{"doctype": "Timesheet", "index": 31},
		{"doctype": "Issue", "index": 32},
		{"doctype": "Serial No", "index": 33},
		{"doctype": "Batch", "index": 34},
		{"doctype": "Branch", "index": 35},
		{"doctype": "Department", "index": 36},
		{"doctype": "Designation", "index": 38},
		{"doctype": "Maintenance Schedule", "index": 45},
		{"doctype": "Maintenance Visit", "index": 46},
		{"doctype": "Warranty Claim", "index": 47},
	],
}

additional_timeline_content = {"*": ["verp.telephony.doctype.call_log.call_log.get_linked_call_logs"]}


extend_bootinfo = [
	"verp.support.doctype.service_level_agreement.service_level_agreement.add_sla_doctypes",
	"verp.startup.boot.bootinfo",
]


default_log_clearing_doctypes = {
	"Repost Item Valuation": 60,
}

export_python_type_annotations = True

fields_for_group_similar_items = ["qty", "amount"]

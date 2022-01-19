from prettytable import PrettyTable
import sentry_sdk

sentry_sdk.init(
    "https://f944bc42dd1d4ed0b8a922abb3e139b2@o556363.ingest.sentry.io/5687123",
    max_breadcrumbs=50,
    debug=True,

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

table = PrettyTable()
table.field_names = ['Name', 'Password', 'Sex', 'Age']
table.add_row(['Anna', '123123', 'W', '22'])
table.add_row(['Kate', '0000', 'W', '25'])
table.add_row(['Pope', '789', 'M', '52'])
table.add_row(['Brut', '111111', 'M', '47'])
table.add_row(['Leo', '321321', 'M', '82'])
division_by_zero = 1 / 0
table.add_row(['Jon', '963852741', 'M', '36'])

print(table)
print(table.get_string(fields=['Age']))
print(table.get_string(start=1, end=4))

table.align = "r"
print(table)

print(table.get_string(sortby="Age"))

table.sortby = "Age"
print(table)

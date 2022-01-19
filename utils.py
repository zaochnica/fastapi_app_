import sentry_sdk
sentry_sdk.init(
    "https://f944bc42dd1d4ed0b8a922abb3e139b2@o556363.ingest.sentry.io/5687123",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)
